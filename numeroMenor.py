def numeroMenor(lista):
    menor = lista[0]
    for numero in lista:  #En este FOR: numero = toma el valor de cada uno de los numeros del arreglo.
        if menor>numero:
            menor=numero
    return menor


arreglo=[0]

print('El numero menor del arreglo es:',numeroMenor(arreglo))
