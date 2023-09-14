from example import *

# Works as expected:
class Test(ExampleListener):
    def OnEvent(self, s):
        print s


t = Test()
call_listener(t)

# # Segmentation fault:
# class TestWithInit(ExampleListener):
#     def __init__(self, a, b, c):
#         self.a = a;
#         self.b = b;
#         self.c = c;

#     def OnEvent(self, s):
#         print s, self.a, self.b, self.c

# twi = TestWithInit(1, 2, 3)
# call_listener(twi)