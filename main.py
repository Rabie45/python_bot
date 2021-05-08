
import speech_recognition as sr
import pyttsx3
import pywhatkit as pk
import pyjokes as pj
import wikipedia
import datetime as dt
import youtube_test
import takeLine

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #female sound
mediaObj = ''


def talk(text):#say the string
    engine.say(text)
    engine.runAndWait()


def inti():
    while True:
        cmd = takeLine.take_comand(listener, sr)  # take the commend from the mic
        if cmd is None:
            print('sleeping')
            pass
        elif cmd == 'how can i help u':
           talk(cmd)
        elif 'play' in cmd:
            song = cmd.replace('play ', '')
            print(song)
            linkSong = youtube_test.takeSong(song) # get the link
            mediaObj = youtube_test.URL(linkSong) # play
            print('playing ' + song)
            talk('playing ' + song)
        elif 'joke' in cmd: # tell me a joke
            joke = pj.get_joke()
            print(joke)
            talk(joke)
        elif 'who is' in cmd:
            name = cmd.replace('who is', '')
            info = wikipedia.summary(name)
            print(info)
            talk(info)
        elif 'time' in cmd:
            time = dt.datetime.now().strftime('%I:%M %p')
            talk(' the time is ' + time)
        elif 'stop' in cmd:
            mediaObj.stop()
        elif 'pause' in cmd:
            mediaObj.pause()
        elif 'continue' in cmd:
            mediaObj.play()
        elif 'volume up' in cmd:
            a = mediaObj.audio_get_volume()
            print(a)
            youtube_test.volumeUp(mediaObj, a)
        elif 'volume down' in cmd:
            a = mediaObj.audio_get_volume()
            print(a)
            youtube_test.volumeDown(mediaObj, a)

        elif 'mute' in cmd:
            youtube_test.mute(mediaObj)
            # youtube_test.volume_up(mediaObj)
        else:
            print('fine')


inti()
