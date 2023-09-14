from enum import Enum

class Trackers(Enum):
    KCFHOG = 1
    LDES = 2
    STRCF = 3
    CSRDCF = 4
    PRDIMP50 = 5
    DIMP50 = 6
    KYS = 7
    TOMP = 8
    MIXFORMERVIT = 9

    @property
    def a(self):
        return self.__a

    ## the attribute name and the method name must be same which is used to set the value for the attribute
    @a.setter
    def a(self, var):
        self.__a = var
    

if __name__ == "__main__":
    obj = Trackers.LDES
    # obj.a = 123
    print(obj.a)
    pass