# BAI 작업 공유 저장소 안내

이 문서는 BAI 팀원이 `trbb82349/bai-shared` 저장소의 목적, 사용 흐름, 기존 문서를 빠르게 파악하도록 돕습니다. 이 저장소에는 AI 에이전트(Claude Code, Codex, Cursor 등)가 만든 프로젝트와 세션 간 맥락을 전달하는 핸드오프가 함께 올라갑니다.

## 저장소에서 공유하는 것

```text
bai-shared/
├── handoffs/                      세션이 끝날 때 남기는 짧은 진행 요약
├── projects/<GitHub아이디>/<프로젝트>/ 실제 프로젝트 코드·데이터·문서
├── .github/pull_request_template.md PR 작성 항목과 체크리스트
├── AGENTS.md                      에이전트 공통 절차
├── CLAUDE.md                      Claude Code가 AGENTS.md를 불러오는 연결 파일
├── MEMBERS.md                     이름과 GitHub 아이디 대응표
└── README.md                      사람이 보는 저장소 안내
```

프로젝트는 GitHub 아이디별로 나뉘어 작성자를 찾기 쉽습니다. 팀원이 함께 만드는 프로젝트의 소유 폴더나 공동 작업 구조는 참여자끼리 먼저 정하고, 개인 폴더를 임의로 서로 대신 수정하지 않습니다. 이름과 아이디는 `MEMBERS.md`에서 확인합니다.

## 작업하고 공유하는 순서

```text
작업 범위 정하기 (큰 일은 Issue로 기록)
       ↓
최신 main에서 <GitHub아이디>/<작업이름> 브랜치 시작
       ↓
자기 projects/<아이디>/<프로젝트>/ 폴더에서 작업
       ↓
프로젝트 README·관련 기록 갱신, 필요한 경우 핸드오프 작성
       ↓
변경 파일·비밀정보·실행 결과 점검
       ↓
작업 브랜치에 commit + push, main 대상 PR 열기
       ↓
자동 검사 통과 + 작성자가 아닌 팀원의 실제 diff 검토
       ↓
사람이 승인하고 병합, 작업 브랜치 정리
```

- 브랜치 이름은 `<GitHub아이디>/<영어-kebab-case-작업명>` 형식입니다. 예: `trbb82349/careerlens-update`.
- 에이전트는 요청된 작업 브랜치에 commit하고 push한 뒤 PR을 열 수 있습니다. `main`에 직접 push하지 않고, PR도 병합하지 않습니다.
- 사람이 변경 파일과 이유, 실행·검증 결과, 데이터·개인정보 영향을 살펴본 뒤 병합합니다. 작성자는 자기 PR을 승인하지 않습니다.
- 사용자는 에이전트에게 작업을 요청할 때 저장소의 `AGENTS.md`와 해당 프로젝트 문서도 읽고 따르도록 안내할 수 있습니다. Claude Code는 `CLAUDE.md`가 `AGENTS.md`를 가져오도록 되어 있습니다.

## PR과 자동 검사

`.github/pull_request_template.md`는 다음 내용을 요구합니다.

- 프로젝트 경로
- 변경 내용과 이유
- 실행 방법 및 테스트 결과 (직접 확인하지 않았다면 그 사실과 이유)
- 핸드오프 핵심 요약
- 본인 프로젝트 폴더만 변경했는지, 민감정보가 없는지, 실행 확인과 핸드오프를 했는지 체크

현재 저장소 README에 문서화된 자동 검사는 세 가지입니다.

- **folder-ownership-check**: 브랜치의 GitHub 아이디와 다른 사람의 프로젝트 폴더를 함께 변경하지 않았는지 확인
- **secret-scan**: API 키·비밀번호처럼 보이는 값을 탐지
- **repo-rules-check**: 민감 파일명, 프로젝트 경로 구조, 새 프로젝트의 `README.md`를 확인

기존 저장소 안내에는 이 검사 통과가 병합 조건이고 CODEOWNERS는 알림용이며 승인 리뷰는 필수가 아니라고 적혀 있습니다. 팀의 운영 원칙은 **사람 리뷰 후 병합**이므로, 저장소 관리자는 가능하면 `main` 보호 설정에서도 사람 승인 1명 이상을 필수로 설정해야 합니다. 현재 설정을 직접 확인할 수 없는 내용은 레포 문서의 설명과 실제 GitHub 설정을 구분해 판단합니다.

병합 뒤 작업 브랜치가 자동 삭제되도록 설정할 수 있습니다. 이 설정을 켜지 않은 경우 병합 후 원격 작업 브랜치를 사람이 정리합니다.

## 안전 및 권한

- 참고 레포는 Public입니다. API 키, 토큰, 비밀번호, 실제 `.env`, 개인 식별 정보, 동의를 받지 않은 원자료를 올리지 않습니다.
- 필요한 설정값 이름만 `.env.example`에 기록하고 실제 값은 포함하지 않습니다.
- 공개된 비밀값이 발견되면 파일을 삭제하는 것만으로 충분하지 않습니다. 해당 키를 폐기·재발급하고 저장소 운영자에게 알려야 합니다.
- 쓰기 권한은 저장소 관리자가 GitHub 아이디를 collaborator로 초대해 부여합니다. 새 팀원은 이름과 GitHub 아이디를 관리자에게 전달하고 `MEMBERS.md`에도 등록합니다.
- 관리자 계정 접근을 잃지 않도록 초대·권한 회수와 복구를 맡을 운영 책임자를 정합니다.

## 동기화와 필요한 폴더만 받기

- 처음 저장소 내용을 확인만 할 때는 AI 세션의 임시 폴더에 clone하는 것이 기본입니다. 계속 작업할 폴더가 필요하면 그 목적에 맞는 위치에 clone합니다.
- 전체 업데이트는 저장소 안내에 따라 새 변경을 확인합니다. 보고했던 핸드오프와 프로젝트 내용을 매번 전부 다시 설명하지 않습니다.
- 특정 팀원 작업만 볼 때는 sparse-checkout을 사용할 수 있습니다. `handoffs/`와 `projects/<GitHub아이디>/`를 받으면 됩니다.
- sparse-checkout은 받은 파일 범위를 줄이는 기능이지, 다른 사람 폴더에 수정·push할 권한이 아닙니다.
- 구체적인 요청 문구와 명령은 저장소의 최신 `README.md` 및 `AGENTS.md`를 기준으로 합니다.

```bash
# 처음 clone
git clone https://github.com/trbb82349/bai-shared.git

# 팀원 한 명의 파일만 가져오기 (이름은 MEMBERS.md에서 아이디로 확인)
git clone --filter=blob:none --sparse https://github.com/trbb82349/bai-shared.git
cd bai-shared
git sparse-checkout set handoffs projects/<GitHub아이디>

# 이후 업데이트
git pull
```

조회만 할 clone은 임시 폴더에 두고 세션이 끝나면 계속 보관하지 않는 것이 기본입니다. 지속적으로 작업할 목적이라면 작업 폴더에 clone합니다.

## 에이전트에게 바로 요청하기

아래 문구에서 괄호 부분을 채워 사용하시면 됩니다. 에이전트가 저장소 규칙을 알아서 찾지 못하는 경우 `AGENTS.md`를 명시해 주세요.

**처음 받아오거나 전체 변경 확인하기**

```text
이 저장소를 clone 받고 AGENTS.md 안내를 따라서, handoffs/ 안의 문서들을 요약해서 보여줘: https://github.com/trbb82349/bai-shared.git
```

**특정 팀원 작업만 보기**

```text
bai-shared 저장소의 AGENTS.md를 읽고, sparse-checkout으로 특정 팀원 작업만 골라서 받아줘. 작업을 받고 싶은 사람은 (팀원 이름)야.
```

**새 작업 브랜치를 미리 연결하기**

```text
bai-shared 저장소를 clone 받고, 이번 작업용 브랜치로 전환(없으면 새로 만들어)해줘. 나는 (이름)이고, 이번 작업은 (작업 내용)이야.
```

**내 프로젝트를 공유하고 PR 열기**

```text
bai-shared 저장소의 AGENTS.md를 읽고, 지금 이 프로젝트를 내 이름에 해당하는 GitHub 아이디 폴더 아래에 올리고 핸드오프 문서도 같이 써서 작업 브랜치에 commit·push하고 main으로 PR을 열어줘. 나는 (이름)이야.
```

개별 단계의 직접 명령과 안전 조건은 저장소 `AGENTS.md`에 둡니다. PR을 연 뒤 사람 리뷰와 승인, 병합은 팀원이 맡습니다.

## 핸드오프 작성 기준

`handoffs/template.md`의 항목은 다음과 같습니다.

1. 기본 정보: 작성자, 날짜, 프로젝트/담당 파트
2. 목표
3. 한 일과 결정한 것 (결정 이유 포함 가능)
4. 저장소 안 결과물 위치
5. 막힌 것/미해결 질문
6. 다음 할 일
7. 다른 파트와의 연결점

핸드오프는 상세 프로젝트 README와 기록을 대신하지 않는 짧은 요약입니다. 대화 전문은 넣지 않습니다. 같은 프로젝트의 이전 핸드오프가 있으면 이전 “다음 할 일”과 이번에 처리한 일을 이어 적습니다. 샘플 핸드오프는 이 구조를 CareerLens MVP에 적용한 예시입니다.

## 저장소에 있는 Markdown 문서 전체 목록

아래 목록은 현재 원격 `main`에서 확인한 Markdown 파일을 모두 담습니다. 새 Markdown을 추가·삭제할 때 이 목록과 설명도 함께 갱신합니다.

| 파일 | 무엇을 담고 있나요? |
|---|---|
| [`README.md`](https://github.com/trbb82349/bai-shared/blob/main/README.md) | 저장소 구조, 작업 브랜치와 PR 흐름, 동기화/부분 체크아웃 예시, 공개 저장소 보안 원칙, 참여 방법 |
| [`AGENTS.md`](https://github.com/trbb82349/bai-shared/blob/main/AGENTS.md) | 에이전트의 임시/영구 clone 판단, 전체·부분 동기화, 팀원 아이디 확인, 작업 브랜치, 프로젝트 복사·갱신, 핸드오프 작성, commit/push/PR, CI 실패 대응 절차 |
| [`CLAUDE.md`](https://github.com/trbb82349/bai-shared/blob/main/CLAUDE.md) | Claude Code가 `AGENTS.md`를 import해 같은 규칙을 따르도록 하는 연결 파일 |
| [`MEMBERS.md`](https://github.com/trbb82349/bai-shared/blob/main/MEMBERS.md) | 팀원 이름과 GitHub 아이디의 대응. 신규 팀원 확인·등록 절차 및 일부 아이디/초대 상태의 메모가 있으므로 실제 참여 전 최신 여부 확인. 현재 문서에는 7명만 적혀 있으므로, 10명 모두를 초대하기 전에 나머지 팀원의 이름·아이디도 확인해 등록 |
| [`.github/pull_request_template.md`](https://github.com/trbb82349/bai-shared/blob/main/.github/pull_request_template.md) | 프로젝트 경로, 변경 내용, 테스트, 핸드오프 요약, 소유 폴더·보안·검증 체크리스트 |
| [`handoffs/template.md`](https://github.com/trbb82349/bai-shared/blob/main/handoffs/template.md) | 핸드오프 7개 항목을 위한 빈 양식 |
| [`handoffs/2026-09-02-trbb82349-핸드오프.md`](https://github.com/trbb82349/bai-shared/blob/main/handoffs/2026-09-02-trbb82349-핸드오프.md) | CareerLens의 목표·결정·결과물·미해결 과제·다음 작업·연결점을 기록한 작성 예시. 카드/버전 배경과 당시의 미해결 threshold·데이터 희소성도 설명 |
| [`projects/trbb82349/careerlens-mvp/README.md`](https://github.com/trbb82349/bai-shared/blob/main/projects/trbb82349/careerlens-mvp/README.md) | CareerLens 전체 진행 기록, 채용공고 수집 제약, v1~v4 결정 이력, 현재 파일 구조, 알려진 한계와 할 일 |
| [`notes/도메인-분류-기준-2026-09-02.md`](https://github.com/trbb82349/bai-shared/blob/main/projects/trbb82349/careerlens-mvp/notes/%EB%8F%84%EB%A9%94%EC%9D%B8-%EB%B6%84%EB%A5%98-%EA%B8%B0%EC%A4%80-2026-09-02.md) | 직무 카테고리 대신 산업 도메인을 택한 이유, 점진적 바텀업 분류 원칙, 9개 도메인과 회사 배정, 74개에서 77개 카드로 바뀐 근거, 남은 표본 한계 |
| [`notes/2026-09-11-프로그램-구성-설명.md`](https://github.com/trbb82349/bai-shared/blob/main/projects/trbb82349/careerlens-mvp/notes/2026-09-11-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EA%B5%AC%EC%84%B1-%EC%84%A4%EB%AA%85.md) | 비전공자 인수인계 설명: 실행 방법, 데이터와 도메인, 모델과 코드의 역할, 코사인 유사도·군집화·추천 기준, 화면 근거, 구조와 한계 |
| [`notes/2026-09-11-코드-재사용-가이드.md`](https://github.com/trbb82349/bai-shared/blob/main/projects/trbb82349/careerlens-mvp/notes/2026-09-11-%EC%BD%94%EB%93%9C-%EC%9E%AC%EC%82%AC%EC%9A%A9-%EA%B0%80%EC%9D%B4%EB%93%9C.md) | v4 JavaScript 함수를 재사용할 때 순수 로직과 DOM/UI 코드를 구분하는 법, 호출 순서, 데이터 구조, 상태와 통합 체크리스트 |
| [`notes/2026-09-11-알고리즘-스펙-재구현용.md`](https://github.com/trbb82349/bai-shared/blob/main/projects/trbb82349/careerlens-mvp/notes/2026-09-11-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%8A%A4%ED%8E%99-%EC%9E%AC%EA%B5%AC%ED%98%84%EC%9A%A9.md) | 다른 언어·스택에서 v4를 재구현하기 위한 입력 구조, 임베딩, 코사인, 완전 연결 군집화, 도메인 통합·선택 비율·주요 추천 단계, 상수와 픽스처 검증 |

### CareerLens 예시의 핵심

CareerLens MVP는 사용자가 업무카드를 선택하면 유사한 카드를 묶어 산업 도메인 추천과 근거를 보여주는 브라우저 프로토타입입니다. 채용공고 18건(당시 모두 원티드, 16개 회사)을 바탕으로 업무카드를 만들었고, 현재 문서 기준 데이터는 77개 카드와 9개 산업 도메인입니다.

기록된 v1~v4는 서로 다른 실험입니다. v1은 키워드 자카드와 같은 분야 보너스, v2는 공고 공동출현과 Sentence-BERT, v3는 코사인 유사도 단독, v4는 v3 계산을 유지하며 데이터를 산업 도메인 카드로 바꿨습니다. v4의 기준 구현은 `src/careerlens-mvp-4.html`이고, v1~v3는 비교용으로 보존합니다.

v4 상세 노트의 설계 핵심은 정규화하지 않은 코사인 유사도 원값, `MERGE_THRESHOLD=0.5`, 완전 연결(complete-linkage), 같은 대표 도메인 하위 그룹의 화면상 통합, 도메인별 카드 수 편차를 보정하는 선택 비율입니다. “주요 추천”은 카드 2개 이상이고 가장 높은 선택 비율의 50% 이상인 그룹으로 설명되어 있습니다. 추천 근거는 그룹의 대표 도메인·평균 유사도·혼합 도메인 간 실제 카드 쌍·가장 약한 연결고리를 제시하며, 임베딩 모델이 의미 설명을 직접 생성한다고 과장하지 않습니다.

문서 기록상 v4는 HTTP 로컬 서버에서 모델 로딩·화면·추천·설명 탭을 Playwright로 카드 조합 1건 확인했습니다. `MERGE_THRESHOLD=0.5`가 다양한 카드 조합에 적절한지는 아직 재검증 과제로 남아 있습니다. 도메인별 공고 수가 적고 모두 원티드 자료인 점도 한계입니다. 새로운 실험 전에 프로젝트 README와 관련 노트를 다시 확인하세요.

## 문서 유지 원칙

- 저장소의 `AGENTS.md`, `README.md`, PR 템플릿이 서로 다른 절차를 말하지 않게 함께 갱신합니다.
- Claude Code 연결 파일은 공통 규칙을 중복 복사하지 않고 `AGENTS.md`를 가져옵니다.
- 프로젝트별 사양과 결정은 해당 프로젝트 README/notes에 두고, 이 README에는 길 찾기와 요약을 둡니다.
- 새 Markdown 파일이 생기면 위 목록에 경로와 용도를 추가합니다. 파일을 옮기거나 지우면 링크도 확인합니다.
- 저장소가 Public인 상태를 전제로 비밀값·개인정보·공유 동의가 없는 원자료를 문서와 예시에도 넣지 않습니다.
