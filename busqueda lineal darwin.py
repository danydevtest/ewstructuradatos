def busqueda_lineal(arr, n, x):
 
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1

arr = [1, 2, 3, 4, 5]
x = 5
n = len(arr)
position = busqueda_lineal(arr, n, x)
if(position == -1):
    print("El número no se ha encontrado")
else:
    print("El número está presente en la posicion", position)