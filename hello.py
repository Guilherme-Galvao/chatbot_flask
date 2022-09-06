from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return b"Viva la vida"

if __name__== "__main__":
    app.run()