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

def getComando():
    r = sr.Recognizer() # Reconhecendo o áudio
    with sr.Microphone() as source: # Ativando o microfone
        print("Ouvindo o áudio...")
        r.pause_threshold = 1 # Aguardando a pessoa falar
        audio = r.listen(source) # Armazenando o que foi dito
    try:
        print("Reconhecendo o áudio...")
        command = r.recognize_google(audio, language='pt-br')
        print("O usuário falou: " + command + "\n")
    except Exception as e:
        print(e)
        speak("Não entendi")
        return ""
    return command

if __name__ == "__main__":
    speak("Assistente Digital foi ativada")
    speak("Olá! Como eu posso te ajudar?")

    while(True):
        command = getComando().lower()
        if 'wikipedia' in command:
            command = command.replace("wikipédia","")
            command = command.replace("procure na","")
            command = command.replace("pesquise na","")

            results = wikipedia.summary(command, sentences=2)
            speak("De acordo com a Wikipédia")
            speak(results)
