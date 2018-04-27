'''
Title: This is an alarm that perfectly lines up with my sleep schedule
Author: Riley Carpenter
'''
from pygame import mixer
import time
import os
import sys
import random
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
        input("Press enter to stop the music and snooze for 5 minutes")
alarmsystem(5,00)
if Hours1 == 5 and Minutes1 < 5:
    alarmsystem(5,5)
elif Hours1 == 5 and Minutes1 < 10:
    alarmsystem(5,10)
elif Hours1 == 5 and Minutes1 < 15:
    alarmsystem(5,15)
elif Hours1 == 5 and Minutes1 < 20:
    alarmsystem(5,20)
elif Hours1 == 5 and Minutes1 < 25:
    alarmsystem(5,25)
elif Hours1 == 5 and Minutes1 < 30:
    alarmsystem(5,30)
elif Hours1 == 5 and Minutes1 < 35:
    alarmsystem(5,35)
elif Hours1 == 5 and Minutes1 < 40:
    alarmsystem(5,40)
elif Hours1 == 5 and Minutes1 < 45:
    alarmsystem(5,45)
elif Hours1 == 5 and Minutes1 < 50:
    alarmsystem(5,50)
elif Hours1 == 5 and Minutes1 < 55:
    alarmsystem(5,55)
elif Hours1 == 5 and Minutes1 > 00 or Hours1 == 6 and Minutes1 == 0:
    alarmsystem(6,00)
elif Hours1 == 6 and Minutes1 < 5:
    alarmsystem(6,5)
elif Hours1 == 6 and Minutes1 < 10:
    alarmsystem(6,10)
elif Hours1 == 6 and Minutes1 < 15:
    alarmsystem(6,15)
elif Hours1 == 6 and Minutes1 < 20:
    alarmsystem(6,20)
elif Hours1 == 6 and Minutes1 < 25:
    alarmsystem(6,25)
