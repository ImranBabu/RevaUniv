from flask import Flask,render_template

app = Flask(__name__)

@app.route("/reva")
def reva_home():
    return {"data" : "It's created."}

@app.route("/access_image")
def access_image():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)