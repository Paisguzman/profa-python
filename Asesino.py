#Author Pablo
from Jugador import Jugador
from Energia import Energia

class Assasin(Jugador, Energia):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
        self.arma = 'pistola'
        self.velocidad = 80
        self.resistencia = 60
        self.ataque = 70
    def clase(self):
        print('Clase', type(self), self.nombreX)
    def estadisticas(self):
        print('velocidad: {3d}'.format(self.velocidad))
        print('resistencia: {3d}'.format(self.resistencia))
        print('ataque: {3d}'.format(self.ataque))
        print('vida: {3d}'.format(super().get_vida()))
        print('energia: {3d}'.format(self.get_energia()))
    
    def atacar(self):
        super().set_energia()

    def defender(self):
        super().set_vida()

    def get_resistencia(self):
        return self.resistencia

    
 
 

      
            
