#import zipfile
#zip_abnierto = zipfile.ZipFile('Proyecto+Dia+9.zip', 'r')

#zip_abierto.extractall()


import os
import re
import time
import datetime
import math

parametro = r'N\D{3}-\d{5}'
dia = datetime.date(2022,5,10)
inicio = time.time()
print('\n')
print(f'Fecha de busqueda: {dia.today().day}-{dia.today().month}-{dia.today().year} ')
print('\n')
print('ARCHIVO\t\t\t NRO. SERIE')
print('--------\t\t ----------')
cont = 0
for carpeta, subcarpeta, archivo in os.walk('Mi_Gran_Directorio'):
    for arch in archivo:
        archivo = open(carpeta+'\\'+arch,'r')
        texto = archivo.read()
        check = re.search(parametro, texto)
        if check==None:
            pass
        else:
            print(f'{arch}\t {texto[check.start():check.end()]}')
            cont += 1
        archivo.close()

print('\n')
print(f'Números encontrados. {cont}')
fin = time.time()
print(f'Duración de la busqueda: {math.ceil(fin-inicio)}')