from rx.core import observable
# from Quartz import CoreGraphics
#TODO: implement Linux key interpretting.

def PressKeyLin(hexKeyCode):
    global lastKey
    lastKey = hexKeyCode
    print("prepush")
    # event = CoreGraphics.CGEventCreateKeyboardEvent(None, hexKeyCode, True)
    # CoreGraphics.CGEventPost(Quartz.CoreGraphics.kCGHIDEventTap, event)
    print("push")


def ReleaseKeyLin():
    hexKeyCode = lastKey
    print("prerelease")
    # event = CoreGraphics.CGEventCreateKeyboardEvent(None, hexKeyCode, False)
    # CoreGraphics.CGEventPost(Quartz.CoreGraphics.kCGHIDEventTap, event)
    print("release")


def KeyPress(observable):
    
    observable.subscribe(lambda key: PressKeyLin(linKeyWords[key]),
    on_next = lambda: ReleaseKeyLin(),
    on_completed =  lambda: ReleaseKeyLin())

#TODO: Get OSX key codes
linKeyWords = {
    "z":6,
    }