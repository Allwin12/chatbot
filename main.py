from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
import speech_recognition as sr
import sys
import pyttsx3

#gets audio

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)

#converts speech to text
    
speech = r.recognize_google(audio)
print(speech)


bot = ChatBot('Test')
bot.set_trainer(ListTrainer)
for _file in os.listdir('database'):
    chats=open('database/'+_file,'r').readlines()
    bot.train(chats)


request = speech
f=open("db.txt","a+")
f.write(request+'\n')
f.close()

f=open("db.txt","r")
contents=f.readlines()
f.close()


response = bot.get_response(request)
print(response)

#convert text back to speech

engine = pyttsx3.init()
engine.say(response)
engine.runAndWait()
