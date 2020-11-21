from rx.core import observable
from Quartz import CoreGraphics
# TODO: Test Mac OSX keyboard
# OSX compatibility will have to be written in xcode using PyObjC

def PressKeyOSX(hexKeyCode):
    global lastKey
    lastKey = hexKeyCode
    print("prepush")
    event = CoreGraphics.CGEventCreateKeyboardEvent(None, hexKeyCode, True)
    CoreGraphics.CGEventPost(Quartz.CoreGraphics.kCGHIDEventTap, event)
    print("push")


def ReleaseKeyOSX():
    hexKeyCode = lastKey
    print("prerelease")
    event = CoreGraphics.CGEventCreateKeyboardEvent(None, hexKeyCode, False)
    CoreGraphics.CGEventPost(Quartz.CoreGraphics.kCGHIDEventTap, event)
    print("release")


def KeyPress(observable):
    
    observable.subscribe(lambda key: PressKeyOSX(macKeyWords[key]),
    on_next = lambda: ReleaseKeyOSX(),
    on_completed =  lambda: ReleaseKeyOSX())

#TODO: Get OSX key codes
macKeyWords = {
    "z":6,
    }