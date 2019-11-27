import numpy as np 
import functools

patrones=[]
file=open("Hopfield.txt",'r')
for line in file.readlines():
    patrones.append([ int(valor) for valor in line.strip().split(",")])

def obtenerMatrizPatron(patron):
    return np.dot(patron.T,patron)-np.identity(len(patrones[0]))



matrices=[]
for patron in patrones:
    npPatron=np.array([patron])
    matrices.append(obtenerMatrizPatron(npPatron))
matriz_Definitivo=functools.reduce(lambda v1,v2: v1+v2,matrices)

def obtenerSalida(entrada):
    return list(map(lambda valor: -1 if valor<0 else 1,np.dot(entrada,matriz_Definitivo).tolist()))

def obtenerPatronAsociado(patron):
    entrada=patron
    salida=obtenerSalida(entrada)
    while not np.array_equal(salida,entrada):
        entrada=salida
        salida=obtenerSalida(entrada)
    return salida
print(obtenerPatronAsociado([1,-1,-1,-1]))


