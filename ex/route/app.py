from flask import Flask
app = Flask(__name__)


@app.route("/")
def helloworld():
    return "Hello World"

@app.route("/board/<article_id>")
@app.route("/board", defaults={ "article_id": 10 }) # /board로 접속시 article_id의 기본값 10으로 지정
def board(article_id):
    return "{}번 게시물을 보고 계십니다.".format(article_id)

@app.route("/sub", subdomain="<user_domain>") # 서브 도메인 라우팅
def board_domain_testandanswer(user_domain):
    return "{} 도메인의 /sub URL을 호출하셨습니다.".format(user_domain)

@app.route("/redirect", redirect_to="/new_board") # redirct
def redirect():
    return "/redirect URL을 호출했지만 실행이 안될걸"

@app.route("/new_board")
def new_board():
    return "/new_board URL 호출"

if __name__ == "__main__":
    app.run()