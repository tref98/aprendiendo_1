from pathlib import Path
from os import system
import os

def mostrar_categoria(archivo):
    print('Estas son las catgorias')
    for x in Path(archivo).glob('*/'):
        print(f'- {x.name}')

def mostrar_recetas(archivo, categoria):
    categoria2=Path(archivo/categoria)
    print(categoria2)
    for txt in Path(categoria2).glob('*.txt'):
        print(txt.stem)

def seguir_al_menu(archivo):
    print('Quiere volver al menu??')
    respuesta=input('si o no: ')
    if respuesta=='si':
        system('cls')
        eleccion(archivo)
    else:
        pass


def eleccion(archivo):
    print('Mira las opciones')
    print('1) Leer receta \n'
          '2) Crear receta \n'
          '3) Crear categoria\n'
          '4) Eliminar receta \n'
          '5) Eliminar categoria\n'
          '6) finalizar programa')
    ingreso_usuario=input('Elije una de las opciones: ')
    while ingreso_usuario.isnumeric()==False:
        print('No es valida la opcion establecida')
        ingreso_usuario=input('Elije una de las opciones: ')
    while int(ingreso_usuario) <1 or int(ingreso_usuario)>6:
        print('no esta dentro de las opciones')
        ingreso_usuario=input('Elija una opcion: ')
    while int(ingreso_usuario)!=0:
        system('cls')
        if int(ingreso_usuario)==1:
            mostrar_categoria(archivo)
            categoria_escojida = input('Elija una de las categorias: ')
            system('cls')
            if categoria_escojida == '':
                eleccion(archivo)
                break
            mostrar_recetas(archivo, categoria_escojida)
            receta_escojida=input('Elija una de las recetas: ')
            if receta_escojida == '':
                eleccion(archivo)
                break
            receta=receta_escojida+'.txt'
            system('cls')
            print(Path(archivo,categoria_escojida,receta).read_text())
            seguir_al_menu(archivo)
            break
        elif int(ingreso_usuario)==2:
            mostrar_categoria(archivo)
            categoria_escojida = input('Elija una de las categorias: ')
            system('cls')
            if categoria_escojida == '':
                eleccion(archivo)
                break
            nueva_receta=input('Escriba el nombre de la nueva receta: ')
            nombre_receta=nueva_receta+'.txt'
            receta=input('ingrese la receta:\n')
            Path(archivo,categoria_escojida,nombre_receta).write_text(receta)
            seguir_al_menu(archivo)
            break
        elif int(ingreso_usuario)==3:
            carpeta_nueva=input('ingrese el nombre de la nueva categoria: ')
            Path(archivo,carpeta_nueva).mkdir()
            seguir_al_menu(archivo)
            break
        elif int(ingreso_usuario)==4:
            mostrar_categoria(archivo)
            categoria_escojida = input('Elija una de las categorias: ')
            system('cls')
            if categoria_escojida == '':
                eleccion(archivo)
                break
            mostrar_recetas(archivo, categoria_escojida)
            receta_escojida = input('Elija una de las recetas que quiere eliminar: ')
            if receta_escojida == '':
                eleccion(archivo)
                break
            receta=receta_escojida+'.txt'
            Path(archivo,categoria_escojida,receta).unlink()
            seguir_al_menu(archivo)
            break
        elif int(ingreso_usuario)==5:
            mostrar_categoria(archivo)
            categoria_escojida = input('Elija una de las categorias que desea eliminar: ')
            system('cls')
            if categoria_escojida == '':
                eleccion(archivo)
                break
            Path(archivo,categoria_escojida).rmdir()
            seguir_al_menu(archivo)
            break
        else:
            break





casa=Path.home()
print("Bienvenido al resetario de Edwin :v")
print(f"La carpeta de recetas se encuentra en {casa}")
recetas=Path("C:/Users/HP/recetas")
cuenta=0
for txt in Path(recetas).glob('**/*.txt'):
    cuenta += 1

print(f'hay {cuenta} recetas')
print(recetas/'Carnes')
eleccion(recetas)
print('hasta luego')

