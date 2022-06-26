from neuralintents import GenericAssistant
from numpy import rec
import speech_recognition
import pyttsx3 as tts


recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

listOfActivities = ["Register to Events", "Download Gated Content", "Show me articles"]

def registerEvents():
    global recognizer

    speaker.say("which event do you want to register?")
    speaker.runAndWait()

    done = False
    
    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                register = recognizer.recognize_google(audio)
                register = register.lower()

                speaker.say(f"Please provide your consent to register {register} , say yes")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                consentProvided = recognizer.recognize_google(audio)
                consentProvided = consentProvided.lower()

                if consentProvided == 'yes':
                   speaker.say(f"Heyy!! You have been registered to the event {register}. Looking forward")
                   speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("apologies, please repeat")
            speaker.runAndWait()


def hello():
    speaker.say("Hello. What can i do for you?")
    speaker.runAndWait()

def quit():
    speaker.say("Bye")
    speaker.runAndWait()
    exit()


    
mappings = { "greeting": hello,
        "events": registerEvents,
        "exit": quit
        }

def Take_query():
    global recognizer
    assitant = GenericAssistant('learn.json', intent_methods=mappings)
    assitant.train_model()

    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                message = recognizer.recognize_google(audio)
                message = message.lower()

            assitant.request(message)
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()

    
if __name__ == '__main__':
# main method for executing
# the functions
    Take_query()

