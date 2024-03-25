from abc import ABC, abstractmethod

class vorm(ABC):

    @abstractmethod
    def nzijdes(self):
        print("de figuur heeft n zijdes")

class driehoek(vorm):

    def nzijdes(self):
        print("deze heeft 3 zijdes")

class vierkant(vorm):

    def __init__(self,zijde):
        self.zijde = zijde
    def nzijdes(self):
        super().nzijdes()
        print("deze heeft 4 zijdes")
    def geef_oppv(self):
        return self.zijde**2

d = vierkant(5)
d.nzijdes()
print(d.geef_oppv())


