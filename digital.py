import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

wikipedia.set_lang("pt")

engine = pyttsx3.init("sapi5")
engine.setProperty('voice', engine.getProperty("voices")[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconhecendo...")
        command = r.recognize_google(audio, language='pt-br')
        print("Usuário falou: " + command + "\n")
    except Exception as e:
        print(e)
        speak("Eu não entendo")
        return "None"
    return command

if __name__ == '__main__':
    speak("Assistente Digital foi ativada")
    speak("Olá! Como eu posso te ajudar?")

    while True:
        command = get_command().lower()
        if 'wikipédia' in command:
            speak("Procurando na Wikipedia ...")
            command = command.replace("Wikipédia","")
            command = command.replace("Procure na","")
            command = command.replace("Pesquise na","")
            results = wikipedia.summary(command, sentences=2)
            speak("De acordo com a Wikipédia")
            speak(results)
        elif 'está tudo bem' in command:
            speak("Olá amigo, eu vou bem, obrigado por perguntar")
        elif 'tchau' in command:
            speak("Tchau, até mais")
            exit(0)