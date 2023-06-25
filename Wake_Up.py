import speech_recognition as command
import os
import keyboard

def Take_Order():
    order = command.Recognizer()
    with command.Microphone() as source :
        print(": Listning .....")
        # order.pause_threshold = 0.8
        audio = order.listen(source)

    try:
        print(": recognizing . . . . . ")
        Eng_query = order.recognize_google(audio, language='en-in')
        # print(f"user said : {Eng_query}\n")
    
    except Exception as e :
        print("can you repeat it please ..... ")
        return "None"
    return Eng_query.lower()



while True :
    word=Take_Order()

    if "friday" in word :
        path = "C:\\FRIDAY\\main.py"
        os.startfile(path)
        break

    elif "close" in word :
        break

    elif "quit" in word :
        break


