## ! pip install pyttsx3
import pyttsx3
import os
import sys

engine= pyttsx3.init()

engine.say("Hello Shivam, kya haal chal hai?")
engine.runAndWait()