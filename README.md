# Cajero-Automatico-UCSP
Integrantes: Gabriel de la Colina - Guillermo Flor - Sebastian Chaña - Henry Wood

Primero definimos “montos” como una lista, donde va a contener todos los montos válidos a retirar.
Luego definimos “saldoActual” como 10000
Seguimos con esUsuario, el cual tomará como valor True si la clave ingresada es correcta y proseguirá con imprimir el menú, y tomará el valor de False si la clave es incorrecta, procediendo a romper con el código.
Finalmente, definimos “salir” como False, si toma valor True, el código imprimirá una despedida, siguiendo a romper con el código.

Definimos el menú, el cual va a contener las 3 opciones, “Retirar, Ver saldo y Salir” y luego definimos función, la que, si toma como valor 1, ejecutará la opción de “Retirar”, si toma como valor 2, “Ver Saldo”, y si toma como valor 3, “Salir”.

Se romperá el código si se elige un valor que no sea 1, 2 o 3 y se imprimirá “Entrada no válida”.

Para definir “Retirar” lo que hicimos fue definir también “Retirar Monto” e “Ingresar Monto”, los cuales toman valores de 1 y 2 respectivamente.
Si eligen la opción 1, definimos retiro con la cantidad que vayamos a retirar, si este es mayor o igual a 10000 o menor o igual a 0, imprimirá “Ese Monto No Se Puede Retirar”.
Si no cumple con esa restricción, pasará a buscar en toda la lista, previamente antes definida como “montos” si el monto a retirar es válido, si es válido, la variable “saldoActual” pasa a restarse con el retiro, el cual tomará valor como “i”en los montos.

Luego para la opción 2, la cual es “Ver Saldo”, solo imprimimos el saldo actual como string.

Para finalizar, la variable, “Salir” si toma valor como True, imprimirá “GRACIAS POR SU ELECCIÓN DE CAJERO” y procederá a romper con el código.

Ejemplo de Funcion:

C A J E R O   A U T O M A T I C O
Ingrese su codigo de autentificacion: 1313

USUARIO UCSP IDENTIFICADO


RETIRAR [1]     VER SALDO [2]     SALIR [3]
Ingrese Numero de Funcion: 1

RETIRAR MONTO [1]     RETIRAR MONTO PERSONAL[2]
Ingrese Numero de Funcion: 1

S/.20
S/.50
S/.100
S/.150
S/.500
CUANTO DESEA RETIRAR: 500

SU SALDO ACTUAL ES: S/.9500

RETIRAR [1]     VER SALDO [2]     SALIR [3]
Ingrese Numero de Funcion: 2

SU SALDO ACTUAL ES: S/.9500

RETIRAR [1]     VER SALDO [2]     SALIR [3]
Ingrese Numero de Funcion: 3

GRACIAS POR SU ELECCION DE CAJERO

Process finished with exit code 0
