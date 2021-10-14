from time import time
from datetime import datetime
from pygame import mixer

def music_on_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        user = input()
        if user == stopper:
            mixer.music.stop()
            break
        else:
            exit()

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water=time()
    init_eyes=time()
    init_exercise=time()

    watersecs=15
    eyessecs=20
    exsecs= 25

    while True:
        if time()-init_water > watersecs:
            print("PLEASE DRINK WATER . Enter drank to stop the alarm ")
            music_on_loop("water.mp3","drank")
            init_water=time()
            log_now("Water drank at ")

        elif time()-init_exercise > exsecs:
            print("PLEASE DO SOME PHYSICAL EXERCISE . Enter doneex to stop the alarm ")
            music_on_loop("physical.mp3","doneex")
            init_exercise=time()
            log_now("Exersice done at ")

        elif time()-init_eyes > eyessecs:
            print("PLEASE RELAX YOUR EYES . Enter doneeyes to stop the alarm ")
            music_on_loop("eyes.mp3","doneeyes")
            init_eyes=time()
            log_now("Eyes relaxed  at ")

