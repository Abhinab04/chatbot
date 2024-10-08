import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
#from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import sounddevice as sd
import numpy as np
import vosk
import json
#from win10toast import ToastNotifier
import os
class initialization:
    def data(self):
        global transai, trans, transweb, transapp, command
        while not command:
            try:
                print("listening...")
                audio=sd.rec(int(16000 * 5), samplerate=16000, channels=1, dtype='int16')
                sd.wait()
                audio=np.squeeze(audio)
                audio_bytes=audio.tobytes()  
                if recognizer.AcceptWaveform(audio_bytes):
                    result=json.loads(recognizer.Result())
                    command=result.get("text", "")
            except Exception as e:
                print(f"Error: {e}")
        print(command)
        if "stop" in command:
            trans="stop"
        elif ("who are you" in command 
        or "who build you?" in command 
        or "who have build you" in command 
        or "who created you" in command 
        or "what can you do for me" in command
        or "what is your name" in command
        or "hey cleo" in command 
        or "hey clear" in command):
            trans=command
            command=""
            p=chitchat()
            p.non_AI()
        elif "weather" in command:
            p=other_applications()
            command=""
            p.weather()
        elif (((("launch" in command and ("in chrome" in command or "in web" in command)) or ("open" in command and ("in chrome" in command or "in web" in command))) 
        and ("how to" not in command and "what to" not in command and "where to" not in command)) or 
        (("search" in command or "search for" in command or "look for" in command) and 
        ("how to" not in command and "what to" not in command and "where to" not in command))):
            transweb=command
            command=""
            p=other_applications()
            p.webwork()
        elif (("launch" in command or "open" in command) 
        and ("how to" not in command and "what to" not in command and "where to" not in command)):
            transapp=command
            command=""
            p=other_applications()
            p.system_work()
        elif cleo_check:
            count=0
            transai=command
            command=""
            if count>0:
                return transai
            count+=1
            p=chitchat()
            p.AI()
    def data_To_Non_ai(self):
        if trans:
            return trans
    def data_To_ai(self):
        if transai:
            return transai
    def data_To_Web(self):
        if transweb:
            return transweb
    def data_To_System(self):
        if transapp:
            return transapp
class chitchat:
    def non_AI(self):
        global cleo_check
        a=initialization()
        datas=a.data_To_Non_ai()
        if "hey cleo" in datas or "hey clear" in datas:
            cleo_check=True
            a.data()
        elif cleo_check:
            if "who are you" in datas or "what is your name" in datas:
                self.non_AI_10(
                    'My name is cleopatra, Your personal assistant, you can just call me cleo, I am very pleased to meet you. Just say "hey cleo" and I will answer your call'
                )
            elif "who build you" in datas or "who have build you" in datas or "who created you" in datas:
                self.non_AI_10(
                    "x Bastille and Osirusss has created me. They're both computer science student. X Bastille is currently pursuing Artificial intelligence and Machine learning whereas osirusss is currently pursuing Web development."
                )
            elif "what can you do for me" in datas:
                self.non_AI_10(
                    "here are the things I can do for you:-\n1: I can be your personal AI language model assistant\n2: I can tell you the weather\n3: I can open apps on your desktop but make sure you call by it's exe file name, otherwise the AI won't catch the app that you requested.\n4: I can search, open websites in the web.\nJust say 'hey cleo' and I will answer your call"
                )
            engine.say("So. What can I help you with?")
            engine.runAndWait()
    def non_AI_10(self, arg0):
        self.AI_2(arg0)     
    def AI(self):
        if cleo_check:
            a=initialization()
            datas=a.data_To_ai()
            print("Generating responese...")
            genai.configure(api_key="AIzaSyCkHKFFUiSL6vLGr4gpDL6tWSljnYVFkiE")
            model=genai.GenerativeModel("gemini-pro")
            response=model.generate_content(datas)
            l=response.text.split("*")
            t="".join(l)
            self.AI_2(t)
            engine.say("Is there anything else that I can help you with?")
            engine.runAndWait()
    def AI_2(self, arg0):
        print(arg0)
        engine.say(arg0)
        engine.runAndWait()
class other_applications:
    def weather(self):
        if cleo_check:
            a=initialization()
            #n=ToastNotifier()
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            r=requests.get("https://weather.com/en-IN/weather/today/l/68509ddcc58030eeb09cd5130641916746139e9174ab3527650e99b108d95ed9", headers=headers)
            soup=BeautifulSoup(r.text, "html.parser")
            current_info1=str(soup.find("div", class_="CurrentConditions--header--kbXKR").get_text())
            current_info2=str(soup.find("span", class_="CurrentConditions--tempValue--MHmYY").get_text())
            current_info3=str(soup.find("div", class_="CurrentConditions--phraseValue--mZC_p").get_text())
            current_info4=str(soup.find("div", class_="CurrentConditions--tempHiLoValue--3T1DG").get_text())
            l=current_info4.split("•")
            res=(f"{current_info1}\n{current_info2}\n{current_info3}\n{current_info4}")
            engine.say("WEATHER UPDATE")
            engine.say(f"{current_info1}\nCurrent temperature is {current_info2}\nIt's {current_info3} today\ntemperature duing day is {l[0]} and during night is {l[1]}")
            engine.runAndWait()
            #n.show_toast("WEATHER UPDATE", res, duration=10)
            engine.say("Is there anything else that I can help you with?")   
            engine.runAndWait()
    def webwork(self):
        if not cleo_check:
            return
        a=initialization()
        wish=a.data_To_Web()
        l=wish.split(" ")
        #if "open" in wish or "launch" in wish:
            #self.webwork_7(l)
        #else:
            #self.webwork_16(l)
    def webwork_16(self, l):
        wish=" ".join(l[2:])
        engine.say(f"searching for {wish} in web")
        engine.runAndWait()
        wish=wish.replace(" ", "+")
        browser=webdriver.Chrome()
        browser.implicitly_wait(1)
        browser.maximize_window()
        browser.get(f"https://www.google.com/search?q={wish}&start=0")
        while True:
            pass
    def webwork_7(self, l):
        l.pop()
        l.pop()
        wish="".join(l[1:])
        browser=webdriver.Chrome()
        browser.maximize_window()
        browser.get(f"https://www.{wish.lower()}.com/")
        engine.say(f"opening {browser.title}")
        engine.runAndWait()
        while True:
            pass
    def system_work(self):
        if not cleo_check:
            return
        a=initialization()
        wish=a.data_To_System()
        wish="".join(wish.split(" ")[1:])
        engine.say(f"opening {wish}")
        engine.runAndWait()
        paths=(r"C:\Users", r"C:\Program Files", r"C:\Program Files (x86)", r"D:", r"E:")
        for path in paths:
            for root, dirs, files in os.walk(path):
                for name in files:
                    if name.lower()==f"{wish.lower()}.exe":
                        os.startfile(os.path.join(root, name))
                        while True:
                            pass
print('say "hey cleo"')
cleo_check=False
command=""
'''r=sr.Recognizer() 
mic=sr.Microphone()'''
engine=pyttsx3.init()
model = vosk.Model("model")  
recognizer = vosk.KaldiRecognizer(model, 16000)
voice=engine.getProperty("voices")
rates=engine.getProperty("rate")
engine.setProperty("voice", voice[1].id)
engine.setProperty("rate", rates-50)
def process_input():
    al=initialization()
    al.data()
if __name__=="__main__":
    process_input()
