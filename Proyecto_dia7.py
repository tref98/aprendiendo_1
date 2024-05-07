from os import system
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta=numero_cuenta
        self.balance=float(balance)
    def __str__(self):
        return f"bienvenido {self.nombre} {self.apellido} el numero de cuenta es {self.numero_cuenta} y su balance es {self.balance}"


    def depositar(self):
        cantidad=input('Ingrese el valor a depositar: ')
        self.balance=self.balance+float(cantidad)

    def retirar(self):
        cantidad=input('Ingrese el valor a retirar: ')
        while float(cantidad)>self.balance:
            print('no tienes suficiente dinero para este retiro')
            cantidad=input('Ingrese un valor permitido retirar: ')
        self.balance=self.balance-float(cantidad)

def creacion_cliente():
    nombre=input('Ingrese su nombre: ')
    apellido=input('Ingrese su apellido: ')
    numero_cuenta=input('Ingrese su numero cuenta: ')
    balance=input('Ingrese su balance: ')
    cliente=Cliente(nombre,apellido,numero_cuenta,balance)
    return cliente

def inicio(cliente):
    print(cliente)
    print('1] Depositar\n'
          '2] Retirar\n'
          '3] salir')
    opcion=input('Seleccione una opcion: ')
    return int(opcion)

cliente=creacion_cliente()
opcion=inicio(cliente)
system('cls')
while opcion!=3:
    if opcion == 1:
        cliente.depositar()
        system('cls')
        opcion=inicio(cliente)
        system('cls')
    elif opcion == 2:
        cliente.retirar()
        system('cls')
        opcion=inicio(cliente)
        system('cls')
print('Hasta luego')
