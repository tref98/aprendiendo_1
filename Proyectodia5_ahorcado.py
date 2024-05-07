from random import *

def seleccion_usuario():
    letra=input('por favor ingrese una letra: ')
    while len(letra)>=2:
        print('debe ingresar solamente una letra')
        letra=input('por favor ingrese una letra: ')
    while letra.isalpha()==False:
        print('lo que ingreso es un numero')
        letra=input('por favor ingrese una letra: ')
    return letra

def pasar_palabra_a_guiones(palabra):
    guiones=''
    for n in range(0,len(palabra)):
        guiones = guiones+'-'
    return guiones

def verificacion_letra(palabra,letra):
    if letra in palabra:
        return True
    else:
        return False

def cambio_de_guiones(palabra,letra,guiones):
    guiones2=''
    if letra in palabra:
        for n in range(0, len(palabra)):
            if palabra[n]==letra:
             guiones2=guiones2+letra
            else:
                guiones2=guiones2+guiones[n]
        guiones=guiones2
    return guiones

def juego(palabra,guiones):
    print(guiones)
    vidas=6
    print(f'tienes que adivinar la plabra secreta y tienes {vidas} vidas para lograrlo')
    lista_errores=[]
    while vidas!=0:
        letra=seleccion_usuario()
        verificacion=verificacion_letra(palabra,letra)
        if verificacion==True:
            guiones=cambio_de_guiones(palabra,letra,guiones)
            print(f'la letra es correcta y la palabra va:')
            print(guiones)
        else:
            vidas=vidas-1
            lista_errores.append(letra)
            print(f'la letra es erronea perdiste una vida te quedan {vidas} vidas y estas son las letras erroneas:')
            print(lista_errores)

        if guiones==palabra:
            print(f'gano el juego y te quedaron {vidas} vidas')
            break
        else:
            pass
    if vidas==0:
        print(f'game over la palabra era {palabra}')
    else:
        pass


palabras=['hipopotomonstrosesquipedaloifobia','Fructifero','otorrinolaringologo','amistad','antiguedad','listo','fiesta','huevo','cuca','licenciado','alcohol','piquela','breves','esternocleidomastoideo','geisha','excentrico','aristocracia']
palabra_secreta=choice(palabras)
guiones=pasar_palabra_a_guiones(palabra_secreta)
juego(palabra_secreta,guiones)

