class BatcuevaSystem: 
    def __init__(self, __mando__central__pass: str, __nivel__inicial__): 
        self.__mando__central__pass = __mando__central__pass
        self.__nivel__alerta = __nivel__inicial__ 

    def obtener__alerta(self) -> str:
        return self.__nivel__alerta    

    def cambiar__alerta(self, nueva__alerta: str, clave__ingresada: str):
        if clave__ingresada == self.__mando__central__pass:
            self.__nivel__alerta = nueva__alerta
            print(f"¡Acceso concedido! Nivel de alerta: {self.__nivel__alerta}")
        else:
            print("Clave incorrecta, ¡Acceso denegado!")        


baticueva = BatcuevaSystem("black123", "verde")

print("\n--- Intento 1: clave incorrecta ---")
baticueva.cambiar__alerta("Rojo", "villano234")
print(F"Nivel de amenenaza: {baticueva.obtener__alerta()}")

print("\n--- Intento 2: clave correcta ---")
baticueva.cambiar__alerta("amarillo", "black123")
print(F"Nivel de amenenaza: {baticueva.obtener__alerta()}")