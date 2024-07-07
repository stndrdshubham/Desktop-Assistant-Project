from src.helper import speak, takeCommand, wish_me

import wikipedia
import os
import datetime
import webbrowser
import streamlitas as st



query=takeCommand()
speak(query)

if __name__=="__main__":
    
    wish_me()
    while True:

        st.title("Desktop Assistant System")

        
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query=query.replace('wikipedia', "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "github" in query:
            speak("Opeing Github")
            webbrowser.open("github.com")

        elif "google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif "youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'goodbye' in query:
            speak("ok shubham/ I am always here for you. Bye")
            exit()

             