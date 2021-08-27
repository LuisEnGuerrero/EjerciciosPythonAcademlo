texto=input('Escribe el texto que deseas trabajar: ')
textoArreglo=texto.split(' ')

palabra=input('\nAhora escribe la palabra del texto que deseas contabilizar: ')

totalPalabra={}

for item in textoArreglo:
    totalPalabra[item] = totalPalabra.get(palabra, 0) + 1

print('La palabra: "',palabra,'" se encuentra: ',totalPalabra[palabra],' veces en el texto: "',texto,'"')