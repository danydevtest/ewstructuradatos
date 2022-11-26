from random import randint
import time
def burbuja(numeros):
    intercambio=True
    while intercambio:
        intercambio=False
        for i in range(len(numeros)-1):
            if numeros [i]>numeros[i+1]:
                numeros[i],numeros[i+1]=numeros[i+1],numeros[i]
                intercambio=True 
                
listanumeros=[randint(1,100) for x in range(10000)]
inicio=time.time()
burbuja(listanumeros)
fin=time.time()
print(listanumeros)
print("Tiempo de ejecución es: ", fin-inicio )

