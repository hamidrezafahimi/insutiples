
import os

file = "log.txt"
if os.path.exists(file):
        os.remove(file)