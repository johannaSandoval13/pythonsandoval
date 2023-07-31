class Fandom:
    def __init__(self, fanbase):
        self.fanbase = fanbase

class Fan:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def pertenencia(self, fandom:Fandom):
        self.fandom = fandom
    
    def eresUn(self):
        if self.fandom is not None:
            print(f"{self.nombre} es parte del fandom {self.fandom.fanbase}")
        else: 
            print(f"{self.nombre} no pertenece a ningun fandom")

f1 = Fan("Liry")
fb1 = Fandom("Blinks")
f1.pertenencia(fb1)
f1.eresUn()

