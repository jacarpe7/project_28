import time
from OS_Router import initKeyMonitoring
from rx.core import Observable
from rx.subject import Subject

#TODO: figure out why example is not responding correctly.
def main():
    key="space"
    subject_test = Subject()
    initKeyMonitoring(subject_test)
    subject_test.on_next(key)
    print("here")
    time.sleep(2)

    subject_test.on_next(key)
    print("here")
    time.sleep(2)
    
    subject_test.on_next(key)
    print("here")
    time.sleep(2)
    subject_test.on_completed()

main()