# Flask study with `Flask 기반의 Phthon 웹 프로그래밍(이지호 지음)`
 
## 이 저장소의 목적
 도서 `Flask 기반의 Phthon 웹 프로그래밍` 을 공부하면서 배운 내용들을 정리하고 자유롭게 코드를 작성하는 저장소입니다. 잘못 작성된 부분이 있다면 자유롭게 new Issue 로 알려주세요!
- [Outline](#outline)
- [Develop Environment](#develop-environment)
- [Web Server](#web-server)
 
## Outline
**마이크로(micro) 프레임워크란?**

Django와 같은 풀스택 프레임워크는 보통 웹 프로그래밍을 할 때 필요로 하는 모든 것들이 종합적으로 갖추어진 프레임워크를 의미하는데 마이크로 프레임워크는 파이선 웹 프로그래밍에서 가장 핵심적인 요소만 포함하고 있다. 
 
**Flask 시작하기**

마이크로 웹 프레임워크인 `Flask`는 `Django`와 더불어 인기있는 Phthon 웹 프로그래밍 프레임워크다. 프로그래미어는 데이터베이스 통합, 폼 유효성 검사, 업로드 처리, 다양한 개방형 인증 기술 등을 프로그래머와 환경에 맞게 추가하거나 직접 개발하여 사용할 수 있다. 또한 `Hook`을 걸어 Flask의 동작을 쉽게 제어할 수 있다.

**Flask와 함께 설치되는 의존성 라이브러리**

* WSGI 코어
* werkzeug(벡자이그) (URL 라우팅 지원)
* Jinja2 

**기타 특징**

- Flask는 환경 설정 값(템플릿 경로, static 파일 경로 설정 등)을 가지고 있다.
- 소스 트리 내 static, templates 디렉터리를 갖춰야 한다.

## Develop Environment

Python이 설치되었다고 가정한다.

**Flask 설치 (의존성 라이브러리 `Werkzeug`, `Jinja2`, `itsdangerous`, `click` 이 같이 설치됨)**
```console
$ pip3 install flask
```

## Web Server

**간단한 웹 서버 생성**
```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def helloworld():
    return "Hello World"

if __name__ == '__main__':
    app.run(port=3000)
```

[`http://localhost:3000`](http://localhost:3000) 에 접속하면 'Hello World'가 출력되게 하는 예제다. 
