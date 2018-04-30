'''
Title: This is an alarm that perfectly lines up with my sleep schedule
Author: Riley Carpenter
TODO: have the volume get louder when it goes off and quieter afterwards
'''
from pygame import mixer
import time
import os
import sys
import random
import getpass
Hours3 = 5
Minutes3 = 5
endorno = ""
Currenttime = time.ctime()
Hours1 = int(Currenttime[11:13])
Minutes1 = int(Currenttime[14:16])
Seconds = int(Currenttime[17:19])
phrases = ["Wake up Riley!!!!","It's time to wake up it's time to wake up","HEEEEYYY WAKE UP","RILEY RILEY RILEY WAKE UP","1 2 3 4 5 6 7 8 9 it is time to wake up","Riley more alarms are to come UNLESS you get up","OH WHEN SHALL I SEE JESUS you wanna not hear this again? Wake up","I'm so tired of telling you to wake up just wake up","A friend of the devil is somehow who doesn't wake up","Babe babe bae wake up"]
optionalsongs = ["Pink Floyd Time.wav","Alarm2.wav","Alarm3.wav","Alarm4.wav","Alarm5.wav","Alarm6.wav","Alarm7.wav","Alarm8.wav","Alarm9.wav","Alarm10.wav","Alarm11.wav"]
def playsound(soundfile):
    mixer.init()
    mixer.music.load(soundfile)
    mixer.music.play(-1)
def alarmsystem(Hours2, Minutes2):
    Currenttime = time.ctime()
    Hours1 = int(Currenttime[11:13])
    Minutes1 = int(Currenttime[14:16])
    Seconds = int(Currenttime[17:19])
    playsound("Citys Night ambience sounds.wav")
    while Hours1 != Hours2 or Minutes1 != Minutes2:
        Currenttime = time.ctime()
        Hours1 = int(Currenttime[11:13])
        Minutes1 = int(Currenttime[14:16])
        Seconds = int(Currenttime[17:19])
        time.sleep(1)
    else:
        mixer.music.stop()
        print(random.choice(phrases))
        playsound(random.choice(optionalsongs))
        endorno = input("Press enter to stop the music and snooze for 5 minutes or type stop ")
        if endorno == "stop":
            if getpass.getuser() == "rileyball2":
                print("Good morning Riles")
            else:
                print("Good morning",getpass.getuser())
            time.sleep(1)
            sys.exit()
def nexttime():
    Currenttime = time.ctime()
    Hours1 = int(Currenttime[11:13])
    Minutes1 = int(Currenttime[14:16])
    Seconds = int(Currenttime[17:19])
    if Minutes1 >= 55:
        print("The alarm will go off at",Hours1 + 1,":",00)
        Hours3 = Hours1 + 1
        Minutes3 = 0
        alarmsystem(Hours3,Minutes3)
    elif Minutes1 == 10:
        print("The alarm will go off at",Hours1,":",15)
        Hours3 = Hours1
        Minutes3 = 15
        alarmsystem(Hours3,Minutes3)
    else:
        Currenttime = time.ctime()
        Hours1 = int(Currenttime[11:13])
        Minutes1 = int(Currenttime[14:16])
        Seconds = int(Currenttime[17:19])
        if Minutes1 >= 50:
            checkminutes = Minutes1 - 50
        elif Minutes1 >= 40:
            checkminutes = Minutes1 - 40
        elif Minutes1 >= 30:
            checkminutes = Minutes1 - 30
        elif Minutes1 >= 20:
            checkminutes = Minutes1 - 20
        elif Minutes1 >= 10:
            checkminutes = Minutes1 - 10
        else:
            checkminutes = Minutes1
        for i in range(0,10):
            if i < 5 and i == checkminutes:
                timetogo = 5 - i
                Minutes1 = int(Minutes1)
                print("The alarm will go off at",Hours1,":",Minutes1 + timetogo)
                Hours3 = Hours1
                Minutes3 = Minutes1 + timetogo
                alarmsystem(Hours3,Minutes3)
            elif i == 5 and i == checkminutes:
                timetogo = 5
                Minutes1 = int(Minutes1)
                print("The alarm will go off at",Hours1,":",Minutes1 + timetogo)
                Hours3 = Hours1
                Minutes3 = Minutes1 + timetogo
                alarmsystem(Hours3,Minutes3)
            elif i > 5 and i == checkminutes:
                timetogo = 10 - i
                Minutes1 = int(Minutes1)
                print("The alarm will go off at",Hours1,":",Minutes1 + timetogo)
                Hours3 = Hours1
                Minutes3 = Minutes1 + timetogo
                alarmsystem(Hours3,Minutes3)
firsthour = int(input("What hour do you want this to start going off? "))
firstminute = int(input("What minute do you want this to start going off? "))
alarmsystem(firsthour,firstminute)
while 1 == 1:
    nexttime()
