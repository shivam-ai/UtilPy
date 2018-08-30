## ! pip install pyttsx3
## ! pip install gTTS
import os
import sys
import pyttsx3
from gtts import gTTS

def pytts(text):
    engine= pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def gtt(text):
    tts= gTTS(text= text, lang='en')
    tts.save('shivam_say.mp3')
    os.system('shivam_say.mp3')











if __name__=='__main__':
    text= "Hello Shivam, kya haal chal hai"
    pytts(text)
    gtt(text)