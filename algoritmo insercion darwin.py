def algoritmo_insercion(nums):
    for i in range(1, len(nums)):
        elemento_a_insertar = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > elemento_a_insertar:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = elemento_a_insertar

ListaNumerosAleatorios = [9,2,6,4,7,3,5]
print("Lista sin ordenar: " + str(ListaNumerosAleatorios))
algoritmo_insercion(ListaNumerosAleatorios)
print("Lista ordenada: " + str(ListaNumerosAleatorios))