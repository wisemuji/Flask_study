from flask import Flask, request

app = Flask(__name__)

@app.route("/example/environ", methods=["GET", "POST"])
def example_environ():
    print(request.environ)
    return str(request.environ)

app.run()

