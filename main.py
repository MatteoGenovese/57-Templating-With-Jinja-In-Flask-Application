from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


# @app.route('/')
# def home():
#     randomNumber = random.randint(1, 9)
#     currentYearToSend = datetime.datetime.now().year
#     print(currentYearToSend)
#     return render_template("index.html", num=randomNumber, currentYear=currentYearToSend)


@app.route('/guess/<name>')
def guess(name):
    ageResponse = requests.get(f"https://api.agify.io?name={name}")
    age = ageResponse.json()["age"]
    genderResponse = requests.get(f"https://api.genderize.io?name={name}")
    gender = genderResponse.json()["gender"]
    return render_template("guess.html", age=age, name=name, gender=gender)


@app.route('/')
def blog():
    articlesUrl = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(articlesUrl)
    blogArticles = response.json()
    return render_template("post.html", articles=blogArticles, articleNumber="all")


@app.route('/posts/<number>')
def post(number):
    articleNumber = int(number)
    articlesUrl = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(articlesUrl)
    blogArticle = response.json()
    return render_template("post.html", articles=blogArticle, articleNumber=articleNumber)


if __name__ == "__main__":
    app.run(debug=True)
