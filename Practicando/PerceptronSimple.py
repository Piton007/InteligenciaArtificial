import random 

W1=1
W2=1
Bias=0.5


patrones=[]
file=open("patronesPerceptronSimple.txt",'r')
for line in file.readlines():
    patrones.append([ int(valor) for valor in line.strip().split(",")])


def obtenerSalida(patron):
    sumatoria=W1*patron[0]+W2*patron[1]+Bias
    return -1 if sumatoria<0 else 1

def actualizarPesos(patron):
    global W1,W2,Bias
    W1=W1+patron[2]*patron[0]
    W2=W2+patron[2]*patron[1]
    Bias=Bias+patron[2]

for patron in patrones:
    while obtenerSalida(patron)!=patron[2]:
        actualizarPesos(patron)
    
print("Ecuacion hiperplano {}x1 + {}x2 + {}".format(W1*patrones[-1][0],W2*patrones[-1][1],Bias))

