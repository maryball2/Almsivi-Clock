'''
Title: This is an alarm that perfectly lines up with my sleep schedule
Author: Riley Carpenter
'''
from pygame import mixer
import time
import os
import sys
import random
snoozeorstop = " "
Currenttime = time.ctime()
Hours1 = int(Currenttime[11:13])
Minutes1 = int(Currenttime[14:16])
Seconds = int(Currenttime[17:19])
optionalsongs = ["Pink Floyd Time.wav","Alarm2.wav","Alarm3.wav","Alarm4.wav","Alarm5.wav","Alarm6.wav","Alarm7.wav","Alarm8.wav","Alarm9.wav","Alarm10.wav"]
phrases = ["Wake up Riley!!!!","It's time to wake up it's time to wake up","HEEEEYYY WAKE UP","RILEY RILEY RILEY WAKE UP","1 2 3 4 5 6 7 8 9 it is time to wake up","Riley more alarms are to come UNLESS you get up","OH WHEN SHALL I SEE JESUS you wanna not hear this again? Wake up","I'm so tired of telling you to wake up just wake up"]
def playsound(soundfile):
    mixer.init()
    mixer.music.load(soundfile)
    mixer.music.play(-1)
def stopsound():
    mixer.music.stop()
def alarm(hour,minute):
    print(random.choice(phrases))
    if Hours1 == hour and Minutes1 == minute:
        stopsound()
        playsound(random.choice(optionalsongs))
        snoozeorstop = input("Do you want to stop the song? ")
        if snoozeorstop == "stop":
            stopsound()
citysounds = input("Do you want to play the soothing sounds of the city? ")
if citysounds == "y" or citysounds == "Yes" or citysounds == "Y" or citysounds == "yes":
    playsound("Citys Night ambience sounds.wav")
while Hours1 != 5 and Minutes1 != 0:
    Hours1 = int(Currenttime[11:13])
    Minutes1 = int(Currenttime[14:16])
    Seconds = int(Currenttime[17:19])
    time.sleep(1)
alarm(5,00)
alarm(5,5)
alarm(5,10)
alarm(5,15)
alarm(5,20)
alarm(5,25)
alarm(5,30)
alarm(5,35)
alarm(5,40)
alarm(5,45)
alarm(5,50)
alarm(5,55)
alarm(6,00)
alarm(6,5)
alarm(6,10)
alarm(6,15)
alarm(6,20)
alarm(6,25)
