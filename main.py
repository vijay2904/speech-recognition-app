import speech_recognition as sr
from kivy.app import App
import webbrowser
import playsound
import os
import time

import random
from gtts import gTTS

from time import ctime


r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            lollipop_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            lollipop_speak('Sorry, I didn\'t get that')
        except sr.RequestError:
            lollipop_speak('Sorry, my sppech service is down')
        return voice_data

def lollipop_speak(audio_string):
    tts = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1, 100000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    if 'what is your name' in voice_data:
        lollipop_speak('My name is Lollipop')
    if 'what time is it' in voice_data:
        lollipop_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        lollipop_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        lollipop_speak('Here is the location ')
    if 'ok bye' in voice_data:
        lollipop_speak('Byeeee have a good day')
        exit()
    if 'what is today' in voice_data:
        lollipop_speak('happy birthday lollipop')


time.sleep(1)
lollipop_speak('How can I help you')
while 1:
    voice_data = record_audio()
    respond(voice_data)