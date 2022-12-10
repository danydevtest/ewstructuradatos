def ordenamiento_burbuja(nums):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                intercambio = True

ListaNumerosAleatorios = [5,2,8,7,6,9]
ordenamiento_burbuja(ListaNumerosAleatorios)
print(ListaNumerosAleatorios)