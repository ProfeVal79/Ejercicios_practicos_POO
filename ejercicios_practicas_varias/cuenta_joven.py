#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven
#que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad 
#se debe guardar una bonificación que estará expresada en tanto por ciento.
# Construye los siguientes métodos para la clase:
#Un constructor.
#Los setters y getters para el nuevo atributo.
#En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad.
#por lo tanto hay que crear un método esTitularValido() que devuelve verdadero 
#si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
#Además la retirada de dinero sólo se podrá hacer si el titular es válido.
#El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
#Piensa los métodos heredados de la clase madre que hay que reescribir.

#Definición de la clase hija que hereda de la clase madre "Cuenta"
from Cuenta import Cuenta
from Persona import Persona
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
#Super() invoca el constructor de la clase madre(Cuenta)
#para inicializar atributos heredados sin repetir código.
        super().__init__(titular, cantidad)
        self._bonificacion = 0
        self.set_bonificacion(bonificacion)

    def get_bonificacion(self):
        return self._bonificacion

    def set_bonificacion(self, nueva_bonificacion):
        if nueva_bonificacion > 100:
            print(f"ERROR!!!La bonificación no puede ser mayor a 100%")
        else:
         self._bonificacion = nueva_bonificacion

    def es_titular_valido(self):
#Retorna el resultado booleano directamente tras la comparación lógica 
#True si tiene entre 18 y 25, caso contrario retorna False.
        return self.get_titular().get_edad() >= 18 and self.get_titular().get_edad() < 25

    def mostrar(self):
        return f"Cuenta Joven de:{self.get_titular().get_nombre()}\n - Saldo: ${self.get_cantidad()}\n- Bonificación:{self.get_bonificacion()}%"

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar: El titular no es válido para esta cuenta joven")        

         

#Instancia
titular_1 = Persona("Valeria", 60, "44897803")
mi_cuenta1 = CuentaJoven(titular_1, 100000, 200)
print(mi_cuenta1.mostrar())
mi_cuenta1.retirar(800)
    

    