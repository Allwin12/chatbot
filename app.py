import os
from flask import Flask, render_template, request
from flask import jsonify
from chatterbot import ChatBot
import speech_recognition as sr
import sys
import pyttsx3
from chatterbot.trainers import ListTrainer


app = Flask(__name__)


bot = ChatBot('New')
bot.set_trainer(ListTrainer)
for _file in os.listdir('database'):
    chats=open('database/'+_file,'r').readlines()
    bot.train(chats)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/get")
def get_bot_response():

    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    speech = r.recognize_google(audio)    
    userText = speech
    engine = pyttsx3.init()
    engine.say(str(bot.get_response(userText)))
    engine.runAndWait()
    return jsonify(
        bot = str(bot.get_response(userText)),
        user = str(userText),
        )


if __name__ == "__main__":
    app.run()
