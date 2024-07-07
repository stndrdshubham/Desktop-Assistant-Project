import pyttsx3
import speech_recognition as sr
import datetime


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

#takeCommand function
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
            query=r.recognize_google(audio, language="en-in")   #hi for hindi recognition
            print(f"user said: {query}\n")

        except Exception as e:
            print("say that again please ...")
            return "None"
           


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