from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def helloworld():
    return "Hello World"
app.add_url_rule("/hello", "hello", hello_world)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224, debug=True)

