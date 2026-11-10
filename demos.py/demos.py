#DEMO TDA
#VAMOS AMODELAR UNA CUENTA BANCARIA SIEMPLE
class CuentaBancaria:
    def __init__(self, titular:str, saldo_inicial: float): #_int_ es el metodo cosntructor
        self.titular = titular
        self.saldo = saldo_inicial #atributos del objeto

Cuenta1 = CuentaBancaria("Juan Perez", 1000.0)
Cuenta2 = CuentaBancaria("Maria Lopez", 500.0) #objetos de instanciación


print(f"Cuenta 1: Titular: {Cuenta1.titular}, Saldo: {Cuenta1.saldo}")
print(f"Cuenta 2: Titular: {Cuenta2.titular}, Saldo: {Cuenta2.saldo}") #Acceso a los atributos de instancia


#DEMO FUNCIONES Y PROCEDIMIENTOS
class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial
        # Método para depositar dinero
    def depositar(self, monto: float):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso de ${monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("El monto a depositar debe ser mayor a cero.")
    # Método para retirar dinero
    def retirar(self, monto: float) -> bool:
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso de ${monto}. Saldo restante: ${self.saldo}")
            return True
        else:
            print("Fondos insuficientes o monto inválido.")
            return False
# Pruebas con los métodos
mi_cuenta = CuentaBancaria("Ana Torres", 200000.0)
# Llamada a métodos
mi_cuenta.depositar(50000.0)  # Saldo sube a 250000
mi_cuenta.retirar(100000.0)   # Saldo baja a 150000
mi_cuenta.retirar(300000.0)   # Intento con saldo insuficiente

#DEMO ENCAPSULAMIENTO
class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.__saldo = saldo_inicial if saldo_inicial >= 0 else 0.0  # Atributo Privado

    # Getter para el saldo
    def get_saldo(self) -> float:
        return self.__saldo

    # Setter para el saldo con validación
    def set_saldo(self, nuevo_saldo: float):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("Error: El saldo no puede ser negativo.")

    def depositar(self, monto: float):
        if monto > 0:
            self.__saldo += monto

# Uso y prueba del encapsulamiento
cuenta = CuentaBancaria("Juan", 100.0)
# Intentar acceder directamente al atributo privado generará AttributeError:
# print(cuenta.__saldo)  #  Error!
# Forma correcta a través del Getter
print(f"Saldo actual: ${cuenta.get_saldo()}")  # 100.0
# Intentar modificar con Setter
cuenta.set_saldo(-50.0)  # Muestra mensaje de error
cuenta.set_saldo(200.0)  #  Modificación válida
print(f"Saldo actualizado: ${cuenta.get_saldo()}")  # 200.0

#DEMO HERENCIA
#Clase Padre / Base
class CuentaBancaria:
    def __init__(self, titular: str, saldo: float): 
        self.titular = titular
        self._saldo = saldo  # Usamos protegido (_) para permitir acceso en las clases hijas

    def obtener_saldo(self):
        return self._saldo

# Clase Hija 1
class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular: str, saldo: float, tasa_interes: float):
        # Llama al constructor de la clase padre
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        interes = self._saldo * self.tasa_interes
        self._saldo += interes
        print(f"Interés aplicado: ${interes}. Nuevo saldo: ${self._saldo}")

# Clase Hija 2
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular: str, saldo: float, limite_sobregiro: float):
        super().__init__(titular, saldo)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto: float):
        # Permite retirar incluso si el saldo es menor al monto, hasta el límite de sobregiro
        if monto <= (self._saldo + self.limite_sobregiro):
            self._saldo -= monto
            print(f"Retiro exitoso de ${monto}. Saldo restante: ${self._saldo}")
        else:
            print("Retiro excede el límite de sobregiro permitido.")

# Pruebas de Herencia
ahorros = CuentaAhorros("Laura", 1000000.0, 0.02)  # 2% interés
ahorros.aplicar_interes()
corriente = CuentaCorriente("Pedro", 200000.0, 500000.0)
corriente.retirar(400000.0)  # Retira usando sobregiro

#DEMO POLIMORFISMO
class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo

    # Método genérico que será sobrescrito por las clases hijas
    def generar_extracto(self):
        return f"Extracto General - Titular: {self.titular} | Saldo: ${self.saldo}"

class CuentaAhorros(CuentaBancaria):
    def generar_extracto(self):
        # Sobrescritura de método
        return f"[CUENTA DE AHORROS] Titular: {self.titular} | Saldo Disponible: ${self.saldo}"

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular: str, saldo: float, sobregiro: float):
        super().__init__(titular, saldo)
        self.sobregiro = sobregiro

    def generar_extracto(self):
        # Sobrescritura de método
        return f"[CUENTA CORRIENTE] Titular: {self.titular} | Saldo: ${self.saldo} | Cupo Sobregiro: ${self.sobregiro}"

#Demostración del Polimorfismo
# Creamos una lista heterogénea de cuentas
cuentas = [
    CuentaAhorros("Andrés", 300000.0),
    CuentaCorriente("Beatriz", 150000.0, 200000.0),
    CuentaAhorros("Camilo", 800000.0)
]

# Recorremos la lista ejecutando la misma función en objetos distintos
print("--- EXTRACTOS BANCARIOS ---")
for c in cuentas:
    # Se ejecuta el método correspondiente a la clase de cada objeto en tiempo de ejecución
    print(c.generar_extracto())