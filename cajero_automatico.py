# Almacena las variables predeterminadas, la lista de montos a retirar, el saldo del usuario, y 2 bools que determinan el estado del programa

montos = [20, 50, 100, 150, 500]
saldoActual = 10000
esUsuario = False
salir = False

"______________________________________________________________________________________________________________________"

# Funciones encargadas de ejecutar los procesos del cajero

# Imprime la pagina principal del cajero
def menu():
    global salir
    print("\nRETIRAR [1]     VER SALDO [2]     SALIR [3]")
    funcion = int(input("Ingrese Numero de Funcion: "))

    if (funcion == 1):
        retirar()
    elif (funcion == 2):
        verSaldo()
    elif (funcion == 3):
        salir = True
    else:
        print("\nEntrada No Valida")

# Se divide entre dos, retirar, e ingresar, manipulamos el saldo, y tomamos en cuenta el monto que el usuario quiere retirar, asegurando que el monto sea el correcto al retirar
def retirar():
    global saldoActual
    print("\nRETIRAR MONTO [1]     INGRESAR MONTO [2]")
    opcion = int(input("Ingrese Numero de Funcion: "))

    if(opcion == 1):
        retiro = int(input("\nCUANTO DESEA RETIRAR: "))
        if(retiro >= 10000 or retiro <= 0):
            print("\nEse Monto No Se Puede Retirar")

        for i in montos:
            if (retiro == i):
                saldoActual -= retiro
                verSaldo()
    elif(opcion == 2):
        ingreso = int(input("\nCUANTO DESEA INGRESAR: "))
        saldoActual += ingreso
        verSaldo()
    else:
        print("\nEntrada No Valida")

# Se visualiza el saldo convertido en str, pero no alterado
def verSaldo():
    print("\nSU SALDO ACTUAL ES: S/." + str(saldoActual))

"______________________________________________________________________________________________________________________"

# Primer visualizacion del programa, se ingresa el codigo de autentificacion, y se comprueba mediante if, si es usuario, inicia el while de abajo

print("C A J E R O   A U T O M A T I C O")
autentificacion = int(input("Ingrese su codigo de autentificacion: "))

if(autentificacion == 1313):
    print("\nUSUARIO UCSP IDENTIFICADO\n")
    esUsuario = True
else:
    print("\nUSUARIO NO IDENTIFICADO")
    esUsuario = False

"______________________________________________________________________________________________________________________"

# El codigo central ocurre aqui, se puede interactuar con el menu y las opciones de aquella, y continua funcionando hasta salir, donde rompe el while

while True:
    if(esUsuario == True):
        menu()
        if(salir == True):
            print("\nGRACIAS POR SU ELECCION DE CAJERO")
            break
    else:
        break