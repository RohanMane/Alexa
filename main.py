import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    transcription = None
    try :
        with sr.Microphone(device_index=2) as source:
            # print(sr.Microphone.list_microphone_names())
            print("LISTENING....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, show_all=True)
            if command is not None:
                transcription = command.get("alternative")[0].get("transcript").lower()
                if 'alexa' in transcription:
                    # transcription = transcription.replace('alexa', '')
                    print(transcription) 
    except:
        pass
    return transcription

def run_alexa():
    command = take_command()
    print(command)
    if command is not None and 'play' in command and 'alexa' in command:
        song = command.replace('play', '')
        song = song.replace('alexa', '')
        talk('playing '+ song)
        pywhatkit.playonyt(song)
    
    elif command is not None and 'time' in command and 'alexa' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+ time)

    elif command is not None and 'who is' in command and 'alexa' in command: 
        person = command.replace('who is', '')
        person = person.replace('alexa', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif command is not None and 'what is' in command and 'alexa' in command: 
        thing = command.replace('what is', '')
        thing = thing.replace('alexa', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)

    elif command is not None and 'tell me a joke' in command and 'alexa' in command: 
        talk(pyjokes.get_joke())

    elif command is not None and 'alexa' in command and 'stop' in command:
        return True
    
    else:
        talk('Please say the command again')

stop_flag = False 

while not stop_flag:
    stop_flag = run_alexa()