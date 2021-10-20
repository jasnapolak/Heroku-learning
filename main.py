from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        name = request.form.get("your-name")
        return f"Hello {name}! :)"


@app.route("/second-handler")
def second_handler():
    return "Here's is the second handler"


@app.route('/about')
def about():
    return 'Something about me'


if __name__ == '__main__':
    app.run()
