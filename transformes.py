class Transformer:
    def transformarse(self) -> str:
        return "El Transformer adopta su forma genérica."

class AutobotCoche(Transformer):
    def transformarse(self) -> str: # Sobrescritura de método
        return "¡Se convierte en un deportivo a 300 km/h!"

class AutobotAvion(Transformer):
    def transformarse(self) -> str: # Sobrescritura de método
        return "¡Despliega las alas y vuela a velocidad supersónica!"

class AutobotDinosaurio(Transformer):
    def transformarse(self) -> str: # Sobrescritura de método
        return "¡Se transforma en un T-Rex robótico!"

# Creación de la lista con un objeto de cada tipo
transformers = [
    AutobotCoche(),
    AutobotAvion(),
    AutobotDinosaurio()
]

print("--- EJÉRCITO DE TRANSFORMERS ---")
# Bucle que aplica polimorfismo (llama al método según la clase de cada objeto)
for t in transformers:
    print(t.transformarse())