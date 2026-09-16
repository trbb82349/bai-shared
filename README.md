# BAI 작업 공유

BAI 소모임원들이 각자 AI 에이전트(Claude Code/Codex 등)로 만든 **프로젝트 파일**과, 그 작업 맥락을 정리한 **핸드오프 문서**를 한 저장소에서 주고받기 위한 공간입니다.

## 폴더 구조

```
bai-shared/
├── handoffs/                  — 세션이 끝날 때 남기는 짧은 요약 문서
│   ├── template.md
│   └── YYYY-MM-DD-이름-핸드오프.md
└── projects/                  — 실제 프로젝트 코드·데이터, 사람(GitHub 아이디)별로 구분
    ├── trbb82349/
    │   └── careerlens-mvp/
    └── (다른 팀원 GitHub 아이디)/
        └── (그 사람의 프로젝트)/
```

프로젝트 폴더는 **사람 기준**으로 나뉩니다 — 팀원이 늘어나도 "누가 만든 건지" 한눈에 보이도록 하기 위해서입니다. 이름과 GitHub 아이디를 연결한 표는 [MEMBERS.md](MEMBERS.md)에 있어서, 아래 명령어에서 GitHub 아이디 대신 이름만 말해도 됩니다.

## 브랜치 작업 → PR 생성 → main merge 작업 흐름

내 작업을 공유할 때 전체적으로 이런 순서로 진행됩니다. 각 단계의 자세한 명령어는 아래 "사용 방법"과 [AGENTS.md](AGENTS.md)를 참고하세요.

```
작업 시작
   ↓
main 최신화                          ← git fetch + origin/main 기준으로 브랜치 생성
   ↓
<GitHub아이디>/<작업이름> 브랜치 생성    ← "내 브랜치 연결하기"
   ↓
자기 projects/<아이디>/ 폴더 위주로 수정  ← "내 작업 공유하기"
   ↓
handoff 작성
   ↓
push
   ↓
PR 생성                              ← pull_request_template.md 양식이 자동으로 채워짐
   ↓
GitHub 자동 검사                      ← folder-ownership-check · secret-scan · repo-rules-check
   ↓
리뷰 또는 본인 최종 확인                ← CODEOWNERS로 알림은 가지만 승인은 필수 아님
   ↓
main merge                           ← 위 검사 3개를 통과해야 merge 가능
   ↓
작업 브랜치 삭제                       ← 자동 (Automatically delete head branches)
```

## 사용 방법 (전원 공통)

자기 AI 코딩 에이전트(Claude Code·Codex·Cursor 등 무엇이든)에게 아래처럼 한 줄만 시키세요. 이 저장소의 [AGENTS.md](AGENTS.md)에 자세한 절차가 적혀 있어서, 그 파일을 읽을 줄 아는 에이전트라면 알아서 따라합니다.

<img src="https://img.shields.io/badge/%ED%8C%80%EC%9B%90%20%EC%9E%91%EC%97%85%20%EA%B3%B5%EC%9C%A0%20%EB%B0%9B%EA%B8%B0-yellow?style=for-the-badge" alt="팀원 작업 공유 받기" height="34">

> 처음 받을 때나, 나중에 다시 동기화할 때나 똑같이 (오른쪽 아래 복사 아이콘 클릭)
>
> ```text
> 이 저장소를 clone 받고 AGENTS.md 안내를 따라서, handoffs/ 안의 문서들을 요약해서 보여줘: https://github.com/trbb82349/bai-shared.git
> ```

직접 명령어: `git clone https://github.com/trbb82349/bai-shared.git` (처음) / `git pull` (이미 받은 경우)

이미 한 번 받아본 적 있으면, AI가 알아서 **지난번 이후 새로 올라온 핸드오프 문서와 업데이트된 프로젝트만** 찾아서 알려줍니다 (이미 봤던 내용을 매번 다시 읽거나 설명하지 않음).

<img src="https://img.shields.io/badge/%ED%8A%B9%EC%A0%95%20%ED%8C%80%EC%9B%90%20%EC%9E%91%EC%97%85%EB%A7%8C%20%EB%B0%9B%EA%B8%B0-yellow?style=for-the-badge" alt="특정 팀원 작업만 받기" height="34">

> 전체 말고 특정 팀원 작업만 받고 싶을 때 (오른쪽 아래 복사 아이콘 클릭)
>
> ```text
> bai-shared 저장소의 AGENTS.md를 읽고, sparse-checkout으로 특정 팀원 작업만 골라서 받아줘. 작업을 받고 싶은 사람은 (여기에 팀원 이름)야.
> ```

직접 명령어: `git clone --filter=blob:none --sparse https://github.com/trbb82349/bai-shared.git && cd bai-shared && git sparse-checkout set handoffs projects/<팀원GitHub아이디>`

<img src="https://img.shields.io/badge/%EB%82%B4%20%EC%9E%91%EC%97%85%20%EA%B3%B5%EC%9C%A0%ED%95%98%EA%B8%B0-orange?style=for-the-badge" alt="내 작업 공유하기" height="34">

> 내 작업을 main에 PR로 올릴 때 (merge는 이후 직접 결정) (오른쪽 아래 복사 아이콘 클릭)
>
> ```text
> bai-shared 저장소의 AGENTS.md를 읽고, 지금 이 프로젝트를 내 이름에 해당하는 GitHub 아이디 폴더 아래에 올리고 핸드오프 문서도 같이 써서 작업 브랜치에 push하고 main으로 PR을 열어줘. 나는 (여기에 이름)이야.
> ```

직접 명령어: `git add . && git commit -m "메시지" && git push -u origin <내GitHub아이디>/<작업이름> && gh pr create --base main --head <내GitHub아이디>/<작업이름>` (프로젝트 폴더 복사·핸드오프 문서 작성은 별도)

**왜 브랜치를 쓰나요?** `main`에 바로 push하지 않고 브랜치에서 작업한 뒤 PR을 열면, merge하기 전에 변경사항을 한눈에 확인할 수 있고 다른 사람 작업과 우연히 충돌할 일이 줄어듭니다. **브랜치는 사람이 아니라 작업 단위입니다** — 이름 형식은 `<GitHub아이디>/<작업이름>` (예: `trbb82349/careerlens-update`, `chldbfk/project-a`). 같은 사람이 여러 작업을 동시에 진행해도 브랜치가 안 겹치고, PR이 merge되면 그 브랜치는 자동으로 삭제됩니다. **PR을 언제 merge할지는 본인이 정하면 됩니다** — "내 작업 공유하기"는 PR을 여는 것까지만 하고, merge는 자동으로 실행되지 않습니다.

**`main`은 보호되어 있습니다.** 이제 `main`에 직접 push할 수 없고, 항상 PR을 통해야 합니다. PR을 열면 자동으로 세 가지를 검사합니다.
- **폴더 소유권 검사**: PR 브랜치의 앞부분(`<GitHub아이디>/...`)과 다른 사람의 `projects/<아이디>/` 폴더를 건드리면 실패합니다.
- **민감정보 스캔**: API 키, 비밀번호 같은 게 실수로 섞였는지 확인합니다.
- **저장소 규칙 검사**: `.env` 등 민감 파일 이름이 그대로 커밋됐는지, `projects/<아이디>/<프로젝트명>/` 구조를 지켰는지, 새로 추가되는 프로젝트에 README.md가 있는지 확인합니다.

리뷰 승인은 필수가 아니라서, 위 세 검사만 통과하면 본인이 바로 merge할 수 있습니다.

<img src="https://img.shields.io/badge/%EB%82%B4%20%EB%B8%8C%EB%9E%9C%EC%B9%98%20%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0-blue?style=for-the-badge" alt="내 브랜치 연결하기" height="34">

> 파일을 올리기 전에, 작업을 시작하면서 미리 작업 브랜치로 연결해두고 싶을 때 (오른쪽 아래 복사 아이콘 클릭)
>
> ```text
> bai-shared 저장소를 clone 받고, 이번 작업용 브랜치로 전환(없으면 새로 만들어)해줘. 나는 (여기에 이름)이고, 이번 작업은 (여기에 작업 내용)이야.
> ```

직접 명령어: `git fetch origin && git switch <내GitHub아이디>/<작업이름>` (없으면 `git switch -c <내GitHub아이디>/<작업이름> origin/main`)

> 이 단계는 선택 사항입니다 — 안 해도 위 "내 작업 공유하기"를 실행하면 알아서 본인 브랜치로 전환됩니다.

## 받은 내용은 어디에 저장되나요

"공유 받기"·"특정 팀원만 받기"는 기본적으로 **AI 세션의 임시 폴더(해당 AI 대화창)**에만 clone됩니다. 내 컴퓨터에 계속 남는 게 아니라서, 확인만 하고 끝낼 때는 이걸로 충분합니다.

이 내용을 내 컴퓨터에 계속 두고 쓰고 싶으면, "내 컴퓨터에 저장해줘"라고 따로 요청하세요. 그때 실제 폴더로 옮겨줍니다. (반대로 "내 작업 공유하기"는 처음부터 내가 계속 작업할 폴더이므로 바로 내 컴퓨터에 clone됩니다.)

## 원칙

- 핸드오프 문서에 원본 대화를 통째로 붙여넣지 않습니다. 노이즈가 많아서 상대방 AI가 핵심을 못 고릅니다. 반드시 템플릿 항목별로 걸러서 요약합니다.
- 프로젝트 폴더 안의 자세한 기록(README 등)은 그대로 두고, 핸드오프 문서는 그 위에 얹는 짧은 요약 레이어로 씁니다.
- 이 저장소는 public입니다. 개인정보·API 키·비밀번호는 절대 올리지 않습니다.

## 참여하기

쓰기 권한(협업자 등록)이 필요합니다. GitHub 아이디를 저장소 관리자(trbb82349)에게 알려주세요. 처음 "내 작업 공유하기"를 할 때 이름을 알려주면 [MEMBERS.md](MEMBERS.md)에 자동으로 등록됩니다.

## 예시

- [handoffs/template.md](handoffs/template.md) — 빈 템플릿
- [handoffs/2026-09-02-trbb82349-핸드오프.md](handoffs/2026-09-02-trbb82349-핸드오프.md) — 실제 프로젝트로 채운 작성 예시 (파일명 규칙을 따른 예시이기도 함)
- [projects/trbb82349/careerlens-mvp/](projects/trbb82349/careerlens-mvp/) — 그 예시가 가리키는 실제 프로젝트
