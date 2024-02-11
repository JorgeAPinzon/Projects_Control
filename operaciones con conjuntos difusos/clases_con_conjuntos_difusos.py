#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 08:58:54 2024

@author: antiXLinux
"""
"""
class MiClase:
    def __init__(self, valor):      # funcion para inicializar los objetos que se han creado
        self.mi_variable = valor

# Crear un objeto de la clase
objeto = MiClase("Hola Mundo")
print(objeto.mi_variable)  # Imprime: Hola Mundo ,esto es un ejemplo clasico de objeto y funcion init 
"""        
class FzSets:
    def __init__(self, A=None, nA=None, B=None, nB=None):
        if A is None:
            self.A = dict()
        else:
            self.A = A
        if B is None:
            self.B = dict()
        else:
            self.B = B

        self.Anombre = nA
        self.Bnombre = nB

        self.complemento_A = dict()
        self.complemento_B = dict()
        self.union_AB = dict()
        self.interseccion_AB = dict()
        self.diferenciaAB = dict()
        self.diferenciaBA = dict()

        self.cambio_union = False
        self.cambio_interseccion = False
        self.cambio_complemento = False 

    def unionOP(self):
        if self.cambio_union:
            print ('El resultado de la operacion union es: ', self.union_AB)
        else:
            sa = set(self.A.keys())
            sb = set(self.B.keys())
            interseccionSet = sa.intersection(sb)

            for i in interseccionSet:
                self.union_AB[i] = max(self.A[i], self.B[i])
            for i in sa-interseccionSet:
                self.union_AB[i] = self.A[i]
            for i in sb-interseccionSet:
                self.union_AB[i] = self.B[i]

            print('El resultado de la operacion union es:', self.union_AB)
            
    def interseccionOP(self):
        if self.cambio_interseccion:
            print ('El resultado de la operacion intersección es: ', self.interseccion_AB)
        else:
            sa = set(self.A.keys())
            sb = set(self.B.keys())
            interseccionSet = sa.intersection(sb)

            for i in interseccionSet:
                self.interseccion_AB[i] = min(self.A[i], self.B[i])
            for i in sa-interseccionSet:
                self.interseccion_AB[i] = self.A[i]
            for i in sb-interseccionSet:
                self.interseccion_AB[i] = self.B[i]

            print('El resultado de la operacion interseccion es:', self.interseccion_AB)
    
    def complementoOP(self):
        if self.cambio_complemento:
            print ('El resultado de la operacion complemento A es: ', self.complemento_A)
            print ('El resultado de la operacion complemento B es: ', self.complemento_B)
        else:
            sa = set(self.A.keys())
            sb = set(self.B.keys())
            interseccionSet = sa.intersection(sb)

            for i in interseccionSet:
                self.complemento_A[i] = round(1 - self.A[i], 1)
            for i in interseccionSet:
                self.complemento_B[i] = round(1 - self.B[i], 1)
            

            print('El resultado de la operacion interseccion es:', self.complemento_A)
            print('El resultado de la operacion interseccion es:', self.complemento_B)
            
    def diferenciaOP(self):
        
        sa = set(self.A.keys())
        sb = set(self.B.keys())
        
        interseccionSet = sa.intersection(sb)
        
        self.diferenciaAB = {}
        self.diferenciaBA = {}
        
        for i in interseccionSet:
            a_val = self.A.get(i, 0)
            b_val = self.B.get(i, 0)
            self.diferenciaAB[i] = round(max(0, a_val - b_val), 1)
            self.diferenciaBA[i] = round(max(0, b_val - a_val), 1)
        
        print('El resultado de la diferencia A - B es:', self.diferenciaAB)
        print('El resultado de la diferencia B - A es:', self.diferenciaBA)
           
    
            

# Ejemplo de uso----------------------------------------------------------------------------------------------
    
#A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
#B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}
#A = {0.2: 1, 0.4: 1, 0.6: 1}
#B = {0.4: 1, 0.6: 1, 0.8: 1}   # aqui imprime 0.2 por que su grado de pertenencia es 1 (ver teoria)
#fz = FzSets(A, "A", B, "B")
#fz.unionOP()

#A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
#B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}
#fz = FzSets(A, "A", B, "B")
#fz.interseccionOP()       
            
#A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
#B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}
#fz = FzSets(A, "A", B, "B")
#fz.complementoOP()
            
A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}
fz = FzSets(A, "A", B, "B")
fz.diferenciaOP()   


    