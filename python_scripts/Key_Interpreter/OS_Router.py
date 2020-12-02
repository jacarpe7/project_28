import sys
from rx.core import Observable
from rx.subject import BehaviorSubject

# Determins the user OS and sends to appropriate function
def initKeyMonitoring(observable):
    if sys.platform.startswith('win32' or 'cygwin'):
        
        winKey(observable)
    elif sys.platform.startswith('darwin'):
        
        osxKey(observable)
    else:

        linKey(observable)
    return  


# Routes to Windows interpreter
def winKey(observable):
    from Windows_Key_Interpreter import KeyPress
    KeyPress(observable)
    return

# Routes to OSX interpreter 
def osxKey(observable):
    from OSX_Key_Interpreter import KeyPress
    KeyPress(observable)
    return

# Routes to Linux interpreter
def linKey(observable):
    from Linux_Key_Interpreter import KeyPress
    KeyPress(observable)
    return