# python-project-template-2023

새 파이썬 프로젝트 시작할 때 사용하실 템플릿입니다.

주요 기능

1. Github Actions로 black (formatter), isort (formatter), ruff (linter), pytest (test) 통과 여부 확인
2. pytest / tox 커맨드 사용 가능

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
