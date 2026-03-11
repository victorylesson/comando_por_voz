print("testando...")

import speech_recognition as sr

import os

import sys

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)

        print("Diga alguma coisa: ")

        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        frase = frase.lower()

        print("Você disse:", frase)

        if "navegador" in frase:
            os.system("start chrome.exe")

        elif "excel" in frase:
            os.system("start excel.exe")

        elif "powerpoint" in frase:
            os.system("start powerpnt.exe")

        elif "fechar" in frase:
            sys.exit()

    except sr.UnknownValueError:
        print("Não entendi o que você disse")


while True:
    ouvir_microfone()