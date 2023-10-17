from deportista import Deportista

class Futbolista(Deportista):
    
    _listaFutbolistas= []
    
    def __init__(self, nombre, edad, altura, sexo, años, goles, tarjetas, piernaHabil):
        super().__init__(nombre, edad, altura, sexo, "Futbol", años)
        self._tarjetasRojas = tarjetas
        self._golesMarcados = goles        
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)

    def setTarjetasRojas(self, tarjetas):
        self._tarjetasRojas = tarjetas
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setGolesMarcados(self, goles):
        self._golesMarcados = goles
    
    def getGolesMarcados(self):
        return self._golesMarcados    
    
    def setPiernaHabil(self, pierna):
        self._piernaHabil = pierna
    
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def __str__(self):
        cadena = "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(self.getNombre(), self.getDeporte(), str(self.getEdad()), str(self.getAñosPracticando()))
        return cadena


    @classmethod
    def setListaFutbolistas(cls, futbolistas):
        cls._listaFutbolistas = futbolistas
    
    @classmethod
    def getListaFutbolistas(cls):
        return cls._listaFutbolistas

if __name__ == "__main__":
     futbolista = Futbolista("Felipe Perez", 21, "1,56", "M", 8, 189, 7, "Izquierda")
     print(futbolista.__str__())