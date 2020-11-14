import ctypes, time
from rx.subject import AsyncSubject
from ctypes import wintypes
user32 = ctypes.WinDLL('user32', use_last_error=True)
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions for hardware control
INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

wintypes.ULONG_PTR = wintypes.WPARAM
class KeyBdInput(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class HardwareInput(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

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


LPINPUT = ctypes.POINTER(Input)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions for key press controls

def PressKeyWin(hexKeyCode):
    print("press")
    global lastKey
    lastKey = hexKeyCode
    x = Input(type=INPUT_KEYBOARD,
              ki=KeyBdInput(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKeyWin():
    print("release")
    hexKeyCode = lastKey
    x = Input(type=INPUT_KEYBOARD,
              ki=KeyBdInput(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


#hexcode will be the hexcode that determines the key being pressed. 
# Key inputs can be found here: http://www.flint.jp/misc/?q=dik&lang=en
def KeyPress(observable: AsyncSubject):
    observable.subscribe(lambda key: PressKeyWin(winKeyWords[key]),
     on_next = lambda: ReleaseKeyWin(),
     on_completed =  lambda: ReleaseKeyWin())

    
#find more @https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
winKeyWords = {
    "up":0x26,
    "down":0x28,
    "left":0x25,
    "right":0x27,
    "space":0x41}
