# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

# Ejemplo para mostrar la 
# Unión de conjuntos difusos 

# UNION DE CONJUNTOS DIFUSOS 
"""
A = dict()
B = dict()
Y = dict()

A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}


print('El primer conjunto difuso es:' ,A)
print('El segundo conjunto difuso es: ',B)

for A_key, B_key in zip(A, B):
    A_valor = A[A_key]
    B_valor = B[B_key]
    
    if A_valor > B_valor:
        Y[A_valor] = A_valor
    else: 
        Y[B_valor])   = B_valor
        
print('La union del conjunto difuso es: ', Y) 
# Ojo tener en cuenta que no imprime en la consola de manera igual
"""
"""
# INTERSECCION DE CONJUNTOS DIFUSOS
# Ejemplo para mostrar la interseccion
# de conjuntos difusos

A = dict()
B = dict()
Y = dict()   

A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}
Y = []

print('El primer conjunto difuso es:' ,A)
print('El segundo conjunto difuso es: ',B)

for A_key, B_key in zip(A, B):
    A_valor = A[A_key]
    B_valor = B[B_key]
    
    if A_valor < B_valor:
        Y.append(A_valor) # agrega elementos en una lista existente, resumiendo no deja que se sobreescriban cod original  
    else: 
        Y.append(B_valor)
        
print('La interseccion del conjunto difuso es: ',Y)           
"""
"""
# COMPLEMENTO DE CONJUNTOS DIFUSOS
# Ejemplo para mostraR el complemento
# de conjuntos difusos

A = dict()
Y = dict()

A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}


print('El primer conjunto difuso es:' ,A)

for A_key in A:
    Y[A_key] = 1 - A[A_key]
    
    
print('El complemento del conjunto difuso es: ', Y )
"""

# DIFERENCIA DE CONJUNTOS DIFUSOS
# Ejemplo para mostraR la diferencia 
# de conjuntos difusos

A = dict()
B = dict()
Y = dict()

A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}
Y =[]


print('El primer conjunto difuso es:' ,A)
print('El segundo conjunto difuso es: ',B)

for A_key, B_key in zip(A, B):
    A_valor = A[A_key]
    B_valor = B[B_key]
    B_valor = 1 - B_valor
    
    if A_valor < B_valor:
        Y.append(A_valor)
    else: 
        Y.append(round(B_valor, 1)) # l resultado no es exactamente 0.1,  debido a  flotante se redondea a un significativo
        
print('La diferencia de conjuntos difusos es: ', Y )
   
    




























