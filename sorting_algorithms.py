# Модуль с алгоритмами сортировки
# Используется сортировка обменом (пузырьковая сортировка)

def bubble_sort(arr,key_func):
    # Сортировка обменом (пузырьковая сортировка)
    n=len(arr)
    sorted_arr=arr.copy()

    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            if key_func(sorted_arr[j])>key_func(sorted_arr[j+1]):
                sorted_arr[j],sorted_arr[j+1]=sorted_arr[j+1],sorted_arr[j]
                swapped=True
        if not swapped:
            break
    return sorted_arr

def multi_key_bubble_sort(arr,key_funcs):
    # Сортировка по нескольким ключам с использованием сортировки обменом
    n=len(arr)
    sorted_arr=arr.copy()

    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            for key_func in key_funcs:
                key1=key_func(sorted_arr[j])
                key2=key_func(sorted_arr[j+1])

                if key1>key2:
                    sorted_arr[j],sorted_arr[j+1]=sorted_arr[j+1],sorted_arr[j]
                    swapped=True
                    break
                elif key1<key2:
                    break
        if not swapped:
            break
    return sorted_arr
