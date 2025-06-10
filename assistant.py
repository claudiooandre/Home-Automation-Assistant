import pyttsx3
import speech_recognition as sr
from controller import handle_command

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except:
            return ""

def main():
    speak("Smart home assistant activated. Say a command or type it.")
    while True:
        try:
            mode = input("Choose mode [voice/text/exit]: ").strip().lower()
            if mode == "voice":
                command = listen()
            elif mode == "text":
                command = input("Enter command: ").strip()
            elif mode == "exit":
                speak("Shutting down. Goodbye!")
                break
            else:
                speak("Invalid mode.")
                continue

            if command:
                response = handle_command(command)
                speak(response)

        except KeyboardInterrupt:
            speak("Interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main()
