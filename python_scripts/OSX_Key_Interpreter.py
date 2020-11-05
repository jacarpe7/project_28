import Quartz
#TODO: implement mac OSX key interpretting.
# OSX compatibility will have to be written in xcode using PyObjC

def PressKeyOSX(hexKeyCode):
    Quartz.CGEventCreateKeyboardEvent(None, hexKeyCode, True)

def ReleaseKeyOSX(hexKeyCode):
    Quartz.CGEventCreateKeyboardEvent(None, hexKeyCode, False)


def KeyPress(hexcode, observable, OS):
    
    if(OS == "Windows"):
        PressKeyOSX(hexcode) # TODO: Find keycodes for OSX keys
        
        ReleaseKeyOSX(hexcode)