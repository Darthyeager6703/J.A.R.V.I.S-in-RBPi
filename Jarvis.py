import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import pyaudio
from jarvis import Whatsapphelper
from jarvis import Mailhelper
from jarvis import YTmusicHelper
from jarvis import YTVideoHelper
from flask_socketio import SocketIO

socketio = SocketIO()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Good Morning!")
        speak("Good Morning!")

    elif 12 <= hour < 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("I am Jarvis Sir. Please tell me how may I help you")
    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    query = ""  # Set an initial value for query

    with sr.Microphone() as source:
        socketio.emit('update_message',{'message': "Listening..."})
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        socketio.emit('update_message',{'message': "Recognizing..."})
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        socketio.emit('update_message',{'message': f"User said: {query}"})
        print(f"User said: {query}\n")

        if 'do a task' in query.lower():
            wishMe()
            HEART()

    except Exception as e:
        socketio.emit('update_message',{'message': "Say that again please..."})
        print("Say that again please...")
        # continue (You don't need 'continue' here)

    return query

def HEART():
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia...")
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'song' in query:
            print("Which song would you like to play?")
            speak("Which song would you like to play?")
            song_name = takeCommand()
            print("AAAH YES! A good Selection. Let me play that in a sec")
            speak("AAAH YES! A good Selection. Let me play that in a sec")
            YTmusicHelper.play_song(song_name)

        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'open an app' in query:
            print("Which app would you like to open?")
            speak("Which app would you like to open?")
            app = takeCommand()
            os.startfile(app)

        elif 'whatsapp' in query:
            print("Who would you like to message?")
            speak("Who would you like to message?")
            name = takeCommand()
            print("What is the message?")
            speak("What is the message?")
            message = takeCommand()
            Whatsapphelper.sendwhatmsg_instantly(name, message)

        elif 'email' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand()
                print("to whom?")
                speak("to whom?")
                to = takeCommand()
                Mailhelper.sendEmail(to, content)
                # print("Email has been sent!")
                # speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry my friend. I am not able to send this email")
                speak("Sorry my friend. I am not able to send this email")

        elif 'youtuber' in query:
            print("Which youtuber would you like to watch?")
            speak("Which youtuber would you like to watch?")
            youtuber = takeCommand()
            print("OK Sir! Would you like to watch a random video or a specific video?")
            speak("OK Sir! Would you like to watch a random video or a specific video?")
            video_type = takeCommand()
            if "random" in video_type:
                print("OK Sir! Let me find a random video for you")
                speak("OK Sir! Let me find a random video for you")
                YTmusicHelper.play_youtube(youtuber)
            elif "specific" in video_type:
                print("OK Sir! What video would you like to watch?")
                speak("OK Sir! What video would you like to watch?")
                video_name = takeCommand()
                print("OK Sir! Let me find that video for you")
                speak("OK Sir! Let me find that video for you")
                YTVideoHelper.search_video(youtuber, video_name)


        elif 'quit' in query:
            print("Thank you for using me sir")

            speak("Thank you for using me sir")
            break



if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
