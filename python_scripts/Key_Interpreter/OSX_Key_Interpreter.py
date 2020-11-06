from rx.core import observable
import Quartz
#TODO: implement mac OSX key interpretting.
# OSX compatibility will have to be written in xcode using PyObjC

def PressKeyOSX(hexKeyCode):
    Quartz.CGEventCreateKeyboardEvent(None, hexKeyCode, True)

def ReleaseKeyOSX(hexKeyCode):
    Quartz.CGEventCreateKeyboardEvent(None, hexKeyCode, False)


def KeyPress(observable):
    
    observable.subscribe(lambda key: PressKeyOSX(macKeyWords[key]),
    on_completed =  lambda key: ReleaseKeyOSX(key))

#TODO: Get OSX key codes
macKeyWords = {
    "up":"",
    "down":"",
    "left":"",
    "right":"",
    "space":""}