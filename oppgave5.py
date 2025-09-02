class Motorsykkel:
    def __init__(self, merke, hastighet, antallKm = 0):
            self.merke = merke
            self.hastighet = hastighet
            self.antallKm = antallKm


    def kjor(self, nyDistance):
        self.antallKm += nyDistance


    def info(self):
        return f"{self.merke} - {self.antallKm} km"

m = Motorsykkel("KTM", 80, 1000)
m.kjor(200)
print(m.info())