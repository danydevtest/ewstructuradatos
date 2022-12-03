import time
def mostrarLista(lista, lon):
	listaordenada=""
	for i in range(0,lon):
		listaordenada+=str(lista[i])+" "
	print(listaordenada)   
	
arreglo = [5,2,4,1,3];

for i in range(1,len(arreglo)):
	clave = arreglo[i]
	j = i-1
	
	while (j>=0 and arreglo[j] > clave):
		arreglo[j+1] = arreglo[j]
		j = j-1
	arreglo[j+1] = clave
	mostrarLista(arreglo, len(arreglo))
mostrarLista(arreglo, len(arreglo))    

inicio = time.time()
time.sleep(1)
fin = time.time()
print("Tiempo de ejecucion: ",fin-inicio) 