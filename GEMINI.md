# GEMINI.md: BizTone Converter

이 문서는 AI 어시스턴트가 'BizTone Converter' 프로젝트의 맥락을 이해하고 일관된 개발을 지원하기 위한 지침입니다.

## 1. 프로젝트 개요 (Project Overview)

**BizTone Converter**는 사용자의 일상적인 문장을 비즈니스 상황에 맞는 전문적인 말투로 변환해주는 AI 기반 웹 솔루션입니다. 사용자는 변환 대상을 '상사', '동료', '고객' 중에서 선택할 수 있으며, 각 대상에 최적화된 어투의 결과물을 얻을 수 있습니다.

-   **Frontend**: `HTML`, `Tailwind CSS`, `JavaScript (ES6+)`
-   **Backend**: `Python`, `Flask`
-   **AI**: `Groq AI API` (`moonshotai/kimi-k2-instruct-0905` 모델 사용)
-   **Architecture**: 정적 프론트엔드와 Flask 백엔드 API 서버가 분리된 구조입니다. 프론트엔드는 Vercel을 통해 호스팅되고, 백엔드는 서버리스 함수로 배포되는 것을 목표로 합니다.

## 2. 주요 파일 구조 (Key File Structure)

```
.
├── backend/
│   ├── app.py         # Flask 앱, API 엔드포인트 및 Groq 연동 로직
│   └── requirements.txt # Python 의존성 목록
├── frontend/
│   ├── index.html     # 메인 UI
│   ├── js/script.js   # API 호출 등 클라이언트 사이드 로직
│   └── css/
│       ├── input.css  # Tailwind CSS 지시문 소스
│       └── style.css  # 빌드된 최종 CSS 파일
├── PRD.md             # 제품 요구사항 명세서 (Product Requirements Document)
├── 프로그램 개요서.md   # 프로젝트 초기 기획 문서
└── .env               # (필수) API 키 등 환경 변수 저장
```

## 3. 빌드 및 실행 (Building and Running)

### 3.1. 백엔드 (Backend)

1.  **가상 환경 생성 및 활성화**:
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

2.  **의존성 설치**:
    ```bash
    pip install -r backend/requirements.txt
    ```

3.  **환경 변수 설정**:
    -   프로젝트 루트에 `.env` 파일을 생성하고 아래 내용을 추가하세요.
    -   `YOUR_API_KEY` 부분은 실제 Groq API 키로 교체해야 합니다.
    ```
    GROQ_API_KEY='YOUR_API_KEY'
    ```

4.  **로컬 서버 실행**:
    ```bash
    python backend/app.py
    ```
    -   서버는 `http://127.0.0.1:5000` 에서 실행됩니다.

### 3.2. 프론트엔드 (Frontend)

프론트엔드는 백엔드 Flask 서버에 의해 정적 파일로 제공되므로 별도의 실행 과정이 필요 없습니다. `http://127.0.0.1:5000`에 접속하면 바로 확인할 수 있습니다.

-   **CSS 스타일 변경 시**:
    -   `frontend/css/input.css` 또는 `frontend/tailwind.config.js` 파일을 수정한 후, 아래 명령어로 `style.css`를 다시 빌드해야 합니다.
    ```bash
    # frontend 디렉토리에서 실행
    cd frontend
    npm install # 최초 1회 실행
    npm run build
    ```

## 4. 개발 컨벤션 (Development Conventions)

-   **API Endpoint**: 백엔드는 `/api/convert` 엔드포인트를 통해 말투 변환 기능을 제공합니다.
-   **민감 정보**: `GROQ_API_KEY`와 같은 모든 민감 정보는 `.env` 파일을 통해 관리하며, 절대로 코드에 하드코딩하지 않습니다.
-   **스타일링**: 프론트엔드 스타일링은 `Tailwind CSS`를 사용합니다. `frontend/css/input.css`가 원본 소스이며, 직접 `style.css`를 수정하지 않습니다.
-   **브랜치 전략**: `feature -> develop -> main` 브랜치 전략 사용을 목표로 합니다. (PRD 기반)
-   **언어**: 코드 주석, 변수명 등은 영어를 기본으로 사용하되, 문서 및 사용자 인터페이스는 한국어를 사용합니다.

