from rx.core import observable
from pynput.keyboard import Key, Controller
# This will be the easiest to detect by games. Don't use it for anything naughty like making a bot or keylogger...
#TODO: Test linux

keyboard = Controller()

def PressKeyLin(keyString):
    global lastKey
    lastKey = keyString
    print("prepush")
    keyboard.press(keyString)
    print("push")


def ReleaseKeyLin():
    keyString = lastKey
    print("prerelease")
    keyboard.release(keyString)
    print("release")


def KeyPress(observable):
    
    observable.subscribe(lambda key: PressKeyLin(key),
    on_next = lambda: ReleaseKeyLin(),
    on_completed =  lambda: ReleaseKeyLin())
