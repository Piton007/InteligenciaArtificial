W1=0.84
W2=0.394
W3=0.783
Bias=0
factorAprendizaje=0.3
errorCuadraticoMedio=0.6

patrones=[]
file=open("patronesAdaline.txt","r")
for line in file.readlines():
    patrones.append([ int(valor) for valor in line.strip().split(",")])

def obtenerSumatoria(patron):
    return W1*patron[0]+W2*patron[1]+W3*patron[2]#+Bias

def actualizarPesos(patron,error):
    global W1,W2,W3,Bias
    W1=W1+factorAprendizaje*patron[0]*error
    W2=W2+factorAprendizaje*patron[1]*error
    W3=W3+factorAprendizaje*patron[2]*error
    #Bias=Bias+factorAprendizaje*error

erroAcumulado=0

for patron in patrones:
    error=abs(patron[-1]-obtenerSumatoria(patron))
    actualizarPesos(patron,error)
    erroAcumulado+=error**2
print("{:.3f} , {:.3f}, {:.3f}".format(W1,W2,W3))

     
   

