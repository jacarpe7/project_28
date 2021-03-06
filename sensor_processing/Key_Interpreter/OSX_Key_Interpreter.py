from rx.core import observable
from Quartz import CoreGraphics

# OSX Compatible key interpretter
# Sends a key press signal
def PressKeyOSX(hexKeyCode):
    global lastKey
    lastKey = hexKeyCode
    print("prepush")
    event = CoreGraphics.CGEventCreateKeyboardEvent(None, hexKeyCode, True)
    CoreGraphics.CGEventPost(CoreGraphics.kCGHIDEventTap, event)
    print("push")

# Sends a key release signal
def ReleaseKeyOSX():
    hexKeyCode = lastKey
    print("prerelease")
    event = CoreGraphics.CGEventCreateKeyboardEvent(None, hexKeyCode, False)
    CoreGraphics.CGEventPost(CoreGraphics.kCGHIDEventTap, event)
    print("release")

# Monitors the observable and updates the values on change
def KeyPress(observable):
    
    observable.subscribe(lambda key: PressKeyOSX(macKeyWords[key]),
    on_next = lambda: ReleaseKeyOSX(),
    on_completed =  lambda: ReleaseKeyOSX())

# Translates keystrokes to CGKeyCode
macKeyWords = {
    "a":0,
    "s":1,
    "d":2,
    "f":3,
    "h":4,
    "g":5,
    "z":6,
    "x":7,
    "c":8,
    "v":9,
    "b":11,
    "q":12,
    "w":13,
    "e":14,
    "r":15,
    "y":16,
    "t":17,
    "o":31,
    "u":32,
    "[":33,
    "i":34,
    "p":35,
    "RETURN":36,
    "l":37,
    "j":38,
    "'":39,
    "k":40,
    ";":41,
    "\\":42,
    ",":43,
    "/":44,
    "n":45,
    "m":46,
    ".":47,
    "TAB":48,
    "SPACE":49,
    "`":50,
    "DELETE":51,
    "ENTER":52,
    "ESCAPE":53,
    }