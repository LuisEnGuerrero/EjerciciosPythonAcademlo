def numeroMayor(lista):
    mayor = -1
    for numero in lista:
        if mayor<numero:
            mayor=numero
    return mayor

arreglo=[45,65,84,75,96,54,85,22,35,36,54,95,86,75,32,15,45]

print('El numero mayor del arreglo es:',numeroMayor(arreglo))


"""
while True:
    number=float(input('Ingresa tu lista de numeros, escribe "0" para terminar: '))
    if number!=0:
        numeroMayor(number)
    else:
        break
"""