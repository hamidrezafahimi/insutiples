import sys
import time

class TerminalLog(object):
    def __init__(self):
        self.orgstdout = sys.stdout
        self.log = open("log.txt", "a")

    def write(self, msg):
        self.orgstdout.write(msg)
        self.log.write(msg)  

sys.stdout = TerminalLog()

for k in range(10):
    print('Hello World')
    time.sleep(0.5)