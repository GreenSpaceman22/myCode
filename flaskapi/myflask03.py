from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello admin"

@app.route("/guest/<guesty>")
def hello_guest():
    return f"Hello {guesty} Guest"

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":

        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guesty = name))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
