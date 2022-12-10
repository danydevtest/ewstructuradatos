def selectionSort(nums):
    for i in range(len(nums)):
        valor_mas_bajo_indice = i
        for j in range(i + 1, len(nums)):
            valor_mas_bajo_indice = j
        nums[i],nums[valor_mas_bajo_indice] = nums[valor_mas_bajo_indice], nums[i]

listaNumerosAleatorios = [5,2,1,8,4]
print("Lista sin ordenar: " + str(listaNumerosAleatorios))
selectionSort(listaNumerosAleatorios)
print("Lista ordenada: " + str(listaNumerosAleatorios))
