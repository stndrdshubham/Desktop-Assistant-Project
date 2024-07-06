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
  

  #Speech Recognition function
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
           

text=takeCommand()
speak(text)
