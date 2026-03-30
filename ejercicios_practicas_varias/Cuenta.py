#Crea una clase llamada Cuenta que tendrá los siguientes atributos:
# titular (que es una persona) y cantidad (puede tener decimales). 
# El titular será obligatorio y la cantidad es opcional. 
# Construye los siguientes métodos para la clase:
#Un constructor, donde los datos pueden estar vacíos.
#Los setters y getters para cada uno de los atributos. 
# El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
##mostrar(): Muestra los datos de la cuenta.
#ingresar(cantidad): se ingresa una cantidad a la cuenta, 
# si la cantidad introducida es negativa, no se hará nada.
#retirar(cantidad): se retira una cantidad a la cuenta. 
# La cuenta puede estar en números rojos.

class Cuenta:
    def __init__(self, titular="", cantidad=0):
      self._titular = titular
      self._cantidad = cantidad

    def get_titular(self):
        return self._titular
    def get_cantidad(self):
        return self._cantidad

    def mostrar_cuenta(self):
        print(f"\n DATOS DE LA CUENTA:\n TITULAR:{self._titular.get_nombre()}\n SALDO:${self._cantidad}")
    
    def ingresar(self, monto):
        if monto > 0:
            self._cantidad += monto
            print(f"Has ingresado: ${monto}. Saldo actual: ${self._cantidad}")
        else:
            print("No se puede ingresar una cantidad negativa")

    def retirar(self, monto):
        if self._cantidad < monto:
            print(f"ALERTA!!! Su saldo va a quedar en rojo!!! ")
        self._cantidad -= monto
        print(f"Has retirado: ${monto}. Saldo actual: ${self._cantidad}")

from ejercicio1 import Persona

titular1 = Persona("Ana Perez", 67, "12897423")
mi_cuenta = Cuenta(titular1, 120500.98)  
mi_cuenta.mostrar_cuenta()
mi_cuenta.ingresar(500)
mi_cuenta.retirar(200100)