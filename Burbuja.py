def burbuja(numeros):
    intercambio=True
    while intercambio:
        intercambio=False
        for i in range(len(numeros)-1):
            if numeros [i]>numeros[i+1]:
                numeros[i],numeros[i+1]=numeros[i+1],numeros[i]
                intercambio=True 