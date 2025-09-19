from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        login_id=request.form['Loginid']
        login_pw=request.form['password']
        return f"id: {login_id}, pw: {login_pw}"

@app.route("/info")
def information():
    data = {
        "id": "s01",
        "name": "홍길동",
        "age": "24",
        "team": ["a",'b','c']
    }
    return render_template("info.html", context=data)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/boot")
def boot():
    return render_template("boot_test.html")

if __name__ == "__main__":
    app.run()