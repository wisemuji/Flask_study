from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = 'GDJKWKSHIOWHKDLKSILD'

@app.route("/session_set")
def session_set():
    session['ID'] = 'SUHYEON Flask Session Setting'
    return "세션이 설정되었습니다."

@app.route("/session_out")
def session_out():
    del session['ID']
    return "세션이 제거되었습니다."

@app.route("/session_status")
def session_status():
    return session['ID'] 

app.run()