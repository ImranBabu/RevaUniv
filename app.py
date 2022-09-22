from flask import Flask

app = Flask(__name__)

@app.route("/reva")
def reva_home():
    return {"data" : "It's created."}

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)