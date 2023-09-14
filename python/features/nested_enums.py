from enum import Enum

class A(Enum):
    one=1
    two=2
    three=3

class Parrot(Enum):
    tracker1 = 1
    tracker2 = 2
    tracker3 = 3
    @property
    def voltage(self):
        """Get the current voltage."""
        if self.value == 1:
            return A.one.name
        elif self.value == 2:
            return A.two.name

if __name__ == "__main__":
    trobj = Parrot.tracker2
    print(trobj.voltage)
    # a = A
    # a = A.set1(trobj)
