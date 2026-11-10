class NaveEspacial:
    def __init__(self, nombre: str, piloto: str, escudo: int):
       self.nombre = nombre
       self.piloto = piloto
       self.escudo = escudo

jugador1 = NaveEspacial("Estrella Mortal", "Alfonso", 90)
jugador2 = NaveEspacial("Linmax", "María", 80)

print(f"Jugador 1 - nombre: {jugador1.nombre}, piloto: {jugador1.piloto}, nivel de escudo: {jugador1.escudo}")
print(f"Jugador 2 - nombre: {jugador2.nombre}, piloto: {jugador2.piloto}, {jugador2.escudo}")