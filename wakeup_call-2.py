import speech_recognition as sr
import time


wake_words = ["wake up igris", "arise", "wake up, daddy's home", "wake up"]


recognizer = sr.Recognizer()
mic = sr.Microphone()

print("Welcome, say the password...")

with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    while True:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")

            if any(word in command for word in wake_words):
              
                print("✅ Password accepted.")
                print("🟢 WAKING UP…")
                time.sleep(5)
                break
            else:
                print("❌ Command not recognized as wake word.")

        except sr.UnknownValueError:
            print(" Couldn't understand. Try again.")
        except sr.RequestError:
            print(" Could not connect to recognition service.")
