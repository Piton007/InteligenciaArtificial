import numpy as np 

pesos=np.array([[0.2,0.8],[0.6,0.4],[0.5,0.7],[0.9,0.3]])
factorAprendizaje=0.6

patrones=[]
file=open("Som.txt",'r')
def actualizarPesosGanador(ganador,patron):
    global pesos
    for i in range(len(pesos)):
        for j in range(len(pesos)):
            if j==ganador:
                pesos[i][j]=pesos[i][j]+factorAprendizaje*(patron[i]-pesos[i][j])
for line in file.readlines():
    patrones.append([ int(valor)for valor in line.strip().split(",")])
for patron in patrones:
    pesosNeurona1=pesos[:,0]
    pesosNeurona2=pesos[:,1]
    DistanciaNeurona1=np.sum(np.power(np.subtract(patron,pesosNeurona1),2))
    DistanciaNeurona2=np.sum(np.power(np.subtract(patron,pesosNeurona2),2))
    ganador= 0 if  DistanciaNeurona1<DistanciaNeurona2 else 1
    actualizarPesosGanador(ganador,patron)
