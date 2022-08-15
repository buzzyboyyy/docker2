from flask import Flask, redirect, url_for
from googleapiclient.discovery import build
from healthcheck import HealthCheck
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = (os.getenv("API_KEY"))

app = Flask(__name__)
health = HealthCheck()

@app.route("/")
def home():
    return "Welcome to the THUNDERDOME <h1>THUNDER</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/health")
def healthtest():
     return health.run()

@app.route("/youtube")
def youtubeprint():
    youtube=build('youtube', 'v3', developerKey=API_KEY)
    
    request=youtube.videos().list(
        part='snippet',
        chart='mostPopular'
    )
    response=request.execute()

    info=response['items'][0]['snippet']['title']

    return("Most Watched Video Today: " + info)
    
@app.route("/tiddy")
def tiddytest():
    return("tiddy")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
