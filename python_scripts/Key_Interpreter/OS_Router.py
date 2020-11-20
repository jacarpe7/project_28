import sys
from rx.core import Observable
from rx.subject import BehaviorSubject





#determins the user OS and sends to appropriate function
def initKeyMonitoring(observable):
    if sys.platform.startswith('win32' or 'cygwin'):
        
        winKey(observable)
    elif sys.platform.startswith('darwin'):
        
        osxKey(observable)
    else:

        linKey(observable)
    return  


#Windows Key Translations
#observables must contain a key description (see interpreter files)
def winKey(observable):
    from Windows_Key_Interpreter import KeyPress
    KeyPress(observable)
    return

#TODO: Finish debugging OSX Key Translations
def osxKey(observable):
    from OSX_Key_Interpreter import KeyPress
    KeyPress(observable)
    return

#TODO: Linux Key Translations
def linKey(observable):
    from Linux_Key_Interpreter import KeyPress
    KeyPress(observable)
    return