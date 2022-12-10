def orden_seleccion(nums):
    for i in range(len(nums)):
        valor_mas_bajo_indice = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[valor_mas_bajo_indice]:
                valor_mas_bajo_indice = j
        nums[i],nums[valor_mas_bajo_indice] = nums[valor_mas_bajo_indice], nums[i]

listaNumerosAleatorios = [5,2,1,8,4]
print("Lista sin ordenar: " + str(listaNumerosAleatorios))
orden_seleccion(listaNumerosAleatorios)
print("Lista ordenada: " + str(listaNumerosAleatorios))