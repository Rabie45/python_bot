import pyttsx3
import speech_recognition as sr
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #female sound
def take_comand(listener,sr):
    try:
        with sr.Microphone() as source:
            print('hmm,,,Iam hearing u')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            if command == 'April':
                command = "how can i help u"
                return command
            elif 'April' in command:
                command = command.replace('April ', '')
                return command

            else:
                print('i can hear u')



    except:
        print('I can hear u')
def talk(text):#say the string
    engine.say(text)
    engine.runAndWait()