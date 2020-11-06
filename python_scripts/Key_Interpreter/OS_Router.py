import sys
from rx.core import Observable
from rx.subject import BehaviorSubject
from Windows_Key_Interpreter import KeyPress
from OSX_Key_Interpreter import KeyPress



#determins the user OS and sends to appropriate function
def initKeyMonitoring(observable):
    if sys.platform.startswith('win32' | 'cygwin'):
        winKey(observable)
    elif sys.platform.startswith('darwin'):
        osxKey(observable)
    return  
    # Linux-specific code here...

#Windows Key Translations
#observables must contain a key description (see interpreter files)
def winKey(observable):
    KeyPress(observable)
    return

#TODO: OSX Key Translations
def osxKey(observable):
    return
