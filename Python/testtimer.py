#!/usr/bin/python

import threading
import time

def hello_world():
    while(True):
        print 'Hello!'
        time.sleep(2)

if __name__ == "__main__":
    hw_thread = threading.Thread(target = hello_world)
    hw_thread.daemon = True
    hw_thread.start()
    try:
        time.sleep(500)
    except KeyboardInterrupt:
        print '\nGoodbye!'
