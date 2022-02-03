from pynput import keyboard
import threading
import datetime, time


def count_down(sec):
    for i in range(sec, 0, -1):
        print(i)
        time.sleep(1)
    print("Script Strat")

def loop():
    ctr = keyboard.Controller()
    ctr.press('a')
    ctr.release('a')
    time.sleep(0.5)
    ctr.press(keyboard.Key.enter)
    ctr.release(keyboard.Key.enter)
    time.sleep(1)

#  - functions  -

def loading():
    while running:
        loop()
        print("Done!", datetime.datetime.now())  # , end='\r')


def on_press(key):
    global running  # inform function to assign (`=`) to external/global `running` instead of creating local `running`

    if key == keyboard.Key.f9:
        running = True
        # create thread with function `loading`
        t = threading.Thread(target = loading)
        # start thread
        t.start()

    if key == keyboard.Key.f10:
        # to stop loop in thread
        running = False

    if key == keyboard.Key.f11:
        # stop listener
        return False


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()