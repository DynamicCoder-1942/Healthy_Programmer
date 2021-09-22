from pygame import mixer
import time

localtime = time.asctime(time.localtime(time.time()))


def water_balance():
    mixer.init()
    mixer.music.load("sample_music.wav")
    mixer.music.set_volume(0.7)
    while True:
        mixer.music.play()

        print("REMINDER :: You have to drink 400ml of water ")
        user_inp = input("Enter 'Stop' to exit REMINDER :: ")

        if user_inp == "Stop" or user_inp == "stop":
            mixer.pause()
            print("*** You have Drank water ***\n"
                  "*** Back to work ***")
            file_open = open("Health Log.txt", "a+")

            file_open.write(f"{localtime} :: Drank water \n")
            # file_open.close()
        break


def eyes_relaxation():
    mixer.init()
    mixer.music.load("sample_music.wav")
    mixer.music.set_volume(0.7)
    while True:
        mixer.music.play()
        print("REMINDER :: You have to relax your eyes by performing some eyes exercise ")

        user_inp = input("Enter 'Stop' to exit REMINDER :: ")

        if user_inp == "Stop" or user_inp == "stop":
            mixer.pause()
            print("*** You have relaxed your eyes now\n"
                  "*** Back to work ***")
            file_open = open("Health Log.txt", "a+")

            file_open.write(f"{localtime} :: Relaxed Eyes\n")
            # file_open.close()
        break


def exercise():
    mixer.init()
    mixer.music.load("sample_music.wav")
    mixer.music.set_volume(0.7)
    while True:
        mixer.music.play()

        print("REMINDER :: You have to perform some body exercise to be fit ")

        user_inp = input("Enter 'Stop' to exit REMINDER :: ")

        if user_inp == "Stop" or user_inp == "stop":
            mixer.pause()
            print("*** You have performed your exercise ***\n"
                  "*** Back to work ***")
            file_open = open("Health Log.txt", "a+")
            file_open.write(f"{localtime} :: Body relaxed\n")
            # file_open.close()
        break


def clearing_file():
    user_inp = input("Enter 'Continue' to update your data 'Clear' to clear data from log :: ")
    if user_inp == "Continue" or user_inp == "continue":
        pass
    elif user_inp == "Clear" or user_inp == "clear":
        a = open("Health Log.txt", "r+")
        a.truncate(0)
        a.close()


while True:
    time.sleep(30*60)
    water_balance()
    mixer.music.pause()

    time.sleep(24*60)
    eyes_relaxation()
    mixer.music.pause()

    time.sleep(60*60)
    exercise()
    mixer.music.pause()

    clearing_file()


