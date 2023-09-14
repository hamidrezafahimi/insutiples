from io import StringIO
import sys

sys.stdout = buffer = StringIO()

print("Hello World")

with open('readme.txt', 'w') as f:
    f.write(buffer.getvalue())