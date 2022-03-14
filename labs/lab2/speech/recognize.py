#!/usr/bin/env python3
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('listening ... ',end='',flush=True)
    audio = r.listen(source, timeout=5)
    print('done listening')
try:
    print("google recognizes:\n" + r.recognize_google(audio))
except sr.UnknownValueError:
    print("google unknown value error")
except sr.RequestError as e:
    print(f'error: {e}')
