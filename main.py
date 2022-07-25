import requests,time
import json
from re import search
from tkinter import messagebox
import threading
import sounddevice as sd
import soundfile as sf
from win32gui import ShowWindow,GetForegroundWindow
from win32con import SW_HIDE
import subprocess
ShowWindow(GetForegroundWindow(),SW_HIDE)
def siren():
    filename = 'siren.wav'
    data, fs = sf.read(filename, dtype='float32')  
    while 1:
        sd.play(data, fs)
        status = sd.wait()
def Obligation():
    link="https://www.reddit.com/user/ObligationNo5291/submitted.json"
    get=requests.get(link, headers = {"User-Agent": "GibMeFree"})
    post=get.json()['data']['children'][0]['data']
    content=post["selftext"]
    list1=[]
    if not content=="[removed]":
        a=str(content).strip()
        list1.append(bool(search("voucher",a)))
        list1.append("1")
        list1.append(content)
        list1.append(post["url"])
    else:
        list1.append(False)
        list1.append("0")
    return list1
    
def main():
    level=0
    while True:
        list1=Obligation()
        if list1[0]==True:
            level+=1
        if list1[1]=="1":
            level+=1
        if level>0:
            if level==2:
                threading.Thread(target=siren).start()
                messagebox.showerror('CRITICAL ALERT', f'FREE VOUCHER AVAILABLE\n {list1[3]}')
                url=list1[3]
                print(url)
                subprocess.Popen([r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', url]).wait()
                exit()
            else:
                messagebox.showerror('normal alet', 'free voucher might be available')
                url=list1[3]
                print(url)
                subprocess.Popen([r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', url]).wait()
        level=0
        time.sleep(2)
if __name__ == "__main__":
    main()
