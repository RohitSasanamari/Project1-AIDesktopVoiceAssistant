import audioop
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your personal assistant. Please let me know how may I assist you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print("You said: {}".format(query))
    except Exception as e:
        print("I didn't quite catch you. Can you please say that again..")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {time}")
            speak("Sir, the time is {}".format(time))
        elif 'open youtube' in query:
            print("Opening YouTube..")
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            print("Opening Google...")
            webbrowser.open("https://www.google.com/")
        elif 'open amazon prime' in query:
            print("Opening Amazon Prime...")
            webbrowser.open("https://www.primevideo.com/ref=av_auth_return_redir")
        elif 'open hotstar' in query:
            print("Opening Hotstar...")
            webbrowser.open("https://www.hotstar.com/in")
        elif 'open gmail' in query:
            print("Opening Gmail...")
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
        elif 'open hackerrank' in query:
            print("Opening Hackerank...")
            webbrowser.open("https://www.hackerrank.com/dashboard")
        elif 'open leetcode' in query:
            print("Opening Leetcode...")
            webbrowser.open("https://leetcode.com/")
        