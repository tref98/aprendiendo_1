from Numeros import *
from os import system

p = perfumeria()
f = farmacia()
c = cosmeticos()


def seleccion(valor):
    if int(valor) == 1:
        decorador(p)
        retornar = input("Quiere volver a sacar un turno Y/N: ")
        while retornar.lower() != 'y' and retornar.lower() != 'n':
            print("Este valor no es valido")
            retornar = input("Ingrese y o n: ")
        system('cls')
        return retornar
    elif int(valor) == 2:
        decorador(f)
        retornar = input("Quiere volver a sacar un turno Y/N: ")
        while retornar.lower() != 'y' and retornar.lower() != 'n':
            print("Este valor no es valido")
            retornar = input("Ingrese y o n: ")
        system('cls')
        return retornar
    elif int(valor) == 3:
        decorador(c)
        retornar = input("Quiere volver a sacar un turno Y/N: ")
        while retornar.lower() != 'y' and retornar.lower() != 'n':
            print("Este valor no es valido")
            retornar = input("Ingrese y o n: ")
        system('cls')
        return retornar


def menu():
    print("Que necesita??\n"
          "1) perfumeria\n"
          "2) farmacia\n"
          "3) cosmeticos")
    opcion = input("Escoja el numero que necesita: ")
    while opcion.isnumeric() == False or int(opcion) < 1 or int(opcion) > 3:
        print("Este valor no es valido")
        opcion = input("ingrese un valor valido: ")
    system('cls')
    return opcion


valor = menu()
retornar = seleccion(valor)
while retornar.lower() != 'n':
    valor = menu()
    retornar = seleccion(valor)
print('Hasta luego')
