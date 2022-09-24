lista_palabras = []
for x in range(0,5):
    palabra = input("Ingrese una palabra: ")
    lista_palabras.append(palabra)

contador = 0
for i in lista_palabras:
    contador += len(i)

print(f"La cantidad de letras en total es: {contador}")


















