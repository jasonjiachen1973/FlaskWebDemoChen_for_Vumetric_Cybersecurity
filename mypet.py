
from flask import Flask, render_template, request


app = Flask(__name__)


class Pet():
    def __init__(self, height, name):
        self.height = height
        self.name = name

        is_human = False

    def is_tall(self):
        if self.height >= 50:
            result = 'is tall!'
        else:
            result = 'is not tall!'

        return result

    def get_img(self):

        if self.height >= 50:
            img = 'https://i0.wp.com/theverybesttop10.com/wp-content/uploads/2018/02/The-Top-10-Biggest-Breeds-of-Dogs-You-Can-Have-as-a-Pet.jpg?fit=600%2C426&ssl=1'
        else:
            img = 'https://post.healthline.com/wp-content/uploads/2020/08/3180-Pug_green_grass-732x549-thumbnail-732x549.jpg'
        return img


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="This demo shows a simple flask workflow",
    )


@app.route("/result", methods=['POST'])
def if_tall():

    name = request.form['name']
    height = int(request.form['height'])
    pet = Pet(height, name)
    return render_template("card.html", name=pet.name, result=pet.is_tall(), img=pet.get_img())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
