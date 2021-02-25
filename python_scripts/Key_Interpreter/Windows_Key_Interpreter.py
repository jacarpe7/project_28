import ctypes, time
from rx.subject import AsyncSubject
from ctypes import wintypes
user32 = ctypes.WinDLL('user32', use_last_error=True)
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions for hardware control
INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
KEYEVENTF_KEYUP = 0x0002


wintypes.ULONG_PTR = wintypes.WPARAM
class KeyBdInput(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class MouseInput(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class Input(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KeyBdInput),
                    ("mi", MouseInput),
                    ("hi", MouseInput))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

# Sends a key press signal
def PressKeyWin(hexKeyCode):
    print("press")
    global lastKey
    lastKey = hexKeyCode
    x = Input(type=INPUT_KEYBOARD,
              ki=KeyBdInput(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

# Sends a key release signal
def ReleaseKeyWin():
    print("release")
    hexKeyCode = lastKey
    x = Input(type=INPUT_KEYBOARD,
              ki=KeyBdInput(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

# Monitors the observable and updates the values on change
def KeyPress(observable: AsyncSubject):
    observable.subscribe(lambda key: PressKeyWin(winKeyWords[key]),
     on_next = lambda: ReleaseKeyWin(),
     on_completed =  lambda: ReleaseKeyWin())

    
# Translates keystrokes to hex
winKeyWords = {
    "up":0x26,
    "down":0x28,
    "left":0x25,
    "right":0x27,
    "space":0x20,
    "shift":0xA0,
    "a":0x41,
    "b":0x42,
    "c":0x43,
    "d":0x44,
    "e":0x45,
    "f":0x46,
    "g":0x47,
    "h":0x48,
    "i":0x49,
    "j":0x4A,
    "k":0x4B,
    "l":0x4C,
    "m":0x4D,
    "n":0x4E,
    "o":0x4F,
    "p":0x50,
    "q":0x51,
    "r":0x52,
    "s":0x53,
    "t":0x54,
    "u":0x55,
    "v":0x56,
    "w":0x57,
    "x":0x58,
    "y":0x59,
    "z":0x5A
    }

