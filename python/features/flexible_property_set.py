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
    def config(self):
        if hasattr(self, 'a'):
            return self.__a
        else:
            raise Exception('Request for `config` attribute of tracker {:s} while no config is set\
           by user'.format(self.name))
    
    @config.setter
    def config(self, val):
        self.__a = val

    @property
    def a(self):
        return self.__a

    ## the attribute name and the method name must be same which is used to set the value for the attribute
    @a.setter
    def a(self, var):
        self.__a = var
    

if __name__ == "__main__":
    obj = Trackers.LDES
    # obj.config = 123
    print(obj.config)
    pass