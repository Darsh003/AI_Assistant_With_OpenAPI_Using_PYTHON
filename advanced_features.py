import webbrowser as web
import os
import pyttsx3
import pywhatkit
import keyboard
import pyjokes
import speech_recognition as command
import pyautogui
from requests import get
import openai
from config import Api_Key

def Respond(audio) :
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[4].id)
    engine.setProperty('rate',160)
    print("FRIDAY :  ",audio)
    engine.say(audio)
    engine.runAndWait()

def Take_Order():
    order = command.Recognizer()
    with command.Microphone() as source :
        print(": Listning .....")
        order.pause_threshold = 1.07
        audio = order.listen(source)

    try:
        print(": recognizing . . . . . ")
        Eng_query = order.recognize_google(audio, language='en-in')
        # print(f"user said : {Eng_query}\n")
    
    except Exception as e :
        print("can you repeat it please ..... ")
        return "None"
    return Eng_query.lower()

def YT_search(term) :
    Respond("here's what i found from youtube")
    result = "https://www.youtube.com/results?search_query=" + term
    web.open_new_tab(result)

def openapps(name) :

    if 'code' in name :
        Respond('opening V S Code . . . ')
        path="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)

    elif 'spotify' in name :
        Respond('opening Spotify')
        path="C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.206.863.0_x86__zpdnekdrzrea0\\spotify.exe"
        os.startfile(path)

    # elif 'whatsapp' in name :
    #     Respond('opening whatsapp')
    #     path=""
    #     os.startfile(path)

    elif 'telegram' in name :
        Respond('opening telegram')
        path="C:\\Program Files\\WindowsApps\\TelegramMessengerLLP.TelegramDesktop_4.6.3.0_x64__t4vj0pshhgkwm\\telegram.exe"
        os.startfile(path)
    
    elif 'chrome' in name :
        Respond('opening chrome')
        path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(path)

    elif 'word' in name :
        Respond("opening word ...")
        path="C:Program Files\\Microsoft Office\\root\\Office16\\winword.exe"
        os.startfile(path)

    elif 'excel' in name :
        Respond("opening excel . . .")
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\excel.exe"

    elif 'edge' in name :
        Respond('opening m s edge')
        path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(path)

    elif 'powerpoint' in name :
        Respond("opening power point")
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\powerpnt.exe"
        os.startfile(path)

def news() :
    Respond("wait a second sir !")
    URL = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=124fa55dbd7249a99c051baa8df1efa4"
    news = get(URL).json()
    articles = news["articles"]
    head= []
    count = ['first','second','third','fourth','fifth','sixth','seventh','eight','ninth','tenth']
    for ar in articles :
        head.append(ar["title"])
    for i in range (len(count)) :
        Respond(f"today's {count[i]} news is : {head[i]}")
    
def google_search(term) :
    Respond("searching google")
    term = term.replace("search","")
    term = term.replace("from google"," ")
    term = term.replace("on google","")
    pywhatkit.search(term)

def music(term) :
    Respond("playing from Youtube")
    term = term.replace("play","")
    term = term.replace("on youtube","")
    term = term.replace("from youtube","")
    pywhatkit.playonyt(term)

def closeapps(term):
    Respond("ok sir, wait a second")
    if 'code' in term :
        os.system("TASKKILL /F /im Code.exe")

    elif 'spotify' in term :
        os.system("TASKKILL /F /im spotify.exe")

    elif 'telegram' in term :
        os.system("TASKKILL /F /im telegram.exe")

    elif 'chrome' in term :
        os.system("TASKKILL /F /im chrome.exe")

    elif 'word' in term :
        os.system("TASKKILL /F /im winword.exe")

    elif 'excel' in term :
        os.system("TASKKILL /F /im excel.exe")

    elif 'powerpoint' in term :
        os.system("TASKKILL /F /im powerpnt.exe")

    elif 'edge' in term :
        os.system("TASKKILL /F /im msedge.exe")

def yt_auto(term):
    Respond('okay!!!')
    if "pause" in term :
        keyboard.press('space bar')
    elif "play" in term :
        keyboard.press('space bar')
    elif "restart" in term :
        keyboard.press('0')
    elif "replay" in term :
        keyboard.press('0')
    elif "mute" in term :
        keyboard.press('m')
    elif "skip" in term :
        keyboard.press('l')
    elif "back" in term :
        keyboard.press('j')
    elif "full screen" in term :
        keyboard.press('f')

def jokes():
    joke=pyjokes.get_joke()
    Respond(joke)

def take_ss():
    Respond("okay! , what should I name the image ")
    name=Take_Order()
    extension = name + ".png"
    take_ss=pyautogui.screenshot()
    path = "C:\\FRIDAY\\screenshot\\"+extension
    take_ss.save(path)
    os.startfile("C:\\FRIDAY\\screenshot\\")
    Respond("your screen shot sir .  .")

def Ai(Prompt) :
    openai.api_key = Api_Key
    result = f"AI Response For Prompt - {Prompt}\n------------------------------------------------------\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=Prompt,
        temperature=1,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    result += response["choices"][0]["text"]
    if not os.path.exists("AI_response"):
        os.mkdir("AI_response")
    with open(f"AI_response\\prompt - {Prompt[0:31]}.txt","w") as f:
        f.write(result)
    path = "C:\\FRIDAY\\AI_response\\"+"prompt - "+Prompt[0:31]+".txt"
    os.startfile(path)
    try :
        return (response["choices"][0]["text"])
    except Exception as e :
        return ("sorry sir i cant do this . . . ")
