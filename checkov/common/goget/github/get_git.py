from __future__ import annotations

import logging
import re
import shutil

from checkov.common.goget.base_getter import BaseGetter
from checkov.common.template_logger_adapter import get_logger_with_template_adapter
from checkov.common.util.contextmanagers import temp_environ

try:
    from git import Repo
    git_import_error = None
except ImportError as e:
    git_import_error = e

COMMIT_ID_PATTERN = re.compile(r"\?(ref=)(?P<commit_id>([0-9a-f]{40}))")
TAG_PATTERN = re.compile(r'\?(ref=)(?P<tag>(.*))')


class GitGetter(BaseGetter):
    def __init__(self, url: str, create_clone_and_result_dirs: bool = True) -> None:
        self.logger = get_logger_with_template_adapter(logging.getLogger(__name__))
        self.create_clone_and_res_dirs = create_clone_and_result_dirs
        self.tag = ''
        self.commit_id: str | None = None

        if "?ref" in url:
            url = self.extract_git_ref(url=url)

        super().__init__(url)

    def extract_git_ref(self, url: str) -> str:
        search_commit_id = re.search(COMMIT_ID_PATTERN, url)
        if search_commit_id:
            self.commit_id = search_commit_id.group("commit_id")
            url = re.sub(COMMIT_ID_PATTERN, '', url)
            return url

        search_tag = re.search(TAG_PATTERN, url)
        if search_tag:
            self.tag = search_tag.group("tag")
            # remove tag/ or tags/ from ref= to get actual branch name
            self.tag = re.sub('tag.*/', '', self.tag)
            url = re.sub(TAG_PATTERN, '', url)
            return url

        logging.info(f"Module URL has an unknown ref: {url}")

        return url

    def do_get(self) -> str:
        if git_import_error is not None:
            raise ImportError("Unable to load git module (is the git executable available?)") \
                from git_import_error

        git_url, internal_dir = self._source_subdir()

        clone_dir = self.temp_dir + "/clone/" if self.create_clone_and_res_dirs else self.temp_dir
        self._clone(git_url, clone_dir)

        if internal_dir:
            clone_dir = clone_dir + internal_dir

        if self.create_clone_and_res_dirs:
            result_dir = self.temp_dir + "/result/"
            shutil.copytree(clone_dir, result_dir)
            return result_dir

        return clone_dir

    def _clone(self, git_url: str, clone_dir: str) -> None:
        self.logger.debug(f"cloning {self.url if '@' not in self.url else self.url.split('@')[1]} to {clone_dir}")
        with temp_environ(GIT_TERMINAL_PROMPT="0"):  # disables user prompts originating from GIT
            if self.commit_id:
                repo = Repo.clone_from(git_url, clone_dir, no_checkout=True)  # need to be a full git clone
                repo.git.checkout(self.commit_id)
            elif self.tag:
                Repo.clone_from(git_url, clone_dir, depth=1, b=self.tag)
            else:
                Repo.clone_from(git_url, clone_dir, depth=1)

    # Split source url into Git url and subdirectory path e.g. test.com/repo//repo/subpath becomes 'test.com/repo', '/repo/subpath')
    # Also see reference implementation @ go-getter https://github.com/hashicorp/go-getter/blob/main/source.go
    def _source_subdir(self) -> tuple[str, str]:
        stop = len(self.url)

        query_index = self.url.find("?")
        if query_index > -1:
            stop = query_index

        start = 0
        scheme_index = self.url.find("://", start, stop)
        if scheme_index > -1:
            start = scheme_index + 3

        subdir_index = self.url.find("//", start, stop)
        if subdir_index == -1:
            return self.url, ""

        internal_dir = self.url[subdir_index + 1:stop]  # Note: Internal dir is expected to start with /
        git_url = self.url[:subdir_index] + self.url[stop:]

        return git_url, internal_dir
