import pyttsx3
import speech_recognition as command
import wikipedia
import webbrowser
import advanced_features as features
import datetime as dt
import os
from requests import get
import keyboard

def StartUp():
    current_time = int(dt.datetime.now().hour)
    if current_time >= 7 and current_time < 10 :
        Respond("Hello Sir!   Good Morning !")
    elif current_time >= 10 and current_time < 12 :
        Respond("Hello Sir!  Good Day !")
    elif current_time >= 12 and current_time < 17 :
        Respond("Hello Sir!  Good Afternoon !")
    elif current_time >=17 and current_time < 20 :
        Respond("Hello Sir!  Good Evening !")
    else :
        Respond("Hello Sir!  Good Night ! ")
    
'''def Startup_hin():
    current_time = int(dt.datetime.now().hour)
    if current_time >= 7 and current_time < 10 :
        Respond_hin(" शुभ प्रभात !")
    elif current_time >= 10 and current_time < 12 :
        Respond_hin(" आपका दिन शुभ हो !")
    elif current_time >= 12 and current_time < 17 :
        Respond_hin(" नमस्कार !")
    elif current_time >=17 and current_time < 20 :
        Respond_hin(" नमस्ते !")
    else :
        Respond_hin(" शुभ रात्रि !")
    
    Respond_hin("मे आपकी पर्सनल सहायक हू")'''

def Respond(audio) :
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[4].id)
    engine.setProperty('rate',160)
    print("FRIDAY :  ",audio)
    engine.say(audio)
    engine.runAndWait()

'''def Respond_hin(audio):
    engine=pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',180)
    print("you said :  ",audio)
    engine.say(audio)
    engine.runAndWait()'''

def Take_Order():
    order = command.Recognizer()
    with command.Microphone() as source :
        print(": Listning .....")
        order.pause_threshold = 1.00
        order.energy_threshold = 500
        audio = order.listen(source)

    try:
        print(": recognizing . . . . . ")
        Eng_query = order.recognize_google(audio, language='en-in')
        # print(f"user said : {Eng_query}\n")
    
    except Exception as e :
        print("can you repeat it please ..... ")
        return "None"
    return Eng_query.lower()

'''def Take_Order_hin():
    order = command.Recognizer()
    with command.Microphone() as source :
        print(": Listning .....")
        order.pause_threshold = 1
        audio = order.listen(source)

    try:
        print(": recognizing . . . . . ")
        Hin_query = order.recognize_google(audio, language='hi-in')
        print(f"user said : {Hin_query}\n")
    
    except Exception as e :
        print("can you repeat it please ..... ")
        return "None"
    return Hin_query'''



if __name__ == "__main__":
    StartUp()
    Respond("how may i help you ?")
    while True :
        query = Take_Order()

        if "wikipedia" in query :
            Respond('searching wikipedia ....')
            search = query.replace("wikipedia", "")
            search = query.replace("friday", "")
            result = wikipedia.summary(search, sentences=2)
            print(result)
            Respond("According to Wikipedia ..... ")
            Respond(result)

        elif "open code" in query :
            features.openapps(query)

        elif "code" in query :
            query = query.replace("friday", "")
            query = query.replace("artificial intelligence", "")
            query = query.replace("using artificial intelligence", "")
            query = query.replace("using ai", "")
            query = query.replace("using", "")
            query = query.replace("a i", "")
            query = query.replace("using a i", "")
            query = query.replace("ai", "")
            Respond("sure sir . . .  ") 
            result = features.Ai(query)
            print(result)

        elif "artificial intelligence" in query:
            query = query.replace("friday", "")
            query = query.replace("artificial intelligence", "")
            query = query.replace("using artificial intelligence", "")
            query = query.replace("using ai", "")
            query = query.replace("using", "")
            Respond("Just a Second . . .  ")
            result = features.Ai(query)
            Respond(result)

        elif " ai " in query:
            query = query.replace("friday", "")
            query = query.replace("using ai", "")
            query = query.replace("using", "")
            query = query.replace("ai", "")
            Respond("Just a Second . . .  ")
            result = features.Ai(query)
            Respond(result)

        elif "a i" in query:
            query = query.replace("friday", "")
            query = query.replace("using", "")
            query = query.replace("using a i", "")
            query = query.replace("a i", "")
            Respond("Just a Second . . .  ")
            result = features.Ai(query)
            Respond(result)

        elif "who are you" in query :
            Respond("I am FRIDAY , your personal assistant. i can do many things like opening and closing apps, searching youtube and google,etc. . based on your commands.")

        elif "tell me something about you" in query :
            Respond("I am FRIDAY , your personal assistant. i can do many things like opening and closing apps, searching youtube and google,etc. . based on your commands.")

        elif "tell me about you" in query :
            Respond("I am FRIDAY , your personal assistant. i can do many things like opening and closing apps, searching youtube and google,etc. . based on your commands.")
        
        elif "what can you do" in query :
            Respond("I am FRIDAY , your personal assistant. i can do many things like opening and closing apps, searching youtube and google,etc. . based on your commands.")

        elif "open youtube" in query :
            Respond("opening   youtube ...")
            webbrowser.open("youtube.com")

        elif "open facebook" in query :
            Respond("opening facebook")
            webbrowser.open_new_tab("facebook.com")

        elif "open instagram" in query :
            Respond("opening instagram ")
            webbrowser.open_new_tab("instagram.com")
        
        elif "time" in query :
            Time = dt.datetime.now().strftime("%I:%M:%S %p")
            Respond(f"Sir, The Time is {Time}")
        
        # elif "open spotify" in query :
        #     features.openapps(query)

        # elif "open telegram" in query :
        #     features.openapps(query)
        
        elif "open chrome" in query :
            features.openapps(query)

        elif "open word" in query :
            features.openapps(query)

        elif "open excel" in query :
            features.openapps(query)

        elif "open edge" in query :
            features.openapps(query)

        elif "open powerpoint" in query :
            features.openapps(query)

        elif "close code" in query :
            features.closeapps(query)
        
        elif "close spotify" in query :
            features.closeapps(query)

        elif "close telegram" in query :
            features.closeapps(query)
        
        elif "close chrome" in query :
            features.closeapps(query)

        elif "close word" in query :
            features.closeapps(query)

        elif "close excel" in query :
            features.closeapps(query)

        elif "close edge" in query :
            features.closeapps(query)

        elif "close powerpoint" in query :
            features.closeapps(query)

        elif "shutdown" in query :
            Respond("okay sir !,signing off")
            os.system("shutdown /s /t 5")

        elif "restart" in query :
            Respond("okay sir !,restarting the system")
            os.system("shutdown /r /t 5")

        elif "from youtube" in query :
            query = query.replace("search","")
            query = query.replace("from youtube","")
            query = query.replace("friday", "")
            features.YT_search(query)

        elif "on youtube" in query :
            query = query.replace("search","")
            query = query.replace("on youtube","")
            query = query.replace("friday", "")
            features.YT_search(query)

        elif "from google" in query :
            query = query.replace("friday", "")
            features.google_search(query)

        elif "on google" in query :
            query = query.replace("friday", "")
            features.google_search(query)

        elif "play" in query :
            features.music(query)

        elif "pause" in query :
            features.yt_auto(query)
                        
        elif "replay" in query :
            features.yt_auto(query)
            
        elif "mute" in query :
            features.yt_auto(query)
            
        elif "skip" in query :
            features.yt_auto(query)
            
        elif "back" in query :
            features.yt_auto(query)
            
        elif "full screen" in query :
            features.yt_auto(query)

        elif "joke" in query :
            Respond("okay!")
            features.jokes()

        elif "screenshot" in query :
            features.take_ss()

        elif "minimize" in query :
            Respond("sure sir!")
            keyboard.press_and_release('windows + down arrow')

        elif "minimise" in query :
            Respond("sure sir!")
            keyboard.press_and_release('windows + down arrow')

        elif "maximize" in query :
            Respond("sure sir!")
            keyboard.press_and_release('windows + up arrow')

        elif "minimise" in query :
            Respond("sure sir!")
            keyboard.press_and_release('windows + up arrow')

        elif "switch window" in query :
            Respond("sure sir!")
            keyboard.press_and_release('alt+tab')

        elif "desktop" in query :
            Respond("okay sir!")
            keyboard.press_and_release('windows + d')

        elif "home screen" in query :
            Respond("okay sir!")
            keyboard.press_and_release('windows + d')

        elif "news" in query :
            features.news()

        elif "thank you" in query :
            Respond("its my pleasure sir")

        elif "thanks" in query :
            Respond("its my pleasure sir")

        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            Respond(f'your IP address is {ip}')

        elif "quit" in query :
            Respond("okay sir!")
            # path = "C:\\FRIDAY\\Wake_Up.py"
            # os.startfile(path)
            break
        
        elif "you need a break" in query :
            Respond("okay sir, you can call me any time")
            # path = "C:\\FRIDAY\\Wake_Up.py"
            # os.startfile(path)
            break

        elif "exit" in query :
            Respond("okay sir, you can call me any time")
            # path = "C:\\FRIDAY\\Wake_Up.py"
            # os.startfile(path)
            break





