from chatterbot import ChatBot
from dadjokes.dadjokes import Dadjoke
from chatbot import chatbot
from werkzeug.serving import run_simple
from flask import Flask, render_template, request
from randfacts import get_fact

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg').lower()
    s = str(chatbot.get_response(userText))
    if "joke" in userText or "jokes" in userText or "laugh" in userText:
        s = Dadjoke().joke
    elif "fact" in userText or "facts" in userText:
        s = get_fact()
    return s
if __name__ == "__main__":
    run_simple('localhost', 5000, app, use_reloader=True, use_debugger=True, use_evalex=True)