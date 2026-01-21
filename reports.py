# Модуль для генерации различных отчетов

from sorting_algorithms import multi_key_bubble_sort

def generate_report_1(owners):
    # Генерация отчета 1:Полный список всех автомобилистов
    if not owners:
        return []

    key_funcs=[
        lambda x:-x.registration_year,
        lambda x:x.last_name.lower()
    ]

    return multi_key_bubble_sort(owners,key_funcs)

def generate_report_2(owners):
    # Генерация отчета 2:Список всех владельцев автомобилей ВАЗ
    if not owners:
        return []

    vaz_owners=[]
    vaz_brands=['ваз','lada','лада']

    for owner in owners:
        if owner.car_brand.lower() in vaz_brands:
            vaz_owners.append(owner)

    if not vaz_owners:
        return []

    key_funcs=[
        lambda x:-x.manufacture_year,
        lambda x:x.engine_volume,
        lambda x:x.last_name.lower()
    ]

    return multi_key_bubble_sort(vaz_owners,key_funcs)

def generate_report_3(owners,year_threshold):
    # Генерация отчета 3:Список всех владельцев автомобилей с годом выпуска ранее заданного
    if not owners:
        return []

    old_car_owners=[owner for owner in owners if owner.manufacture_year<year_threshold]

    if not old_car_owners:
        return []

    key_funcs=[
        lambda x:-x.manufacture_year,
        lambda x:x.car_brand.lower()
    ]

    return multi_key_bubble_sort(old_car_owners,key_funcs)

def display_report(report_title,owners_list):
    # Отображение отчета в консоли
    print(f"\n{'='*60}")
    print(f"{report_title}")
    print(f"{'='*60}")

    if not owners_list:
        print("Нет данных для отображения.")
        return

    for i,owner in enumerate(owners_list,1):
        print(f"{i:3}.{owner}")
    print(f"\nВсего записей:{len(owners_list)}")
