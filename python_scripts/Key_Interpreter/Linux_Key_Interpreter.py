from rx.core import observable
from pynput.keyboard import Key, Controller

# Ubuntu compatible key interpretter
keyboard = Controller()

# Sends a key press signal
def PressKeyLin(keyString):
    global lastKey
    lastKey = keyString
    print("prepush")
    keyboard.press(keyString)
    print("push")

# Sends a release key signal
def ReleaseKeyLin():
    keyString = lastKey
    print("prerelease")
    keyboard.release(keyString)
    print("release")

# Monitors the observable and updates the values on change
def KeyPress(observable):
    
    observable.subscribe(lambda key: PressKeyLin(key),
    on_next = lambda: ReleaseKeyLin(),
    on_completed =  lambda: ReleaseKeyLin())
