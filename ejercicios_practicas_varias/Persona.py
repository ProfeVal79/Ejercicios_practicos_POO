# Vamos a crear una clase llamada Persona. Sus atributos son:
#  nombre, edad y DNI. 
# Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. 
# Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# esMayorDeEdad(): Devuelve un valor lógico indicando 
# si es mayor de edad.

class Persona:
    def __init__(self, nombre="", edad=None, DNI=""):
#Usamos los métodos 'set' en el constructor para asegurar que
# los datos iniciales también cumplan con las reglas de validación.      
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_DNI(DNI)
    

    def  get_nombre(self):
        return self._nombre
    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre == "":
         self._nombre = ""
        elif len(nuevo_nombre)<3:
            print(f"ERROR!!! el nombre debe tener al menos 3 caracteres!!!")
        else:
            self._nombre = nuevo_nombre

    def get_edad(self):
        return self._edad
    def set_edad(self, nueva_edad):
        if nueva_edad is None:
            self._edad = 0
        elif nueva_edad < 0:
            print(f"ERROR!!! la edad no puede ser negativo!!!")
        else:
            self._edad = nueva_edad

    def get_DNI(self):
        return self._DNI
    def set_DNI(self, nuevo_DNI):
        if nuevo_DNI == "":
         self._DNI = ""
 #.isdigit <-- asegura que sean digitos numericos no letras o simbolos
        elif nuevo_DNI.isdigit() and 7 <= len(nuevo_DNI) <= 8:
            self._DNI = nuevo_DNI
        else:
            print(f"ERROR!!! El DNI debe ser numerico y tener entre 7 y 8 cifras")

    def mostrar(self):
       datos = f"\n FICHA DE PERSONA\n NOMBRE: {self._nombre} \n EDAD {self._edad} \n DNI: {self._DNI}"
       return datos
    def es_mayor_de_edad(self):
        if self.get_edad() >= 18:
            return True
        else:
         return False

#Instancias
#persona1 = Persona("Diego", 44, "28754983")
#resultado = persona1.mostrar()
#edad_mayor = persona1.es_mayor_de_edad()
#print(resultado)
#print(edad_mayor)

#persona1.set_nombre("Cristian")
#persona1.set_DNI("23457Q4")

#resultado = persona1.mostrar()
#print(resultado)


    


    

   