import os
import json
import requests
import speech_recognition as sr


class Recognition:
    def __init__(self, lang="fr-FR"):
        self.lang=lang

    def totext(self, voice):
        filename = voice.filename
        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language=self.lang)
        return [True, {"text": text}, None]
