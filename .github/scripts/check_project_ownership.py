"""PR이 본인 소유가 아닌 projects/<github아이디>/ 폴더를 건드리는지 확인합니다.

이 저장소의 관례상 브랜치 이름 = 작성자 GitHub 아이디이므로,
PR 브랜치 이름과 다른 projects/<아이디>/ 경로가 바뀌면 실패시킵니다.
"""

import os
import subprocess
import sys


def main() -> int:
    base_sha = os.environ["BASE_SHA"]
    head_sha = os.environ["HEAD_SHA"]
    branch = os.environ["BRANCH"]

    diff = subprocess.run(
        ["git", "diff", "--name-only", base_sha, head_sha],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()

    errors = []
    for path in diff:
        if not path.startswith("projects/"):
            continue
        parts = path.split("/")
        if len(parts) < 2:
            continue
        owner = parts[1]
        if owner != branch:
            errors.append(path)

    if errors:
        print("다른 팀원의 프로젝트 폴더를 수정하는 변경이 포함되어 있습니다:\n")
        for path in errors:
            print(f"  - {path}")
        print(
            f"\n이 PR의 브랜치는 '{branch}'인데, 위 파일들은 다른 사람의 projects/ 폴더에 있습니다."
            f" 본인 폴더(projects/{branch}/)만 이 PR에서 수정해주세요."
        )
        return 1

    print("프로젝트 폴더 소유권 검사 통과: 본인 폴더만 수정했습니다.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
