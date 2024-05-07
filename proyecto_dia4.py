nombre=input('coloque su nombre: ')
from random import *
numero_secreto = randint(1,100)
print('debes adivinar el numero secreto que esta entre 1 y el 100 tienes 8 intentos buena suerte')
numero_usuario= input('ingrese el numero: ')
for x in range(1,9):
    while float(numero_usuario) < 1 or float(numero_usuario) > 100:
        print('ups este numero no es permitido')
        numero_usuario = input('ingrese un numero valido: ')
    if float(numero_usuario)<int(numero_secreto):
        print('el numero que usted ingreso es menor al numero secreto')
        print(f'te quedan {8-x} intentos')
        if x == 8:
            print(f'lo siento {nombre} has perdido')
            break
        numero_usuario = input('ingrese otro numero: ')

    elif float(numero_usuario)>int(numero_secreto):
        print('el numero que usted ingreso es mayor al numero secreto')
        print(f'te quedan {8-x} intentos')
        if x==8:
            print(f'lo siento {nombre} has perdido')
            break
        numero_usuario = input('ingrese otro numero: ')

    elif float(numero_usuario)==int(numero_secreto):
        print(f'felicidades {nombre} adivino el numero')
        print(f'te tomo {x} intentos')
        break