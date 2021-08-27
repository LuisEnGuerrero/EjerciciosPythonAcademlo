# Programa para calcular el Sueldo por semana.
import sys

def computepay(horas, valorHora):

    valorExtra = valorHora*1.5

    if horas > 40:
        horaExtra=horas-40
        horasTrabajadas=40
    else:
        horasTrabajadas=horas
        horaExtra=0

    salarioTotal = (horasTrabajadas * valorHora) + (horaExtra * valorExtra)

    print('\nTrabajaste', horasTrabajadas, 'horas normales: \t$', horasTrabajadas * valorHora, '\ny:', horaExtra,
          'Horas Extras:\t$', horaExtra * valorExtra, '\n por lo que te corresponde como Salario la suma de:',
          salarioTotal)

    return salarioTotal

print('Calculadora de Salarios')
horasIndicadas = input('\nIngresa la cantidad de horas trabajadas en la semana: ')
valorHoras = input('\nIngresa el valor de la hora trabajada: ')

try:
    horasIndicadas=int(horasIndicadas)
    valorHoras = float(valorHoras)
except ValueError:
    mitad = -1
    print('Ingresa sólo números!!!')
    sys.exit()

computepay(horasIndicadas, valorHoras)
