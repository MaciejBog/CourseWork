from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,9)
print(random_number)

toolow_html = ("<h1 style='color: blue'>Too low, try again!</h1>"
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")
toohigh_html = ("<h1 style='color: red'>Too high</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
correct_html = ("<h1 style='color: green'>You got it!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")

@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")

@app.route("/<name>")
def check_number(name):
    if int(name) < random_number:
        return toolow_html
    if int(name) > random_number:
        return toohigh_html
    if int(name) == random_number:
        return correct_html

if __name__ == "__main__":
    app.run(port=8000, debug=True)
