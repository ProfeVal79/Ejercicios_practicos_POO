# Ejercicios_practicos_POO
##Sistema Bancario POO
Este proyecto consiste en un sistema de gestión de cuentas bancarias desarrollado en Python, aplicando los pilares de la Programación Orientada a Objetos: Encapsulamiento, Herencia y Polimorfismo.
## Estructura de Clases
* Clase Persona: Es la base del sistema. Contiene los datos del usuario:
  * Atributos: nombre, edad, DNI
  * Incluye validaciones para asegurar que los datos sean correctos.
* Clase Cuenta: Representa una cuenta bancaria genérica.
  * Relación: Utiliza Composición, ya que el atributo titular es un objeto de la clase Persona.
  * Atriburos: titular (Clase Persona) y cantidad (saldo).
  * Métodos: ingresar() y retirar().
* Clase CuentaJoven (Herencia): Es una clase hija que hereda de Cuenta.
  * Concepto: Especialización de la cuenta para usuarios entre 18 y 25 años.
  * Bonificación: Incluye un atributo extra de bonificación (porcentaje).
  * Seguridad: Sobreescribe el método retirar() para verificar que el titular siga siendo válido según su edad antes de permitir movimientos.
## Tecnologias y Conceptos Aplicados
* Lenguaje: Python 3.x
* Herencia: Reutilización de lógica de la clase madre Cuenta.
* Encapsulamiento: Uso de atributos privados (_atributo) y métodos Getter/Setter para proteger la integridad de los datos.
* Validaciones: Lógica personalizada para limites de bonificación y rango de edad.
