class DatosNave: 
    def __init__(self, nombre: str, escudo: float): 
       self.titular = nombre 
       self.escudo = escudo

    def recibir_disparo(self, disparo: float, escudo: float): 
       if self.escudo <= 0:
        print("Nave destruida.")  
       else: 
        self.escudo -= disparo 
        print(f"Disparo exitoso, escudo restante: {self.escudo}")  


    def recargarEscudos(self, recarga_escudo, escudo: float) -> bool:  
      if 0 < self.escudo: 
        self.escudo += recarga_escudo 
        print(f"Recarga de escudo exitoso, nivel de escudo: {self.escudo}") 
        return True 
      else: 
        print("La nave esta hecha pedazos :(") 
        return False        

nave = DatosNave("La Divina Nave", 500.00)

while nave.escudo > 0:
  nave.recibir_disparo(250.00 , 500.00)
  nave.recargarEscudos(150.00, 500.00) 
 