#!/usr/bin/env python3
import asyncio
import speech_recognition as sr
from time import sleep


# class VoiceIface:
#     def __init__(self):
#         self.r = sr.Recognizer()
#         self.r.dynamic_energy_threshold = False
#         self.heard_william = False
#
#     async def listen(self):
#         print('begin listen function')
#         with sr.Microphone() as source:
#             print('listening ... ', flush=True)
#             audio = self.r.listen(source, timeout=5)
#             print('done listening')
#         try:
#             heard = self.r.recognize_google(audio)
#         except sr.UnknownValueError:
#             heard = None
#         if heard:
#             heard = heard.lower()
#             if heard.find('william') and not self.heard_william:
#                 self.heard_william = True
#         else:
#             print('nothing heard')
#
#     def said_william(self):
#         if self.heard_william:
#             print('you said william')
#             self.heard_william = False
#         else:
#             print('you did not hear william')


async def foo():
    sleep(2)
    print('foo')


async def main():
    # v = VoiceIface()
    while True:
        print('loop')
        # v.listen()  # blocks
        task = await asyncio.create_task(foo())
        print('done loop')
        print()
        # v.said_william()


asyncio.run(main())

'''
what i want the output to look like

loop
done loop
loop
done loop
...
foo
'''
