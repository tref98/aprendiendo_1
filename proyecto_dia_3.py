texto = input("introdusca el texto de su elleccion: ")

primer_letra = input("introdusca la primer letra de su elección: ")
segunda_letra = input("introdusca la segunda letra de su elección: ")
tercera_letra = input("introdusca la tercera letra de su elección: ")

texto_min = texto.lower()

conteo_primer_letra = texto_min.count(primer_letra.lower())
conteo_segunda_letra = texto_min.count(segunda_letra.lower())
conteo_tercera_letra = texto_min.count(tercera_letra.lower())

print(f"la letra \"{primer_letra}\" se repite {conteo_primer_letra} veces")
print(f"la letra \"{segunda_letra}\" se repite {conteo_segunda_letra} veces")
print(f"la letra \"{tercera_letra}\" se repite {conteo_tercera_letra} veces")

lista_texto = texto.split()
largo_texto = len(lista_texto)

print("el texto tiene "+str(largo_texto)+" palabras")

primer_letra_texto = texto[0]
ultima_letra_texto = texto[-1]

print("la primer letra del texto es: \""+primer_letra_texto+"\"")

print("la ultima letra del texto es: \""+ultima_letra_texto+"\"")

print("el texto al reves queda así:")
lista_texto.reverse()
print(" ".join(lista_texto))

Bool = "python" in texto
Dic = {True:"si esta",False:"no esta"}
print("python "+Dic[Bool]+ " en el texto")