class Mago: 
    def __init__(self, nombre: str, mana_base: float): 
        self.nombre = nombre 
        self.mana_base = mana_base  

class MagoFuego(Mago): 
    def __init__(self, nombre: str, mana_base: float, temperatura_llama: float):
        super().__init__(nombre, mana_base) 
        self.temperatura_llama = temperatura_llama 
        
    def lanzar_bola_fuego(self, ataque_mana: float):  
        self.mana_base -= ataque_mana 
        print(f"Ataque ardiente, temeratura de la llama: {self.temperatura_llama} °,mana restante{self.mana_base}")

class MagoHielo(Mago): 
    def __init__(self, nombre: str, mana_base: float, grosor_escudo: float):
        super().__init__(nombre, mana_base) 
        self.grosor_escudo = grosor_escudo 
        
    def congelar_terreno(self, ataque_mana: float):  
        self.mana_base -= ataque_mana 
        print(f"Ataque de congelación exitoso, grosor de escudo aplicado: {self.grosor_escudo} cm,mana restante{self.mana_base}")

MagoFuego = MagoFuego("Antonio", 1000, 450.5)
MagoHielo = MagoHielo("Elsa", 1000, 15)

MagoFuego.lanzar_bola_fuego(150)
MagoHielo.congelar_terreno(200)