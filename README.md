# python-project-template-2023

새 파이썬 프로젝트 시작할 때 사용하실 템플릿입니다.

노션: https://www.notion.so/Z-Python-Project-Packaging-c9d8b9824a5243929adce03f8091cd16?pvs=4

**주요 기능**

1. Github Actions로 black (formatter), isort (formatter), ruff (linter), pytest (test) 통과 여부 확인
2. pytest / tox 커맨드 사용 가능

## 돌려 보기

1. `pip install -e .`으로 dependencies 및 zproject 패키지 설치
2. `python tools/color_logging_main.py` 실행해보기. 로깅 내용은 `train.log` 파일에도 기록됨 (저장 위치는 알아서 변경해 쓰기)
3. `pip install -e .[dev]` (다른방법: `pip install -r requirements_dev.txt` 으로 pytest 등 개발자용 패키지도 설치가능
4. `pytest` 커맨드로 테스트 실행해보기.
5. `tox` 커맨드로 테스트 여러 환경에서 실행해볼수도 있음. 엄청 중요한건 아님 (github action 쉽게 쓰기 위함이 더 목적임)

## 파일 설명

1. `.github` 폴더: 깃헙 액션 및 Issues 템플릿을 정의합니다.
2. `src/zproject` 폴더: `import zproject` 해서 사용할 수 있는 함수나 클래스 등을 정의합니다.
  a. 모델, 데이터셋 등
3. `src/zproject/_version.py`: `setuptools-scm`에서 자동 생성되는 버전정보 파일. git 트래킹하지 않습니다.
4. `tools/` 폴더: import 하지 않고 바로 실행 가능한 파일들. (예: train.py)
5. `tests/` 폴더: `pytest` 실행시 실행되는 함수들
6. `pyproject.toml`: 파이썬 프로젝트 일반 정보. `pip install -e .`으로 설치할 때 설치되는 dependencies는 물론, ruff등 외부 툴의 설정도 포함합니다.
7. `requirements.txt`: 혹시 모를 dependency 오류를 방지하기 위해 현재 사용중인 static version 작성. `pyproject.toml`과 얼추 비슷해야함.
8. `requirements_dev.txt`: 프로그램 사용자가 아닌 개발자에게 필요한 dependencies. `pyproject.toml`과 얼추 비슷해야함.

## Github 사용법

예시로 issues와 pull requests가 있음. 어떻게 쓰는건지 둘러보기.

1. main이 아닌 branch를 만들어 개발
2. 해당 branch를 push하고, pull request를 올림
3. 어떤 issue를 fix하는지 쓰기 (예: Fixes #1) -> accept되면 자동으로 issue 닫힘
4. pull request는 다른 팀원이 간략히 코드 리뷰하고 squash 혹은 rebase하면 됨. merge는 웬만하면 피하기.

또한, release에서 새 버전 생성 가능

## 템플릿 사용하기

`pyproject.toml`, `requirements.txt` 등 바꿔서 쓰면 됨. 이름 `zproject`인거 전부 새 패키지 이름으로 치환해 쓰기
