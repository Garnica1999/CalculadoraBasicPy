# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:35:16 2020

@author: Carlos Garnica
"""

from functools import reduce

'''
Clase que permite calcular en base a las funciones preestablecidas dado un 
conjunto de numeros almancenados en una lista.

Con esta clase puedes armar tus propios calculos matematicos, como funciones seno,
calculo de la ecuacion cuadratica, funciones de calculo de areas, entre otros.
'''
class Calculadora:
    '''
    Constructor principal. Nos aseguramos que todos los numeros dados como
    argumentos en la consola esten convertidos a entero para evitar problemas
    posteriores con los tipos de datos de los elementos de la lista.
    Entrada:
        * numbers: Lista de numeros
    '''
    def __init__(self, numbers):
        self.__numbers = []
        for number in numbers:
            self.__numbers.append(int(number))
        
    '''
    Metodo que permite contruir funciones matematicas utilizando funciones 
    anonimaso lambda.
    Entradas:
        * Operations: Lista de funciones lambda. En caso de que solo este 
        usando una funcion lambda puede ingresarla a una lista, y esta 
        ingresarla como entrada.
        * Numbers: Lista de numeros a utilizar.
        * Type_op: Sobre las funciones lamba hay multiples operaciones (map, 
        reduce y filter). Puede utilizar cada una de ella depende de lo que 
        desea obtener como
        salida en la funcion matematica que ha construido.
        * ls: Algunos tipos de operaciones de las funciones anonimas devuelven 
        objetos de tipo map o filter. Este argumento indica si estas clases se 
        convierten diredctamente a una lista con los nuevos numeros.
    Salida:
        Este metodo devuelve una lista con los calculos realizados.
    '''
    def operate(self, operations, numbers, type_op=None, ls = True):
        #La operacion no puede ser None
        if operations is None:
            raise TypeError('Las variable operation no puede ser NoneType')
        tup = []
        #Para cada funcion lambda de la lista de operaciones...
        for operation in operations:
            #Se compara que tipo de operacion desea realizar
            if type_op is None:
                tup.append(operation(numbers))
            elif type_op == 'map':
                mp = map(operation, numbers)
                if ls is True:
                    tup.append(list(mp))
                else:
                    tup.append(mp)
            elif type_op == 'reduce':
                tup.append(reduce(operation, numbers))
            elif type_op == 'filter':
                fil = filter(operation, numbers)
                if ls is True:
                    tup.append(list(fil))
                else:
                    tup.append(fil)
                    
        return tup
    '''
    Se suman todos los elementos de la lista
    Entrada:
        * numbers: Lista de numeros
    Salida:
        Retorna la sumatoria de todos los elementos de la lista dada como entrada
    '''
    def add(self, numbers):
        suma = reduce(lambda x, y: x + y, numbers)
        return suma
    '''
    Se restan todos los elementos de la lista
    Entrada:
        * numbers: Lista de numeros
    Salida:
        Retorna la resta de todos los elementos de la lista dada como entrada
    '''
    def substract(self, numbers):
        resta = reduce(lambda x, y: x - y, numbers)
        return resta
    '''
    Metodo que multiplica todos los elementos de la lista
    Entrada:
        * numbers: Lista de numeros
    Salida:
        Retorna el resultado de la multiplicacion de todos los numeros xn-1 * xn
        hasta terminar la lista.
    '''
    def multiply(self, numbers):
        mult = reduce(lambda x, y: x * y, numbers)
        return mult
    '''
    Metodo que divide todos los elementos de la lista
    Entrada:
        * numbers: Lista de numeros
    Salida:
        Retorna el resultado de la division de todos los numeros xn-1 * xn
        hasta terminar la lista.
    '''
    def divide(self, numbers):
        divide = reduce(lambda x, y: x / y, numbers)
        return divide
    '''
    Metodo que calcula el promedio de todos los numeros de la lista
    Entrada:
        * numbers: Lista de numeros
    Salida:
        Retorna el promedio o la media de todos los numeros de la lista dada
        por la entrada.
    '''
    def mean(self, numbers):
        suma = self.add(numbers)
        return suma / len(numbers)
    '''
    Para cada elemento de la lista calcula el exponente dado un numero exponente.
    Entrada:
        * numbers: Lista de numeros
        * n: Exponente
        * ls: Argumento de decision que tiene como funcion retornar si se desea
        obtener un objeto de la clase map o una lista con los numeros calculados
    Salida:
        Retorna el resultado de la multiplicacion de todos los numeros xn-1 * xn
        hasta terminar la lista.
    '''
    def power(self, n, numbers, ls = True):
        power = map(lambda x: x ** n, numbers)
        if ls is True:
            return list(power)
        else:
            return power
    '''
    Para cada numerod e la lista se calcula la raiz n.
    Entrada:
        * n: Radical o indice de la raiz
        * numbers: Lista con cada radicando de la raiz
        * ls: Argumento que se utiliza como decision para devolver una lista
        de numeros con los resultados o un objeto de la instancia map
    '''
    def root(self, n, numbers, ls = True):
        if len(numbers) == 1:
            root = lambda x : x[0] ** (1/n)
        elif len(numbers) > 1: 
            root = map(lambda x: x ** (1/n), numbers)
        if ls is True:
            return list(root)
        else:
            return root
    '''
    Metodo que devuelve la lista de numeros convertida al instanciar un objeto
    de esta clase.
    '''
    def get_numbers(self):
        return self.__numbers