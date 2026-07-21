# BugBox 프로젝트 개발노트

> **A Personal Debugging Memory System Powered by Computer Vision and AI**  
> 오류 화면을 읽고, 과거의 해결 경험을 기억하며, 다음 디버깅을 돕는 개인 AI 오류 관리 시스템

## 한 줄 소개

오류 스크린샷이나 로그를 등록하면 컴퓨터 비전과 OCR을 이용해 오류 내용을 추출하고, 과거에 발생한 유사 오류와 해결 기록을 검색한 뒤, 필요한 경우 LLM이 원인 후보와 확인 절차를 제시하는 개인용 디버깅 지식 시스템이다.

> **Turn every bug into reusable knowledge.**  
> 한 번 겪은 오류를 다시 사용할 수 있는 지식으로 만든다.

---

## 목차

1. [프로젝트 기본 정보](#1-프로젝트-기본-정보)
2. [프로젝트 배경](#2-프로젝트-배경)
3. [해결하고자 하는 문제](#3-해결하고자-하는-문제)
4. [프로젝트 목표](#4-프로젝트-목표)
5. [프로젝트 범위](#5-프로젝트-범위)
6. [전체 사용자 흐름](#6-전체-사용자-흐름)
7. [권장 기술 스택](#7-권장-기술-스택)
8. [권장 시스템 아키텍처](#8-권장-시스템-아키텍처)
9. [구현할 핵심 기능](#9-구현할-핵심-기능)
10. [주요 화면 구성](#10-주요-화면-구성)
11. [데이터베이스 설계 초안](#11-데이터베이스-설계-초안)
12. [FastAPI 엔드포인트 초안](#12-fastapi-엔드포인트-초안)
13. [권장 폴더 구조](#13-권장-폴더-구조)
14. [사전에 알아두어야 할 지식](#14-사전에-알아두어야-할-지식)
15. [이 프로젝트에서 얻을 수 있는 지식](#15-이-프로젝트에서-얻을-수-있는-지식)
16. [AI 분석기 교체 구조](#16-ai-분석기-교체-구조)
17. [평가 방법](#17-평가-방법)
18. [테스트 데이터 준비](#18-테스트-데이터-준비)
19. [한 달 개발 일정](#19-한-달-개발-일정)
20. [우선순위](#20-우선순위)
21. [프로젝트 성공 기준](#21-프로젝트-성공-기준)
22. [예상 문제와 대응 방법](#22-예상-문제와-대응-방법)
23. [응용 분야](#23-응용-분야)
24. [포트폴리오에서 강조할 점](#24-포트폴리오에서-강조할-점)
25. [README용 프로젝트 설명 초안](#25-readme용-프로젝트-설명-초안)
26. [개발 중 기록할 실험](#26-개발-중-기록할-실험)
27. [최종 프로젝트 정의](#27-최종-프로젝트-정의)

---

# 1. 프로젝트 기본 정보

## 프로젝트명

**BugBox**

## 영문 부제

**A Personal Debugging Memory System Powered by Computer Vision and AI**

## 국문 부제

**오류 화면을 읽고, 과거의 해결 경험을 기억하며, 다음 디버깅을 돕는 개인 AI 오류 관리 시스템**

## 프로젝트 성격

- 개인용 디버깅 기록 도구
- 오류 스크린샷 기반 컴퓨터 비전 프로젝트
- OCR 및 의미 기반 검색 프로젝트
- 선택적 LLM 연동 프로젝트
- 로컬 우선·개인정보 보호 중심 애플리케이션

---

# 2. 프로젝트 배경

개발 과정에서 같은 오류를 여러 번 마주치지만, 과거에 어떤 방법으로 해결했는지 기억하지 못하는 경우가 많다.

기존의 오류 해결 방식은 대체로 다음과 같다.

1. 오류 메시지를 검색한다.
2. 검색 결과나 AI 답변을 확인한다.
3. 여러 해결 방법을 시도한다.
4. 오류를 해결한다.
5. 해결 과정을 별도로 기록하지 않는다.
6. 몇 달 뒤 같은 오류가 발생하면 처음부터 다시 검색한다.

특히 초보 개발자는 오류 메시지의 어느 부분이 중요한지, 어떤 라이브러리에서 발생한 오류인지, 먼저 무엇을 확인해야 하는지 판단하기 어렵다.

BugBox는 오류를 단순히 AI에게 질문하는 서비스가 아니다. 오류와 해결 과정을 개인 데이터로 축적하여, 시간이 지날수록 사용자의 실제 개발 환경에 맞는 답을 더 잘 제공하는 것을 목표로 한다.

---

# 3. 해결하고자 하는 문제

## 3.1 오류 기록의 부재

오류를 해결해도 원인과 해결 방법을 기록하지 않아 동일한 시행착오를 반복한다.

## 3.2 오류 메시지 해석의 어려움

긴 스택 트레이스에는 파일 경로, 라이브러리 내부 호출, 실제 예외 메시지가 섞여 있다. 초보자는 어떤 줄이 핵심인지 구분하기 어렵다.

## 3.3 스크린샷 중심의 비구조화된 기록

오류 화면을 캡처해두더라도 사진첩이나 폴더에 묻혀 다시 찾기 어렵다. 이미지 안의 오류 문구도 일반 파일 검색으로는 찾을 수 없다.

## 3.4 일반적인 AI 답변의 한계

LLM은 일반적인 해결책을 제시할 수 있지만, 사용자가 과거에 실제로 성공했던 해결 방법이나 당시의 개발 환경까지 기억하지는 못한다.

## 3.5 민감정보 노출 가능성

오류 로그와 스크린샷에는 다음과 같은 정보가 포함될 수 있다.

- API 키
- 사용자 이름
- 로컬 파일 경로
- 데이터베이스 주소
- 비공개 프로젝트 코드
- 이메일 주소
- 토큰과 비밀번호

이를 그대로 외부 AI 서비스에 전송하면 개인정보와 보안 문제가 발생할 수 있다.

---

# 4. 프로젝트 목표

## 4.1 핵심 목표

1. 오류 스크린샷을 로컬에서 분석하여 텍스트를 추출한다.
2. 오류 메시지를 구조화하고 핵심 정보를 분리한다.
3. 동일하거나 유사한 과거 오류를 검색한다.
4. 사용자가 시도한 해결 방법과 성공 여부를 기록한다.
5. 민감정보를 제거한 뒤에만 Groq API를 선택적으로 호출한다.
6. LLM은 정답을 단정하기보다 원인 후보와 확인 절차를 제시한다.
7. 기록이 누적될수록 사용자의 과거 해결 경험을 우선적으로 추천한다.

## 4.2 학습 목표

이 프로젝트를 통해 다음 영역을 함께 공부한다.

- 컴퓨터 비전
- OCR
- 이미지 전처리
- REST API
- 프론트엔드와 백엔드 통신
- 데이터베이스
- 정규표현식과 문자열 파싱
- 텍스트 임베딩
- 의미 기반 검색
- LLM API 활용
- 프롬프트 설계
- 구조화된 출력
- 개인정보 마스킹
- 소프트웨어 아키텍처
- 테스트와 평가

---

# 5. 프로젝트 범위

## 5.1 지원 입력

초기 버전에서는 다음 입력을 지원한다.

- PNG, JPG, JPEG 형식의 오류 스크린샷
- 사용자가 직접 붙여 넣은 오류 로그
- 오류와 관련된 짧은 코드 조각
- 사용자가 직접 입력한 개발 환경 정보
- 사용자가 작성한 해결 과정과 최종 해결 방법

## 5.2 초기 지원 대상

처음부터 모든 프로그래밍 언어와 IDE를 지원하지 않는다.

1차 버전에서는 다음을 우선 지원한다.

- Python
- JavaScript 또는 TypeScript
- React
- FastAPI
- pandas
- NumPy
- Node.js
- 일반적인 터미널 및 브라우저 콘솔 오류

주로 사용자가 실제 프로젝트에서 마주치는 오류를 중심으로 확장한다.

## 5.3 지원하지 않을 기능

한 달 개발 범위에서는 다음 기능을 제외한다.

- 전체 저장소 자동 분석
- 코드를 자동으로 수정하는 에이전트
- 사용자의 코드를 서버에서 직접 실행하는 기능
- VS Code 확장 프로그램
- 다중 사용자 계정
- 클라우드 동기화
- 오류 팝업 객체 탐지 모델 직접 학습
- 패키지 의존성 문제의 완전 자동 해결
- LLM이 생성한 코드의 자동 실행
- 원본 스크린샷을 외부 AI API로 전송하는 기능

---

# 6. 전체 사용자 흐름

```text
오류 발생
   ↓
스크린샷 또는 로그 등록
   ↓
이미지 전처리
   ↓
OCR을 이용한 텍스트 추출
   ↓
사용자가 OCR 결과 확인·수정
   ↓
민감정보 자동 탐지 및 마스킹
   ↓
오류 메시지 구조화
   ↓
오류 지문 생성
   ↓
과거 유사 오류 검색
   ↓
기존 해결 기록이 있으면 우선 제공
   ↓
필요한 경우 Groq AI 분석 실행
   ↓
원인 후보와 디버깅 순서 확인
   ↓
해결 방법 시도
   ↓
성공·실패·부분 성공 결과 기록
   ↓
다음 유사 오류 검색에 반영
```

핵심은 AI 답변으로 끝나는 것이 아니라, **실제 해결 결과가 다시 BugBox의 데이터로 돌아오는 순환 구조**다.

---

# 7. 권장 기술 스택

## 7.1 프론트엔드

### React

사용자가 스크린샷을 업로드하고, OCR 결과를 수정하고, 유사 오류와 AI 분석 결과를 확인하는 인터페이스를 구현한다.

주요 학습 요소:

- 컴포넌트 분리
- Props
- State
- Hook
- 이벤트 처리
- API 호출
- 이미지 미리보기
- 다단계 폼
- 로딩 및 오류 상태

### Vite

React 프로젝트 생성과 로컬 개발 서버 실행에 사용한다.

### 추가 후보

- TypeScript
- React Router
- Axios 또는 Fetch API
- Zustand 또는 Context API
- Tailwind CSS 또는 CSS Modules

초기에는 상태관리 라이브러리를 반드시 도입할 필요는 없다. 화면 간 공유 상태가 복잡해질 때 추가한다.

---

## 7.2 백엔드

### Python

컴퓨터 비전, OCR, 임베딩 모델, 데이터 처리 생태계를 활용하기 위해 백엔드는 Python을 사용한다.

### FastAPI

React에서 보낸 이미지와 텍스트를 받아 다음 처리를 수행하는 API 서버로 사용한다.

- 컴퓨터 비전 전처리
- OCR
- 오류 파싱
- 개인정보 마스킹
- 유사 오류 검색
- Groq API 호출
- SQLite 데이터 저장

FastAPI는 Python 타입 힌트를 기반으로 API를 만들고, OpenAPI 기반 자동 문서와 Swagger UI를 제공한다. 개발 중 `/docs`에서 각 API를 직접 호출할 수 있다.

### Pydantic

API 요청과 응답 데이터의 형식을 정의하고 검증한다.

```python
from pydantic import BaseModel


class CauseCandidate(BaseModel):
    cause: str
    confidence: float | None
    how_to_check: str


class AIAnalysisResult(BaseModel):
    summary: str
    probable_causes: list[CauseCandidate]
    debug_steps: list[str]
    warnings: list[str]
```

---

## 7.3 컴퓨터 비전

### OpenCV

오류 스크린샷을 OCR에 적합한 이미지로 변환하는 데 사용한다.

주요 활용 기능:

- 이미지 크기 조정
- 그레이스케일 변환
- 대비 향상
- 노이즈 제거
- 선명화
- 색상 반전
- 이진화
- 적응형 임계값 처리
- 모폴로지 연산
- 윤곽선 검출
- 관심 영역 자르기
- OCR 결과 박스 시각화

---

## 7.4 OCR

### PaddleOCR

스크린샷 안의 터미널 로그, 팝업 문구, 파일명, 줄 번호 등을 텍스트로 변환한다.

OCR 결과에는 다음 정보가 포함되어야 한다.

- 인식한 텍스트
- 텍스트의 좌표
- 인식 신뢰도
- 줄 단위 정렬 결과
- 사용된 전처리 방식

OCR은 완벽하지 않으므로 사용자가 결과를 직접 수정할 수 있는 인터페이스가 필수다.

---

## 7.5 데이터베이스

### SQLite

오류 기록, 해결 과정, 태그, OCR 결과, AI 분석 결과를 로컬에 저장한다.

SQLite의 장점:

- 별도의 데이터베이스 서버가 필요 없음
- 하나의 파일로 데이터베이스 관리 가능
- 개인용 로컬 애플리케이션에 적합
- 설치와 배포가 단순함

### ORM 후보

- SQLAlchemy
- SQLModel

FastAPI와 함께 사용하기 편한 SQLModel을 우선 검토할 수 있다. ORM을 배우는 부담이 크다면 초기에는 Python 기본 `sqlite3`로 시작해도 된다.

---

## 7.6 임베딩과 유사 오류 검색

### Sentence Transformers

오류 메시지를 의미를 나타내는 숫자 벡터로 변환한다.

의미 기반 검색은 정확히 같은 단어가 없어도 뜻이 비슷한 기록을 찾는 방식이다.

```text
KeyError: 'region_name'
Column 'region_name' not found
Cannot find requested column region_name
```

위 문장들은 표현은 다르지만 유사한 오류로 검색될 수 있다.

### 초기 검색 방식

1. 모든 오류 기록의 임베딩 생성
2. 현재 오류의 임베딩 생성
3. 코사인 유사도 계산
4. 유사도가 높은 순서대로 정렬

### 확장 검색 방식

기록이 많아지면 다음을 검토한다.

- FAISS
- 벡터 데이터베이스
- Cross-Encoder 재정렬
- 키워드 검색과 벡터 검색 결합

---

## 7.7 LLM API

### Groq API

민감정보가 제거된 오류 텍스트를 분석하는 데 선택적으로 사용한다.

권장 역할 분리:

- `llama-3.1-8b-instant`
  - 짧은 요약
  - 오류 분류
  - 태그 생성
  - 간단한 JSON 구조화
- `openai/gpt-oss-120b`
  - 사용자가 요청한 정밀 원인 분석
  - 원인 후보 생성
  - 확인 절차 및 검증 방법 제시

제공 모델과 무료 한도는 변경될 수 있으므로 모델 ID를 코드에 직접 고정하지 않고 환경변수로 관리한다.

```env
GROQ_API_KEY=사용자_API_키
GROQ_QUICK_MODEL=llama-3.1-8b-instant
GROQ_DEEP_MODEL=openai/gpt-oss-120b
```

---

# 8. 권장 시스템 아키텍처

```text
┌─────────────────────────────┐
│        React Client         │
│                             │
│ 이미지 업로드               │
│ OCR 결과 수정               │
│ 마스킹 결과 확인            │
│ 유사 오류 조회              │
│ 해결 과정 기록              │
└──────────────┬──────────────┘
               │ HTTP / JSON
               ▼
┌─────────────────────────────┐
│        FastAPI Server       │
│                             │
│ Upload API                  │
│ OCR API                     │
│ Error Parser                │
│ Privacy Masker              │
│ Similarity Search           │
│ Groq Client                 │
└───────┬────────┬────────────┘
        │        │
        ▼        ▼
┌────────────┐  ┌─────────────┐
│ Local AI   │  │ Groq API    │
│            │  │             │
│ OpenCV     │  │ 오류 요약   │
│ PaddleOCR  │  │ 원인 추론   │
│ Embedding  │  │ 확인 절차   │
└──────┬─────┘  └─────────────┘
       │
       ▼
┌─────────────────────────────┐
│       SQLite Database       │
│                             │
│ 오류 기록                   │
│ OCR 결과                    │
│ 임베딩                      │
│ 해결 시도                   │
│ AI 분석 결과                │
└─────────────────────────────┘
```

---

# 9. 구현할 핵심 기능

## 기능 1. 오류 입력 및 등록

사용자는 오류를 다음 방식으로 등록할 수 있다.

- 오류 스크린샷 업로드
- 오류 로그 직접 붙여넣기
- 관련 코드 조각 입력
- 프로그래밍 언어 선택
- 사용 중인 프레임워크와 라이브러리 입력
- 오류가 발생한 상황 메모

### 구현 포인트

- 드래그 앤 드롭 이미지 업로드
- 이미지 형식과 용량 검증
- 업로드 이미지 미리보기
- 원본 이미지 로컬 저장
- 동일 이미지 중복 등록 방지
- 오류 로그만으로도 등록 가능

### 공부할 내용

- HTML 파일 입력
- `multipart/form-data`
- FastAPI의 `UploadFile`
- 프론트엔드와 백엔드 간 파일 전송
- 파일명 충돌 방지
- UUID 기반 파일명 생성

---

## 기능 2. 이미지 전처리 및 OCR

업로드된 이미지에서 오류 텍스트를 추출한다.

하나의 전처리 방식만 적용하지 않고 여러 후보 이미지를 생성한다.

```text
원본
├─ 2배 확대
├─ 그레이스케일
├─ 대비 강화
├─ 선명화
├─ 적응형 이진화
└─ 색상 반전
```

각 이미지에 OCR을 적용한 뒤 다음 기준으로 가장 좋은 결과를 선택한다.

- 평균 OCR 신뢰도
- 인식된 문자 수
- 오류 키워드 포함 여부
- 줄 구조 보존 여부
- 특수문자 보존 정도

### 주요 오류 키워드 예시

- `Error`
- `Exception`
- `Traceback`
- `Warning`
- `failed`
- `undefined`
- `null`
- `ModuleNotFound`
- `TypeError`
- `KeyError`
- `SyntaxError`

### 컴퓨터 비전 학습 포인트

#### 그레이스케일

RGB 색상 정보를 밝기 정보 중심으로 단순화한다.

#### 이진화

픽셀을 전경과 배경으로 나누어 문자와 배경의 구분을 명확하게 만든다.

#### 적응형 임계값

이미지 전체에 하나의 임계값을 사용하지 않고 주변 영역의 밝기에 따라 다른 임계값을 적용한다.

#### 모폴로지 연산

- 침식: 작은 잡음을 제거하거나 흰색 영역을 줄인다.
- 팽창: 끊어진 글자 영역을 연결하거나 흰색 영역을 넓힌다.
- 열림 연산: 작은 잡음을 제거한다.
- 닫힘 연산: 글자 내부나 선 사이의 작은 틈을 메운다.

#### 윤곽선 검출

터미널이나 팝업처럼 큰 직사각형 영역을 찾는 데 활용할 수 있다.

#### ROI

이미지 전체가 아닌 사용자가 선택한 오류 영역만 OCR에 전달하여 인식 정확도를 높인다.

### 화면에 보여줄 결과

- 원본 이미지
- 선택된 전처리 이미지
- OCR이 인식한 텍스트 박스
- 각 줄의 신뢰도
- 최종 추출 텍스트
- 사용자가 직접 수정할 수 있는 입력창

---

## 기능 3. OCR 결과 교정

OCR 결과를 그대로 신뢰하지 않고 사용자가 수정할 수 있게 한다.

특히 코드와 오류 로그에서는 다음 문자가 자주 혼동될 수 있다.

```text
O ↔ 0
I ↔ l ↔ 1
: ↔ ;
. ↔ ,
_ ↔ -
{ ↔ (
' ↔ "
```

### 후처리 기능

- 여러 공백을 하나로 정리
- 줄바꿈 복원
- 파일 경로 연결
- `Traceback` 구조 복원
- 깨진 특수문자 후보 표시
- 낮은 신뢰도의 OCR 줄 강조
- 원본 이미지와 텍스트를 함께 비교

### 중요한 설계 원칙

OCR 정확도가 낮더라도 프로젝트 전체가 실패해서는 안 된다. 사용자가 직접 교정한 텍스트를 이후 분석의 최종 입력으로 사용한다.

---

## 기능 4. 민감정보 탐지 및 마스킹

Groq API를 호출하기 전에 오류 로그와 코드에서 민감정보를 제거한다.

### 탐지 대상

- API 키
- Access Token
- GitHub Token
- 이메일 주소
- 전화번호
- IPv4 및 IPv6 주소
- 로컬 사용자 경로
- 데이터베이스 연결 문자열
- URL의 사용자 이름과 비밀번호
- `.env` 변수 값
- JWT 형식 문자열
- AWS 키 형식
- 비밀번호로 추정되는 값
- 사용자 지정 금지어

### 변환 예시

```text
/Users/myname/project/main.py
→ <USER_PATH>/project/main.py

C:\Users\myname\Desktop\app.js
→ <USER_PATH>\Desktop\app.js

myname@example.com
→ <EMAIL>

postgresql://admin:password@localhost/app
→ <DATABASE_URL>

ghp_abcdefghijklmnopqrstuvwxyz
→ <GITHUB_TOKEN>
```

### 구현 방법

- 정규표현식
- 접두어 패턴 사전
- 엔트로피 기반 임의 문자열 탐지
- 사용자 지정 마스킹 규칙
- 마스킹 전후 비교 화면
- 전송 예정 데이터 미리보기

### 안전 원칙

1. 원본 스크린샷은 Groq에 보내지 않는다.
2. OCR 결과에서 민감정보를 먼저 제거한다.
3. 사용자에게 실제 전송될 텍스트를 보여준다.
4. 사용자가 명시적으로 분석 버튼을 눌렀을 때만 전송한다.
5. API 키는 프론트엔드에 저장하지 않는다.
6. API 키는 백엔드 환경변수로만 관리한다.
7. `.env` 파일은 Git에 올리지 않는다.

---

## 기능 5. 오류 메시지 구조화

OCR 텍스트나 직접 입력한 로그에서 다음 정보를 추출한다.

```json
{
  "language": "python",
  "exception_type": "KeyError",
  "message": "'district_name'",
  "library": "pandas",
  "file_name": "analysis.py",
  "line_number": 127,
  "function_name": "preprocess_data",
  "environment": {
    "python": "3.11",
    "os": "macOS"
  }
}
```

### 구현 순서

#### 1단계: 규칙 기반 파싱

정규표현식과 문자열 규칙으로 정보를 추출한다.

Python 예시:

```text
File "analysis.py", line 127, in preprocess_data
KeyError: 'district_name'
```

JavaScript 예시:

```text
TypeError: Cannot read properties of undefined
at UserCard (UserCard.jsx:24:18)
```

#### 2단계: Groq 보조 구조화

규칙 기반 파서가 충분한 정보를 추출하지 못한 경우에만 작은 모델에 구조화를 요청한다.

LLM 결과는 반드시 JSON 형식으로 제한하고 Pydantic으로 검증한다.

### 공부할 내용

- 정규표현식
- Named capture group
- 언어별 스택 트레이스 구조
- Pydantic 검증
- JSON 파싱 오류 처리
- LLM 구조화 출력
- 규칙 기반 시스템과 생성형 AI의 결합

---

## 기능 6. 오류 지문 생성

같은 종류의 오류라도 파일명, 줄 번호, 변수명은 매번 달라질 수 있다.

```text
KeyError: 'district_name'
File "analysis.py", line 127
```

```text
KeyError: 'region_code'
File "preprocess.py", line 58
```

문자열 전체를 비교하면 다르지만 본질적으로는 비슷한 오류일 수 있다.

따라서 검색에 사용할 정규화된 오류 지문을 만든다.

```text
python|pandas|keyerror|missing-key
```

### 정규화 대상

- 절대 파일 경로
- 줄 번호
- 메모리 주소
- UUID
- 날짜와 시간
- 사용자 이름
- 임시 파일명
- 특정 변수명
- 포트 번호
- 요청 ID

### 지문 생성 방식

1. 프로그래밍 언어
2. 예외 클래스
3. 주요 라이브러리
4. 오류 카테고리
5. 정규화된 오류 메시지

### 활용

- 동일 오류 중복 등록 감지
- 같은 유형의 오류 그룹화
- 유사도 검색 점수 보정
- 오류 통계 생성
- 반복 오류 감지

---

## 기능 7. 과거 유사 오류 검색

현재 오류와 유사한 과거 기록을 검색한다.

### 검색 데이터

임베딩 생성에 사용할 문자열은 다음 정보를 결합한다.

```text
언어: Python
라이브러리: pandas
예외: KeyError
메시지: DataFrame에서 요청한 컬럼을 찾을 수 없음
상황: merge 이후 컬럼 접근
```

### 검색 점수 예시

```text
텍스트 임베딩 유사도      45%
오류 지문 일치도         25%
예외 클래스 일치         10%
언어·라이브러리 일치     10%
과거 해결 성공 여부       5%
최근 사용 여부            5%
```

각 가중치는 실험을 통해 조정한다.

### 검색 결과에 표시할 정보

- 유사도 점수
- 오류 제목
- 발생 날짜
- 언어와 라이브러리
- 당시 원인
- 성공한 해결 방법
- 실패한 해결 방법
- 현재 오류와 다른 점
- 해결까지 걸린 시간

### 중요한 우선순위

```text
1. 사용자가 과거에 성공한 해결 방법
2. 동일한 오류 지문을 가진 기록
3. 의미적으로 유사한 과거 기록
4. 규칙 기반 기본 안내
5. Groq의 새로운 분석
```

LLM의 일반적인 추론보다 사용자의 실제 성공 기록을 우선한다.

---

## 기능 8. Groq 빠른 분석

오류를 저장할 때 작은 모델을 이용해 짧은 메타데이터를 생성한다.

```json
{
  "summary": "pandas DataFrame에 존재하지 않는 컬럼을 조회했다.",
  "category": "data-access",
  "tags": [
    "python",
    "pandas",
    "keyerror"
  ],
  "difficulty": "basic",
  "deep_analysis_recommended": false
}
```

### 용도

- 오류 제목 자동 생성
- 태그 추천
- 오류 카테고리 분류
- 긴 메시지 한 줄 요약
- 검색용 설명 생성
- 정밀 분석 필요 여부 제안

### 토큰 절약 원칙

- 출력 토큰 제한
- 전체 코드 전송 금지
- OCR 원문 전체보다 핵심 오류 줄 우선
- 같은 오류에 대한 분석 결과 캐싱
- 사용자가 내용을 수정하지 않았다면 재호출하지 않음
- API 한도 초과 시 로컬 기능만 사용

---

## 기능 9. Groq 정밀 분석

사용자가 `정밀 분석` 버튼을 눌렀을 때만 큰 모델을 호출한다.

### 입력 정보

- 마스킹된 오류 메시지
- 관련 코드 앞뒤 약 10~30줄
- 프로그래밍 언어
- 라이브러리와 버전
- 오류가 발생한 상황
- 로컬에서 찾은 유사 오류 3개
- 과거에 성공하거나 실패한 해결 방법

### 출력 형식

```json
{
  "summary": "오류에 대한 쉬운 설명",
  "probable_causes": [
    {
      "cause": "merge 이후 컬럼명에 _x 또는 _y가 추가됨",
      "confidence": 0.62,
      "how_to_check": "df.columns.tolist()를 출력한다."
    },
    {
      "cause": "CSV 헤더에 공백이 포함됨",
      "confidence": 0.23,
      "how_to_check": "repr(df.columns.tolist())로 확인한다."
    }
  ],
  "debug_steps": [
    "현재 DataFrame의 컬럼 목록을 확인한다.",
    "공백과 접미사를 확인한다.",
    "해당 컬럼이 생성되는 코드의 실행 순서를 확인한다."
  ],
  "warnings": [
    "원인을 확인하기 전에 임의로 빈 컬럼을 생성하지 않는다."
  ],
  "verification": [
    "수정 후 동일한 입력 데이터로 코드를 다시 실행한다.",
    "예상한 컬럼이 존재하는지 단위 테스트를 추가한다."
  ]
}
```

### LLM 사용 원칙

- 하나의 정답을 단정하지 않는다.
- 가능한 원인을 여러 개 제시한다.
- 각 원인의 확인 방법을 반드시 포함한다.
- 바로 코드를 수정하기 전에 진단 절차를 제시한다.
- 불확실한 정보는 불확실하다고 표시한다.
- 과거 기록과 충돌할 경우 그 차이를 설명한다.
- 생성된 해결 코드는 사용자가 검토하도록 한다.

---

## 기능 10. 해결 과정 기록

사용자는 AI 또는 과거 기록에서 제안된 방법을 시도한 뒤 결과를 남긴다.

### 기록 항목

- 시도한 해결 방법
- 성공 여부
- `실패 / 부분 성공 / 해결` 상태
- 실제 원인
- 최종 수정 코드
- 해결에 걸린 시간
- 참고한 자료
- 다음에 기억할 내용
- 해결 후 검증 결과

### 여러 시도 기록 예시

```text
시도 1
방법: 컬럼 이름의 대소문자 변경
결과: 실패

시도 2
방법: merge 이후 생성된 _x, _y 접미사 확인
결과: 부분 성공

시도 3
방법: 필요한 컬럼만 선택한 뒤 merge 수행
결과: 해결
```

이 기능이 BugBox의 핵심 차별점이다. AI 답변 자체보다 **무엇을 시도했고 실제로 무엇이 성공했는지**가 더 중요한 데이터다.

---

## 기능 11. 오류 기록 관리

### 목록 기능

- 오류 제목
- 상태
- 언어
- 라이브러리
- 태그
- 발생 날짜
- 해결 여부
- AI 분석 여부

### 필터

- 미해결 오류
- 해결된 오류
- 프로그래밍 언어
- 오류 종류
- 태그
- 특정 프로젝트
- 발생 기간
- 반복 발생 여부

### 검색

- 오류 메시지 키워드 검색
- 제목 검색
- 의미 기반 검색
- 해결 방법 검색
- 코드 내용 검색

---

## 기능 12. 개인 오류 대시보드

핵심 기능이 완성된 뒤 시간이 남으면 구현한다.

### 표시할 통계

- 가장 자주 발생한 예외
- 언어별 오류 수
- 라이브러리별 오류 수
- 해결률
- 평균 해결 시간
- 반복 발생한 오류
- 가장 많이 실패한 해결 방식
- 최근 일주일 오류 발생량
- AI 분석이 실제 해결로 이어진 비율
- 과거 기록으로 해결한 비율

### 목적

단순히 예쁜 그래프를 보여주는 것이 아니라 사용자의 취약 영역을 확인한다.

```text
최근 반복 오류

1. React 상태 업데이트 관련 오류: 6회
2. pandas 컬럼명 오류: 4회
3. 비동기 처리 누락: 3회
```

---

# 10. 주요 화면 구성

## 10.1 홈 대시보드

- 전체 오류 수
- 미해결 오류 수
- 최근 등록 오류
- 자주 발생한 오류
- 새 오류 등록 버튼

## 10.2 오류 등록 화면

- 스크린샷 업로드
- 이미지 크롭
- 직접 로그 입력
- 관련 코드 입력
- 언어·라이브러리 선택
- 프로젝트명 입력

## 10.3 OCR 검토 화면

- 원본 이미지
- 전처리 이미지 비교
- OCR 박스 오버레이
- OCR 텍스트 편집
- 신뢰도 낮은 줄 강조
- 다시 전처리하는 버튼

## 10.4 민감정보 검토 화면

- 원본 텍스트
- 마스킹 결과
- 탐지된 민감정보 목록
- 사용자가 직접 추가 마스킹
- 외부 전송 동의 버튼

## 10.5 분석 결과 화면

- 구조화된 오류 정보
- 과거 유사 오류
- 규칙 기반 확인 사항
- 빠른 AI 요약
- 정밀 분석 버튼
- 원인 후보
- 디버깅 순서

## 10.6 해결 기록 화면

- 시도 추가
- 성공 상태 선택
- 실제 원인 입력
- 최종 해결 코드
- 검증 방법
- 해결 완료 처리

## 10.7 오류 상세 화면

- 원본 스크린샷
- 추출 로그
- AI 분석
- 유사 오류
- 해결 타임라인
- 수정 및 삭제
- Markdown 내보내기

---

# 11. 데이터베이스 설계 초안

## `errors`

```text
id
title
project_name
language
framework
library
exception_type
raw_log
masked_log
normalized_message
fingerprint
status
actual_cause
final_solution
created_at
updated_at
resolved_at
```

## `screenshots`

```text
id
error_id
original_path
processed_path
width
height
ocr_confidence
selected_preprocess_method
created_at
```

## `ocr_results`

```text
id
error_id
raw_text
corrected_text
bounding_boxes_json
confidence_json
created_at
```

## `solution_attempts`

```text
id
error_id
description
code_snippet
result
notes
attempted_at
```

## `ai_analyses`

```text
id
error_id
analysis_type
model_name
input_hash
result_json
created_at
```

## `embeddings`

```text
id
error_id
model_name
embedding_blob
source_text_hash
created_at
```

## `tags`

```text
id
name
```

## `error_tags`

```text
error_id
tag_id
```

## `masked_entities`

```text
id
error_id
entity_type
masked_token
start_position
end_position
created_at
```

---

# 12. FastAPI 엔드포인트 초안

```text
POST   /api/errors
GET    /api/errors
GET    /api/errors/{error_id}
PATCH  /api/errors/{error_id}
DELETE /api/errors/{error_id}

POST   /api/images/preprocess
POST   /api/ocr
PATCH  /api/errors/{error_id}/ocr

POST   /api/privacy/detect
POST   /api/privacy/mask

POST   /api/errors/{error_id}/parse
POST   /api/errors/{error_id}/fingerprint
GET    /api/errors/{error_id}/similar

POST   /api/errors/{error_id}/ai/quick
POST   /api/errors/{error_id}/ai/deep

POST   /api/errors/{error_id}/attempts
PATCH  /api/attempts/{attempt_id}
DELETE /api/attempts/{attempt_id}

GET    /api/dashboard/summary
GET    /api/dashboard/categories

GET    /api/errors/{error_id}/export
```

## API 설계 학습 포인트

- GET, POST, PATCH, DELETE 차이
- Path parameter
- Query parameter
- Request body
- HTTP 상태 코드
- 파일 업로드
- CORS
- 요청 및 응답 검증
- 예외 처리
- 비동기 처리
- API 문서화

---

# 13. 권장 폴더 구조

```text
bugbox/
├─ frontend/
│  ├─ src/
│  │  ├─ api/
│  │  ├─ components/
│  │  ├─ features/
│  │  │  ├─ error-upload/
│  │  │  ├─ ocr-review/
│  │  │  ├─ privacy-review/
│  │  │  ├─ similar-errors/
│  │  │  └─ solution-log/
│  │  ├─ pages/
│  │  ├─ hooks/
│  │  ├─ types/
│  │  └─ utils/
│  ├─ public/
│  └─ package.json
│
├─ backend/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ api/
│  │  │  ├─ errors.py
│  │  │  ├─ images.py
│  │  │  ├─ ocr.py
│  │  │  ├─ privacy.py
│  │  │  └─ analysis.py
│  │  ├─ core/
│  │  │  ├─ config.py
│  │  │  ├─ exceptions.py
│  │  │  └─ logging.py
│  │  ├─ cv/
│  │  │  ├─ preprocess.py
│  │  │  ├─ roi.py
│  │  │  └─ visualization.py
│  │  ├─ ocr/
│  │  │  ├─ engine.py
│  │  │  ├─ postprocess.py
│  │  │  └─ evaluator.py
│  │  ├─ parsing/
│  │  │  ├─ base.py
│  │  │  ├─ python_parser.py
│  │  │  ├─ javascript_parser.py
│  │  │  └─ fingerprint.py
│  │  ├─ privacy/
│  │  │  ├─ detector.py
│  │  │  └─ masker.py
│  │  ├─ search/
│  │  │  ├─ embedder.py
│  │  │  ├─ similarity.py
│  │  │  └─ ranker.py
│  │  ├─ ai/
│  │  │  ├─ base.py
│  │  │  ├─ groq_client.py
│  │  │  ├─ prompts.py
│  │  │  └─ schemas.py
│  │  ├─ database/
│  │  │  ├─ models.py
│  │  │  ├─ schemas.py
│  │  │  └─ session.py
│  │  └─ services/
│  ├─ tests/
│  └─ requirements.txt
│
├─ data/
│  ├─ database/
│  ├─ screenshots/
│  ├─ processed/
│  └─ models/
│
├─ docs/
│  ├─ architecture.md
│  ├─ api.md
│  ├─ privacy.md
│  └─ experiments/
│
├─ .env.example
├─ .gitignore
├─ README.md
└─ LICENSE
```

기능별 모듈을 분리하는 이유는 OpenCV, OCR, 파싱, 검색, LLM 기능이 서로 강하게 결합되는 것을 방지하기 위해서다.

---

# 14. 사전에 알아두어야 할 지식

모든 내용을 개발 전에 완벽히 공부할 필요는 없다. 필요한 기능을 구현하면서 순서대로 학습한다.

## Python 기초

- 함수와 클래스
- 모듈과 패키지
- 타입 힌트
- 예외 처리
- 파일 입출력
- JSON 처리
- 가상환경
- 비동기 함수 기초

## 웹 기초

- 클라이언트와 서버
- HTTP 요청과 응답
- REST API
- JSON
- CORS
- 파일 업로드 방식
- 프론트엔드와 백엔드 분리

## React 기초

- 컴포넌트
- Props
- State
- Hook
- 이벤트 처리
- 조건부 렌더링
- 목록 렌더링
- API 호출
- 로딩 및 오류 상태

## 데이터베이스 기초

- 테이블
- 행과 열
- 기본키와 외래키
- 1:N 관계
- CRUD
- 인덱스
- 트랜잭션
- 정규화

## 컴퓨터 비전 기초

- 이미지의 픽셀 구조
- RGB와 BGR
- 그레이스케일
- 커널과 필터
- 블러
- 선명화
- 히스토그램
- 임계값
- 모폴로지
- 윤곽선
- 바운딩 박스
- 좌표계
- 이미지 보간

## NLP와 검색 기초

- 토큰
- 정규표현식
- 문자열 정규화
- 임베딩
- 코사인 유사도
- 키워드 검색
- 의미 기반 검색
- 검색 결과 재정렬

## LLM 기초

- 프롬프트
- 입력·출력 토큰
- 컨텍스트
- Temperature
- 최대 출력 토큰
- 구조화된 JSON 출력
- 환각
- Rate limit
- 재시도
- Timeout
- 캐싱

## 보안 기초

- 환경변수
- API 키 관리
- `.gitignore`
- 로그 마스킹
- 입력 검증
- 파일 확장자 검증
- 경로 조작 공격
- Prompt injection 가능성

---

# 15. 이 프로젝트에서 얻을 수 있는 지식

## 컴퓨터 비전

- 입력 이미지의 품질이 OCR 결과에 미치는 영향
- 전처리 방식별 성능 차이
- 어두운 IDE 테마와 밝은 IDE 테마 처리
- 텍스트 영역 검출
- 좌표 기반 시각화
- 자동 처리와 사용자 보정의 결합
- 정량적 OCR 평가 방법

## 인공지능

- 사전학습 OCR 모델 활용
- 임베딩 기반 검색
- 규칙 기반 시스템과 LLM의 결합
- 작은 모델과 큰 모델의 역할 분리
- 검색 결과를 컨텍스트로 제공하는 방식
- 생성형 AI 출력 검증
- 사용자의 실제 피드백을 이용한 개인화

## 백엔드

- Python API 서버 구축
- 파일 처리
- 계층형 아키텍처
- 서비스 레이어
- 데이터 검증
- 오류 처리
- 외부 API 연동
- 비동기 요청
- API 테스트

## 프론트엔드

- 복잡한 다단계 폼
- 이미지 업로드
- 이미지 위 좌표 오버레이
- API 진행 상태
- 사용자 교정 인터페이스
- 검색 및 필터
- 데이터 시각화

## 데이터베이스

- 오류와 해결 시도의 1:N 관계
- 태그 다대다 관계
- 임베딩 저장
- 중복 데이터 방지
- 데이터 마이그레이션
- 검색 성능 개선

## 소프트웨어 설계

- 관심사 분리
- 인터페이스 기반 설계
- 외부 API 교체 가능성
- 확장 가능한 모듈 구조
- 실패해도 기본 기능이 유지되는 폴백 설계
- 기능별 테스트 가능성

---

# 16. AI 분석기 교체 구조

Groq에 프로젝트 전체가 종속되지 않게 분석기 인터페이스를 만든다.

```python
from abc import ABC, abstractmethod


class AIAnalyzer(ABC):

    @abstractmethod
    async def quick_analyze(self, context: dict) -> dict:
        pass

    @abstractmethod
    async def deep_analyze(self, context: dict) -> dict:
        pass
```

```python
class GroqAnalyzer(AIAnalyzer):
    ...
```

```python
class RuleBasedAnalyzer(AIAnalyzer):
    ...
```

향후 다음 분석기를 추가할 수 있다.

- Ollama 로컬 LLM
- 다른 무료 API
- 유료 API
- 규칙 기반 분석기
- AI 기능을 완전히 끈 오프라인 모드

## 장점

- Groq 모델 종료에 대응 가능
- 무료 한도가 부족할 때 로컬 분석으로 전환 가능
- 테스트 시 실제 API를 호출하지 않아도 됨
- 모델별 결과 비교 가능
- API 비용이 생겨도 다른 제공자로 교체 가능

---

# 17. 평가 방법

프로젝트가 작동한다는 것과 성능이 좋다는 것은 다르다. 각 기능별로 평가 기준을 정한다.

## 17.1 OCR 평가

### 문자 오류율

정답 텍스트와 OCR 결과의 문자 차이를 비교한다.

### 줄 인식률

전체 오류 로그 줄 중 올바르게 인식한 줄의 비율을 측정한다.

### 핵심 오류 인식률

`KeyError`, `TypeError`, 파일명, 줄 번호 등 핵심 정보가 정확히 추출되었는지 평가한다.

### 실험 조건

- 밝은 테마
- 어두운 테마
- 작은 글자
- 고해상도
- 저해상도
- 여러 패널이 포함된 화면
- 크롭된 터미널 화면

## 17.2 오류 파서 평가

- 예외 클래스 정확도
- 파일명 정확도
- 줄 번호 정확도
- 라이브러리 분류 정확도
- 오류 카테고리 정확도

각 항목별 Precision, Recall, F1-score를 계산할 수도 있다.

## 17.3 유사 오류 검색 평가

### Top-k Accuracy

실제로 같은 유형의 오류가 검색 결과 상위 k개 안에 포함되는지 확인한다.

### MRR

정답에 해당하는 유사 오류가 몇 번째에 등장했는지를 평가한다.

### 사용자 평가

검색 결과가 실제 해결에 도움이 되었는지 다음 값으로 기록한다.

- 매우 도움 됨
- 일부 도움 됨
- 도움 안 됨

## 17.4 AI 분석 평가

LLM 결과를 다음 기준으로 직접 평가한다.

- 오류 내용을 올바르게 이해했는가?
- 가능한 원인이 현실적인가?
- 확인 절차가 실행 가능한가?
- 존재하지 않는 함수나 옵션을 만들지 않았는가?
- 과도하게 단정하지 않았는가?
- 민감정보가 출력에 복구되지 않았는가?
- 실제 해결에 도움이 되었는가?

---

# 18. 테스트 데이터 준비

개발 중 실제 오류가 발생할 때마다 BugBox 데이터셋에 추가한다.

추가로 테스트용 오류를 직접 만든다.

## Python 오류

- SyntaxError
- TypeError
- ValueError
- KeyError
- IndexError
- AttributeError
- ModuleNotFoundError
- ImportError
- FileNotFoundError
- PermissionError

## JavaScript 오류

- `undefined` 속성 접근
- `null` 속성 접근
- ReferenceError
- SyntaxError
- 비동기 Promise 오류
- React Hook 사용 오류
- JSX 컴파일 오류
- npm 패키지 오류

## 이미지 조건

각 오류에 대해 다음 버전을 만든다.

- 원본 스크린샷
- 축소된 이미지
- 흐린 이미지
- 밝기가 낮은 이미지
- 밝은 테마
- 어두운 테마
- 전체 화면
- 오류 영역만 크롭한 이미지

## 테스트 데이터 주의사항

공개 저장소에 올릴 테스트 이미지에는 개인 경로, 실제 API 키, 비공개 코드가 포함되지 않도록 한다.

---

# 19. 한 달 개발 일정

## 1주차: 프로젝트 기반과 오류 기록

### 목표

AI와 OCR 없이도 오류를 등록하고 관리할 수 있는 기본 애플리케이션을 완성한다.

### 구현

- [ ] React 프로젝트 생성
- [ ] FastAPI 프로젝트 생성
- [ ] 프론트엔드와 백엔드 연결
- [ ] SQLite 연동
- [ ] 오류 등록 API
- [ ] 오류 목록 API
- [ ] 오류 상세 API
- [ ] 오류 수정·삭제
- [ ] 스크린샷 업로드
- [ ] 기본 화면 구현

### 공부

- React 컴포넌트
- FastAPI
- HTTP
- CRUD
- SQLite
- 파일 업로드
- Git 브랜치와 커밋

### 완료 기준

스크린샷과 로그를 등록하고 저장된 기록을 다시 열어볼 수 있다.

---

## 2주차: 컴퓨터 비전과 OCR

### 목표

스크린샷을 분석하여 오류 텍스트를 추출한다.

### 구현

- [ ] OpenCV 이미지 불러오기
- [ ] 이미지 확대
- [ ] 그레이스케일
- [ ] 대비 향상
- [ ] 이진화
- [ ] 색상 반전
- [ ] 여러 전처리 결과 비교
- [ ] PaddleOCR 연동
- [ ] OCR 박스 시각화
- [ ] OCR 결과 수정 화면
- [ ] OCR 신뢰도 표시

### 공부

- 픽셀과 색상 공간
- Threshold
- Adaptive threshold
- Blur와 sharpening
- Morphology
- Bounding box
- OCR의 검출과 인식

### 완료 기준

일반적인 터미널 스크린샷에서 핵심 오류 문구를 추출하고 사용자가 교정할 수 있다.

---

## 3주차: 오류 파싱과 유사 검색

### 목표

오류를 구조화하고 과거 기록을 검색한다.

### 구현

- [ ] Python 오류 파서
- [ ] JavaScript 오류 파서
- [ ] 오류 지문 생성
- [ ] 개인정보 탐지
- [ ] 마스킹 결과 확인
- [ ] Sentence Transformers 연동
- [ ] 임베딩 저장
- [ ] 코사인 유사도 검색
- [ ] 검색 점수 결합
- [ ] 유사 오류 화면

### 공부

- 정규표현식
- 문자열 정규화
- 임베딩
- 벡터
- 코사인 유사도
- 검색 랭킹
- 개인정보 패턴

### 완료 기준

현재 오류와 비슷한 과거 오류를 상위 검색 결과로 보여준다.

---

## 4주차: Groq 분석과 완성도 개선

### 목표

AI 분석, 해결 과정 기록, 평가와 문서화를 완성한다.

### 구현

- [ ] Groq API 연동
- [ ] 빠른 분석
- [ ] 정밀 분석
- [ ] JSON 출력 검증
- [ ] Rate limit 오류 처리
- [ ] 분석 결과 캐싱
- [ ] 해결 시도 기록
- [ ] 최종 해결 처리
- [ ] Markdown 내보내기
- [ ] 테스트 코드
- [ ] README
- [ ] 실행 GIF 또는 영상
- [ ] 프로젝트 회고

### 공부

- LLM API
- 프롬프트 설계
- 구조화된 출력
- 외부 API 예외 처리
- 백오프와 재시도
- 캐싱
- 테스트
- 프로젝트 문서화

### 완료 기준

오류 등록부터 해결 기록까지 전체 사용 흐름이 끊기지 않고 작동한다.

---

# 20. 우선순위

## 반드시 구현할 기능

1. 오류 스크린샷 및 로그 등록
2. OpenCV 이미지 전처리
3. PaddleOCR 텍스트 추출
4. OCR 결과 사용자 교정
5. 민감정보 마스킹
6. 오류 구조화 및 지문 생성
7. 과거 유사 오류 검색
8. Groq 정밀 분석
9. 해결 과정과 성공 여부 기록
10. 오류 목록 및 상세 조회

## 시간이 남으면 구현할 기능

1. Groq 빠른 자동 분류
2. 오류 통계 대시보드
3. Markdown 내보내기
4. 전처리 방식 자동 선택
5. Python·JavaScript 외 언어 지원
6. 검색 가중치 자동 조정
7. 다크모드
8. OCR 성능 비교 리포트
9. 오프라인 규칙 기반 분석
10. Ollama 로컬 LLM 백엔드

---

# 21. 프로젝트 성공 기준

다음 조건을 만족하면 1차 버전이 완성된 것으로 본다.

- [ ] 이미지와 로그를 등록할 수 있다.
- [ ] 이미지가 로컬에 저장된다.
- [ ] 최소 세 가지 전처리 방식을 적용할 수 있다.
- [ ] OCR 결과와 텍스트 좌표를 확인할 수 있다.
- [ ] 사용자가 OCR 결과를 수정할 수 있다.
- [ ] API 키, 이메일, 사용자 경로를 마스킹할 수 있다.
- [ ] Python과 JavaScript 오류를 일부 구조화할 수 있다.
- [ ] 오류 지문을 생성할 수 있다.
- [ ] 유사 오류 상위 3개를 검색할 수 있다.
- [ ] 마스킹된 텍스트만 Groq에 전송된다.
- [ ] AI가 원인 후보와 확인 절차를 JSON으로 반환한다.
- [ ] 해결 시도를 여러 개 저장할 수 있다.
- [ ] 최종 해결 방법을 기록할 수 있다.
- [ ] API 실패 시에도 오류 기록과 검색 기능은 작동한다.
- [ ] 설치 방법과 실행 방법이 README에 작성되어 있다.
- [ ] 개인정보 및 보안 설계가 문서화되어 있다.

---

# 22. 예상 문제와 대응 방법

## 22.1 OCR 정확도가 낮음

### 원인

- 작은 글씨
- 어두운 테마
- 코드 특수문자
- 복잡한 화면 배치

### 대응

- 이미지 확대
- 여러 전처리 결과 비교
- 사용자가 ROI 선택
- 사용자 직접 교정
- 핵심 오류 키워드 기반 결과 선택

## 22.2 Groq 무료 한도 초과

### 대응

- 분석 버튼을 눌렀을 때만 호출
- 기존 분석 결과 캐싱
- 긴 코드 전송 제한
- 빠른 분석과 정밀 분석 분리
- Rate limit 발생 시 로컬 검색 결과 제공
- AI 기능 없이도 앱을 사용할 수 있도록 설계

## 22.3 LLM이 잘못된 해결책을 제시함

### 대응

- 정답 대신 원인 후보를 요청
- 후보마다 확인 방법을 요구
- 과거 성공 기록을 함께 제공
- 신뢰도는 모델의 추정임을 표시
- 실제 해결 여부를 사용자에게 기록받음
- 자동 코드 실행 금지

## 22.4 유사 검색 결과가 부정확함

### 대응

- 임베딩 유사도만 사용하지 않음
- 오류 지문을 함께 비교
- 언어와 라이브러리 필터 적용
- 예외 타입 일치 점수 추가
- 사용자가 유사 여부 평가
- 검색 가중치 실험

## 22.5 프로젝트 범위가 커짐

다음 우선순위를 지킨다.

```text
오류 기록
→ OCR
→ 파싱
→ 유사 검색
→ AI 분석
→ 해결 기록
→ 부가 기능
```

새 기능을 추가하기 전 다음 질문을 한다.

> 이 기능이 오류를 읽고, 찾고, 해결 과정을 기억하는 핵심 흐름에 필요한가?

필요하지 않다면 후순위 기능으로 이동한다.

---

# 23. 응용 분야

## 개발 트러블슈팅 관리

- 개인 개발자 오류 기록
- 팀 내부 장애 사례 관리
- 기술지원 지식베이스
- 사내 개발 FAQ
- 반복 장애 분석

## IT 헬프데스크

- 프로그램 오류 화면 수집
- 사용자 문의 스크린샷 분석
- 유사 문의 자동 검색
- 해결 이력 추천

## 교육

- 프로그래밍 수업의 오답노트
- 학생별 반복 오류 분석
- 오류 유형별 학습 자료 추천
- 디버깅 과정 평가

## 테스트 및 품질관리

- 테스트 실패 로그 분류
- 반복 실패 패턴 검색
- 회귀 오류 추적
- 오류 발생 빈도 분석

## 문서 이미지 처리

- 스크린샷 OCR
- 문서 구조 분석
- 민감정보 마스킹
- 이미지 기반 검색

## 보안

- 로그 내 비밀 키 탐지
- 개인정보 포함 여부 검사
- 외부 전송 전 데이터 비식별화

---

# 24. 포트폴리오에서 강조할 점

BugBox를 단순히 “AI가 오류를 알려주는 앱”이라고 설명하지 않는다.

## 컴퓨터 비전

다양한 IDE 테마와 해상도의 오류 스크린샷에서 OCR 성능을 높이기 위해 여러 이미지 전처리 방식을 비교했다.

## OCR

텍스트 검출 좌표와 신뢰도를 이용해 사용자가 인식 결과를 검토하고 수정할 수 있도록 설계했다.

## 정보보호

오류 로그가 외부 LLM에 전달되기 전에 API 키, 로컬 경로, 이메일, 데이터베이스 주소 등을 로컬에서 마스킹했다.

## 검색

키워드가 달라도 의미가 비슷한 오류를 찾기 위해 임베딩 기반 의미 검색과 규칙 기반 오류 지문을 결합했다.

## LLM

작은 모델은 구조화와 분류에 사용하고 큰 모델은 사용자가 요청한 복잡한 원인 분석에만 사용해 무료 API 한도를 관리했다.

## 개인화

AI의 일반적인 답변보다 사용자가 과거에 실제로 성공한 해결 방법을 우선 추천했다.

## 안정성

Groq API가 실패하거나 한도를 초과해도 OCR, 기록, 검색 기능은 정상 작동하도록 폴백 구조를 구현했다.

---

# 25. README용 프로젝트 설명 초안

## BugBox

BugBox is a personal debugging memory system that converts error screenshots into searchable and reusable troubleshooting knowledge.

It uses local computer vision and OCR to extract error messages, masks sensitive information before external transmission, retrieves similar past errors through semantic search, and optionally uses an LLM to suggest probable causes and diagnostic steps.

Unlike a general-purpose debugging chatbot, BugBox prioritizes solutions that the user has previously tested and confirmed in their own development environment.

### Core Features

- Error screenshot preprocessing with OpenCV
- Local OCR with PaddleOCR
- Editable OCR results and confidence visualization
- Sensitive information detection and masking
- Error parsing and fingerprint generation
- Semantic search over past debugging records
- Optional Groq-powered cause analysis
- Resolution attempts and success-history tracking
- Fully functional local fallback without LLM access

---

# 26. 개발 중 기록할 실험

단순히 코드를 완성하는 것뿐 아니라 실험 과정도 개발노트와 GitHub에 남긴다.

## OCR 실험표

```text
실험 번호:
입력 이미지:
IDE 테마:
해상도:
전처리 방식:
OCR 평균 신뢰도:
핵심 오류 인식 여부:
문제점:
개선 아이디어:
```

## 검색 실험표

```text
검색 오류:
기대하는 유사 오류:
검색된 상위 5개:
정답 순위:
사용 임베딩 모델:
검색 가중치:
문제점:
```

## LLM 실험표

```text
사용 모델:
입력 토큰:
출력 토큰:
프롬프트 버전:
구조화 출력 성공 여부:
원인 후보의 적절성:
실제 해결에 도움을 주었는가:
환각 또는 잘못된 정보:
```

## 개발 일지

```text
오늘 구현한 기능:
새롭게 배운 개념:
발생한 오류:
오류의 원인:
해결 방법:
아직 이해하지 못한 부분:
다음 구현 목표:
```

BugBox를 개발하다 발생한 오류를 BugBox의 테스트 데이터로 다시 넣을 수 있다. 프로젝트를 만드는 과정 자체가 프로젝트의 데이터셋이 되는 구조다.

---

# 27. 최종 프로젝트 정의

BugBox는 오류를 대신 해결해주는 만능 AI가 아니다.

BugBox는 다음 세 가지 역할을 수행한다.

1. **오류 화면을 읽는다.**
2. **과거의 해결 경험을 찾아준다.**
3. **새로운 해결 과정을 다시 기억한다.**

컴퓨터 비전과 OCR은 오류 화면을 읽기 위해 사용한다. 임베딩 검색은 과거 경험을 찾기 위해 사용한다. LLM은 가능한 원인과 확인 순서를 정리하기 위해 사용한다. 데이터베이스는 실제로 성공한 해결 경험을 축적하기 위해 사용한다.

따라서 BugBox의 본체는 Groq API가 아니라 다음 구조다.

> **로컬 이미지 처리 + 오류 구조화 + 개인 해결 기록 + 의미 기반 검색**

Groq는 이 본체를 보조하는 선택적 추론 도구다.

이 원칙을 유지하면 BugBox는 단순한 LLM API 래퍼가 아니라 컴퓨터 비전, 검색, 백엔드, 데이터베이스, 보안, 생성형 AI를 하나의 실제 사용 흐름 안에서 결합한 개인 프로젝트가 된다.

---

# 참고 공식 문서

- [React Documentation](https://react.dev/learn)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenCV Documentation](https://docs.opencv.org/4.x/)
- [PaddleOCR Documentation](https://paddlepaddle.github.io/PaddleOCR/)
- [SQLite Documentation](https://sqlite.org/)
- [Sentence Transformers Documentation](https://sbert.net/)
- [Groq Documentation](https://console.groq.com/docs/)
