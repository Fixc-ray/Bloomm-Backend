from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome to Bloom</h1>"


if __name__ == "__main__":
    app.run(port= 5500, debug=True)