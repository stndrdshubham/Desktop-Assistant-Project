import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


#Taking voice from my system
#initialise text to speech library. sapi5 is needed to initialise it. 
# these code are inbuild by developers https://pyttsx3.readthedocs.io/en/latest/engine.html 'pyttsx3 documentation
#to call the voice property from the library call through 'voices'
# OS have inbuild two voices, male and female voices[0],voices[1], call it by printing it.
engine=pyttsx3.init('sapi5')    
voices=engine.getProperty('voices')
print(voices,voices[0].id)
# print(type(voices))

#giving command or setting property for voice to voices[0] which is male voice
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',200)



#Speak function
# defining speak function to speak the text with a variable text and to speak it calling variable 'say' and ending it with runAndWait function
# now the written text is called by defined function speak.
def speak(text):
    """This function takes text and returns voice
    Args:
        text (_type_): string
    """
    engine.say(text)
    engine.runAndWait()

#speak("Hello i am a programmer, how are you?")
  

#Speech Recognition function  https://makeblock-micropython-api.readthedocs.io/en/latest/haloboard/haloboard/speech_recognition/speech_recognition.html
#importing microphine as source
#r.pause_threshold will wait for 1ms b/w speech to avoid the noise in b/w speech and embedded through listen command.
# for recognistion we are using try and except block just to handle the exceptions, to recognize we use google API (there are bunch of other options available) 
def takeCommand():
    """this function will recognize voice & return text
    """
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold=1
        audio = r.listen(source)

        try:
            print("Recognizing ...")
            query=r.recognize_google(audio, language="en-in")
            print(f"user said: {query}\n")

        except Exception as e:
            print("say that again please ...")
            return "None"
           

# text=takeCommand()
# speak(text)

#this function for wish me by using time
def wish_me():
    hour=(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning shubham. How are you doing")

    elif hour>=12 and hour<18:
        speak("Good afternoon shubham. How are you doing")

    else:
        speak("Good evening shubham. How are you doing")

    speak("I am JARVIS. Tell me how can i help you")


if __name__=="__main__":
    
    wish_me()
    while True:
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

    else:
        speak("Opening Youtube")
        webbrowser.open("youtube.com")





