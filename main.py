# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:49:19 2020

@author: Carlos Garnica 
"""

'''
Carga de librerias y modulos necesarios
'''
from calculadora import Calculadora
from functools import reduce
import sys
from math import sqrt

'''
Cargamos los numeros dados como parametros por consola
'''
numbers = []

for i in range(1, len(sys.argv)):
    numbers.append(int(sys.argv[i]))
print(numbers)

print('CALCULADORA')
print('HECHA POR CARLOS A. GARNICA')
    
#instancia de la calculadora
calc = Calculadora(numbers)

#Obtemos la lista de numeros convertidos a entero cada uno de los elementos.
numbers = calc.get_numbers()

#Realizamos las operaciones
suma = calc.add(numbers)
resta = calc.substract(numbers)
multiplicacion = calc.multiply(numbers)
division = calc.divide(numbers)
mean = calc.mean(numbers)
power = calc.power(numbers[-1], numbers[:len(numbers) - 1]) #Se toma el ultimo elemento de la lista como exponente, este ultimo elemento no se calcula
root = calc.root(numbers[-1], numbers[:len(numbers) - 1]) #Se toma el ultimo elemento de la lista como indice de la raiz, este ultimo elemento no se calcula
numbers_copy = calc.get_numbers()

#Creamos una funcion matematica para calcular personalizada
operation = (lambda x, y : ((x + y) ** 2/(3)))
result_operator = calc.operate([operation], numbers, type_op= 'reduce')

#Creamos una segunda funcion matematica, una ecuacion cuadratica
'''
SEA x[0]: a, x[1]: b y x[2] :c, los demas valores despues del indice 3 se ignoran
'''
new_numbers = numbers[:3] #Solo se necesitan los primeros 3 valores de la lista para calculas la ecuacion cuadratica
cuadratic_eq = None
try:
    cuadratic_eq_op = lambda x: ((-x[1] + sqrt((x[1] ** 2) - (4 * x[0] * x[2])))/(2*x[0])), lambda x: ((-x[1] - sqrt((x[1] ** 2) - (4 * x[0] * x[2])))/(2*x[0]))
    cuadratic_eq = calc.operate(cuadratic_eq_op, new_numbers, ls = None)
except ValueError:
    #print('Los valores no tienen una solucion posible')
    cuadratic_eq = 'Los valores no tienen una solucion posible'
#Imprimimos los resultados en consola
print('Lista: {}'.format(numbers))
print('Suma: {}'.format(suma))
print('Resta: {}'.format(resta))
print('Multiplicacion: {}'.format(multiplicacion))
print('Division: {}'.format(division))
print('Promedio: {}'.format(mean))
print('Potencia: {}'.format(power))
print('Raiz: {}'.format(root))
print('Copia de lista: {}'.format(numbers_copy))
print('Operation: {}'.format(result_operator))
print('Ecuacion cuadratica: {}'.format(cuadratic_eq))