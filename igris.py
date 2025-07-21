import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import subprocess
import time

# --- Configuration ---
spotify_path = r"C:\Users\user\OneDrive\New folder\OneDrive\Desktop\Spotify.lnk"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
wake_words = ["arise", "hey igris", "igris", "wake up igris", "wake up"]
# --- Initialize recognizer and TTS engine ---
recognizer = sr.Recognizer()
tts = pyttsx3.init()
voices = tts.getProperty('voices')

# Set male voice
for voice in voices:
    if "male" in voice.name.lower():
        tts.setProperty('voice', voice.id)
        break

def speak(text):
    print(f"IGRIS: {text}")
    tts.say(text)
    tts.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio).lower()
        print(f"You: {query}")
        return query
    except sr.UnknownValueError:
        print("IGRIS: Couldn't understand.")
        return ""
    except sr.RequestError:
        print("IGRIS: Network error.")
        return ""

def open_browser():
    subprocess.Popen([chrome_path])

def open_youtube():
    webbrowser.get(f'"{chrome_path}" %s').open("https://www.youtube.com")

def search_youtube():
    speak("What do you want to search on YouTube?")
    query = listen()
    if query:
        webbrowser.get(f'"{chrome_path}" %s').open(f"https://www.youtube.com/results?search_query={query}")

def open_spotify():
    os.startfile(spotify_path)

def play_spotify_song():
    speak("Which song should I play on Spotify?")
    song = listen()
    if song:
        webbrowser.get(f'"{chrome_path}" %s').open(f"https://open.spotify.com/search/{song}")

def close_app(app_name):
    try:
        os.system(f"taskkill /f /im {app_name}")
        print(f"IGRIS: Closed {app_name}")
    except Exception as e:
        print(f"Error closing {app_name}: {e}")

# --- Start IGRIS ---
print("IGRIS is booting...")
speak("IGRIS is online. Awaiting your command.")

while True:
    text = listen()
    if any(wake in text for wake in wake_words):
        speak("I am listening. What's your command?")
        while True:
            command = listen()

            if "open browser" in command:
                open_browser()

            elif "open youtube" in command:
                open_youtube()

            elif "search youtube" in command:
                search_youtube()

            elif "open spotify" in command:
                open_spotify()

            elif "play" in command and "on spotify" in command:
                play_spotify_song()

            elif "close spotify" in command:
                close_app("Spotify.exe")

            elif "close browser" in command or "close chrome" in command:
                close_app("chrome.exe")

            elif "go to sleep" in command:
                speak("Good night, master.")
                break
