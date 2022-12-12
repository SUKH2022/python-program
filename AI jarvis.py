import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

#sapi5= is used for getting voices from the computer or get an API
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#To get voices from the computer below mention expression is used
# or if you want male or female voice then voices[1]/[0] is used. 
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wish us using speak function 
def wishMe():
    hour= int(datetime..datetime.now().hour) #int function is giving hour from 1 to 24.
    if hour>=0 and hour<12:
        speak("Good Morning!..")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!..")

    else:
        speak("Good Evening!..")

    speak("I am Jarvis Ma'am. Kindly tell me how may i help you.")

def takeCommand():
    '''It takes microphone input from the user and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        
        #seconds of non-speaking audio before a phrase is considered complete.
        r.pause_threshold = 1 

        # all these are from speak recognition module
        audio=r.listen(source)
    try:
        print("Recognizing ....")
'''speech recognition in Python to convert the spoken 
words into text, make a query or give a reply. You can 
even program some devices to respond to these spoken words.'''
        
        query=r.recognize.google(audio, language='en-in')
        print("User said: {query}\n")
'''An exception is an event, which occurs during the execution 
of a program that disrupts the normal flow of the 
program's instructions. In general, when a Python script 
encounters a situation that it cannot cope with, 
it raises an exception. An exception is a Python object 
that represents an error.
'''
    except Exception  as e:
        #print(e)
        print("Say that again please...") 
        return "None" 
    return query

def sendEmail(to, content):
           

if __name__--"_main_":
    #speak("Simar is a good girl")
    wishMe()
    while True:
    query = takeCommand().lower()

    #logic for executing tasks based on query
    if 'wikipedia' in query:
        speak("Searching Wikipedia....")
        query= query.replace("wikipedia","")
        results=wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

     elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        #webbrowser.open("spotify.com")
        music_dir='D\\Non Critical\\songs\\favorite Songs2'
        song=os.listdir(music_dir)
        print(songs)
        # we can use random module here for song no.
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'the time ' in query:
          strTime= datetime.datetime.now().strftime("%H:%M:%S")
          print(strTime)
          speak(f"Ma'am, The time is {strTime}")

    elif 'open Vs code' in query:
        codePath= "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

#we canmake a dictionary of name and email in here to send 
# email to everyone according to name 
    elif 'email to simar' in query:
        try:
            speak("What should i say? ")
            content=takeCommand()
            to = "harryyourEmail@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!..")
        except Exception as e:
            print(e)
            speak("Sorry my friend. I am not able to send the email.")