import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import jokes


recogniser=sr.Recognizer()
engine= pyttsx3.init()

# function to browse music from library
def playMusic(call):
    if "play" in call.lower():
        sound=call.split(" ")[1]
        link=musicLibrary.music(sound)
        webbrowser.open(link)
        
        print("command:",call)
        


#function to process browsing command 
def processcommand(call):
    if "open google" in call.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in call.lower():
        webbrowser.open("https://youtube.com")
    elif "open discord" in call.lower():
        webbrowser.open("https://discord.com/channels/1126177173812809770/1126561882266943568")
    elif "open music" in call.lower():
        webbrowser.open("https://music.youtube.com/")
        
    print("command:",call)
    

        
    
    

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
def jokescommand(call):
    if "tell me a joke" in call.lower():
        speak(jokes.speakJokes())

    

    
if __name__ =="__main__":
    speak("welcome home....")
    # listen to the wakek word jarvis
    # obtain audio from the microphone
    while True:
        r = sr.Recognizer()

        # Reading Microphone as source
        # listening the speech and store in audio_text variable
        
        print("Recognizing......")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio_text=r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio_text)
            if(word.lower()=="chiku"):
                speak("yess boss...")
                # Listening for command
                with sr.Microphone() as source:
                    print("chiku active....")
                    audio_text=r.listen(source)
                    call=r.recognize_google(audio_text)
                    
                    processcommand(call)
                    jokescommand(call)
                    playMusic(call)
        except Exception as e:
            print("Error; {0}".format(e))
                    
                    
         