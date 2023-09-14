
class AA:
    def __init__(self):
        pass

    def func1(self, st):
        print(st)
    
    def func2(self):
        getattr(self, "func1")("sfff")



if __name__ == '__main__':
    a = AA()
    a.func2()