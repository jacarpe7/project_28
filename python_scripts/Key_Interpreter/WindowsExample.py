import time
from OS_Router import initKeyMonitoring
from rx.core import Observable
from rx.subject import Subject

# Example implementation of windows key interpretter
def main():
    key="space"
    keyTwo="a"
    subject_test = Subject()
    initKeyMonitoring(subject_test)
    subject_test.on_next(keyTwo)
    print("here")
    time.sleep(1)

    subject_test.on_next(key)
    print("here")
    time.sleep(1)
    
    subject_test.on_next(keyTwo)
    print("here")
    time.sleep(1)
    subject_test.on_completed()

main()