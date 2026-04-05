import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia

# initialize
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except:
            speak("Sorry, I didn't catch that")
            return ""

def process_command(command):
    if "hello" in command:
        speak("Hello Ronit! How can I help you?")
    
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")
    
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open my github profile" in command:
        webbrowser.open("https://www.github.com/Ronit049")
        speak("Opening Your github profile Ronit")
    
    elif "open my Twitter profile" in command:
        webbrowser.open("https://x.com/its_rsr04")
        speak("Opening your twitter profile")

    elif "search" in command:
        speak("What should I search?")
        query = listen()
        webbrowser.open(f"https://www.google.com/search?q={query}")
    
    elif "wikipedia" in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    
    elif "exit" in command:
        speak("Goodbye!")
        exit()

# main loop
speak("Voice assistant started")

while True:
    command = listen()
    process_command(command)