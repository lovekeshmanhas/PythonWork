# Health Programmer
# 9am - 5am
# Water - water.mp3 (3.5 litres) - Drank - capture logs
# Eyes  - eyes.mp3 (every 30 min) - EyDone - logs
# Physical activity - physical.mp3 - every 45 min - ExDone - logs
#
# Rules
# Pygame module to play audio

import time
from pygame import mixer

def logTime():
    return time.asctime(time.localtime(time.time()))

def playMp3(mp3File):
    mixer.init()
    mixer.music.load(mp3File)
    mixer.music.play()

def stopMp3():
    mixer.init()
    mixer.music.stop()


if __name__ == '__main__':
    while(True):
        time.sleep(20)
        playMp3("water.mp3")
        inputValue = input("Enter q to done ")
        print("Logged Time ",logTime())
        if inputValue == "q":
            stopMp3()
            f = open("water.log","a")
            f.write(f"Water drink at {logTime()} \n")
            f.close()
        else:
            stopMp3()
            f = open("water.log", "a")
            f.write(f"Water not drink at {logTime()} \n")
            f.close()

