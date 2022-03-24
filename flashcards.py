from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="This demo shows a simple flask workflow",
    )


@app.route("/addemp", methods=['POST'])
def addnmae():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return render_template("card.html", first_name=first_name, last_name=last_name)


if __name__ == '__main__':
    app.run()
