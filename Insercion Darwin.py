from random import randint
import time
def insercion(A):
    for i in range(len(A)):
        for j in range(i,0,-1):
            if(A[j-1] > A[j]):
                aux=A[j];
                A[j]=A[j-1];
                A[j-1]=aux;
    print (A)

#Programa Principal
A=[randint(1,5) for x in range(100)];
print (A);
insercion(A);
inicio=time.time()
insercion(A)
fin=time.time()
print(A)
print("Tiempo de ejecución es: ", fin-inicio )