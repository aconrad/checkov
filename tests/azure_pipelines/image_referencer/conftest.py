from __future__ import annotations

from typing import Any

import pytest


@pytest.fixture()
def image_cached_result() -> dict[str, Any]:
    return {
        "results": [
            {
                "id": "sha256:2460522297a148c1bcb477b126451ed44cca05c916694367313be1a91c69f793",
                "name": "redis:latest",
                "distro": "Debian GNU/Linux 11 (bullseye)",
                "distroRelease": "bullseye",
                "digest": "sha256:091a7b5de688f283b30a4942280b64cf822bbdab0abfb2d2ce6db989f2d3c3f4",
                "collections": [
                    "All"
                ],
                "packages": [
                    {
                        "type": "os",
                        "name": "tzdata",
                        "version": "2021a-1+deb11u5"
                    }
                ],
                "compliances": [
                    {
                        "id": 41,
                        "title": "(CIS_Docker_v1.2.0 - 4.1) Image should be created with a non-root user",
                        "severity": "high",
                        "description": "It is a good practice to run the container as a non-root user, if possible. Though user\nnamespace mapping is now available, if a user is already defined in the container image, the\ncontainer is run as that user by default and specific user namespace remapping is not\nrequired"
                    }
                ],
                "complianceDistribution": {
                    "critical": 0,
                    "high": 1,
                    "medium": 0,
                    "low": 0,
                    "total": 1
                },
                "complianceScanPassed": "true",
                "vulnerabilities": [
                    {
                        "id": "CVE-2021-38297",
                        "status": "fixed in 1.17.2, 1.16.9",
                        "cvss": 9.8,
                        "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
                        "description": "Go before 1.16.9 and 1.17.x before 1.17.2 has a Buffer Overflow via large arguments in a function invocation from a WASM module, when GOARCH\u003dwasm GOOS\u003djs is used.",
                        "severity": "critical",
                        "packageName": "go",
                        "packageVersion": "1.16.7",
                        "link": "https://nvd.nist.gov/vuln/detail/CVE-2021-38297",
                        "riskFactors": [
                            "Attack complexity: low",
                            "Attack vector: network",
                            "Critical severity",
                            "Has fix",
                            "Recent vulnerability"
                        ],
                        "impactedVersions": [
                            "\u003c1.16.9"
                        ],
                        "publishedDate": "2021-10-18T06:15:00Z",
                        "discoveredDate": "2022-09-18T14:26:20Z",
                        "fixDate": "2021-10-18T06:15:00Z"
                    },
                    {
                        "id": "CVE-2022-23806",
                        "status": "fixed in 1.17.7, 1.16.14",
                        "cvss": 9.1,
                        "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H",
                        "description": "Curve.IsOnCurve in crypto/elliptic in Go before 1.16.14 and 1.17.x before 1.17.7 can incorrectly return true in situations with a big.Int value that is not a valid field element.",
                        "severity": "critical",
                        "packageName": "go",
                        "packageVersion": "1.16.7",
                        "link": "https://nvd.nist.gov/vuln/detail/CVE-2022-23806",
                        "riskFactors": [
                            "Recent vulnerability",
                            "Attack complexity: low",
                            "Attack vector: network",
                            "Critical severity",
                            "Has fix"
                        ],
                        "impactedVersions": [
                            "\u003c1.16.14"
                        ],
                        "publishedDate": "2022-02-11T01:15:00Z",
                        "discoveredDate": "2022-09-18T14:26:20Z",
                        "fixDate": "2022-02-11T01:15:00Z"
                    },
                    {
                        "id": "CVE-2022-30580",
                        "status": "fixed in 1.18.3, 1.17.11",
                        "cvss": 7.8,
                        "vector": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
                        "description": "Code injection in Cmd.Start in os/exec before Go 1.17.11 and Go 1.18.3 allows execution of any binaries in the working directory named either \\\"..com\\\" or \\\"..exe\\\" by calling Cmd.Run, Cmd.Start, Cmd.Output, or Cmd.CombinedOutput when Cmd.Path is unset.",
                        "severity": "high",
                        "packageName": "go",
                        "packageVersion": "1.16.7",
                        "link": "https://nvd.nist.gov/vuln/detail/CVE-2022-30580",
                        "riskFactors": [
                            "Attack complexity: low",
                            "Has fix",
                            "High severity",
                            "Recent vulnerability"
                        ],
                        "impactedVersions": [
                            "\u003c1.17.11"
                        ],
                        "publishedDate": "2022-08-10T20:15:00Z",
                        "discoveredDate": "2022-09-18T14:26:20Z",
                        "fixDate": "2022-08-10T20:15:00Z"
                    }
                ],
                "vulnerabilityDistribution": {
                    "critical": 2,
                    "high": 19,
                    "medium": 5,
                    "low": 12,
                    "total": 38
                },
                "vulnerabilityScanPassed": "true"
            }
        ]
    }

@pytest.fixture()
def license_statuses_result() -> list[dict[str, str]]:
    return [{
        "package_name": "dpkg",
        "package_version": "1.20.12",
        "policy": "BC_LIC_1",
        "license": "GPL-2.0+",
        "status": "COMPLIANT"
    },
    {
        "package_name": "systemd",
        "package_version": "247.3-7+deb11u1",
        "policy": "BC_LIC_1",
        "license": "LGPL-2.1-or-later",
        "status": "COMPLIANT"
    }]
