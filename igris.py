import speech_recognition as sr
import pyttsx3
import time
import os

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
tts = pyttsx3.init()

# Configure TTS voice (optional, can be customized)
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[0].id)  # Use voices[1] for female voice
tts.setProperty('rate', 150)

def speak(text):
    print("IGRIS:", text)
    tts.say(text)
    tts.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("I'm having trouble connecting.")
            return ""

def handle_command(command):
    if "open browser" in command:
        speak("Opening browser.")
        os.system("start chrome")
    elif "what time is it" in command or "tell me the time" in command:
        current_time = time.strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "exit" in command or "goodbye" in command:
        speak("Goodbye, summoner.")
        exit()
    elif command:
        speak("I didn't understand that.")

# Greet the user
speak("IGRIS activated. Awaiting your command.")

# Main loop
while True:
    command = listen()
    handle_command(command)
