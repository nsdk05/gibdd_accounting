# Модуль с функциями меню и пользовательского интерфейса

import os
from reports import generate_report_1,generate_report_2,generate_report_3,display_report

def clear_screen():
    # Очистка экрана консоли
    os.system('cls' if os.name=='nt' else 'clear')

def get_int_input(prompt,min_value=None,max_value=None):
    # Безопасное получение целочисленного ввода от пользователя
    while True:
        try:
            value=int(input(prompt))
            if min_value is not None and value<min_value:
                print(f"Ошибка:значение должно быть не меньше {min_value}")
                continue
            if max_value is not None and value>max_value:
                print(f"Ошибка:значение должно быть не больше {max_value}")
                continue
            return value
        except ValueError:
            print("Ошибка:введите целое число.")

def get_year_input(prompt):
    # Получение корректного года от пользователя
    while True:
        try:
            year=int(input(prompt))
            if year<1900 or year>2100:
                print("Ошибка:введите корректный год (1900-2100).")
                continue
            return year
        except ValueError:
            print("Ошибка:введите целое число.")

def show_main_menu():
    # Отображение главного меню программы
    clear_screen()
    print("                 УЧЕТ В ГИБДД - ГЛАВНОЕ МЕНЮ           ")
    print("  1.Отчет 1:Полный список всех автомобилистов          ")
    print("  2.Отчет 2:Владельцы автомобилей ВАЗ                  ")
    print("  3.Отчет 3:Автомобили старше заданного года           ")
    print("  4.Выйти из программы                                 ")

    return get_int_input("\nВыберите пункт меню (1-4):",1,4)

def handle_report_1(owners):
    # Обработка запроса на отчет 1
    if not owners:
        print("\nОшибка:данные не загружены.")
        input("\nНажмите Enter для продолжения...")
        return

    sorted_owners=generate_report_1(owners)
    display_report("ОТЧЕТ 1:ПОЛНЫЙ СПИСОК АВТОМОБИЛИСТОВ\nСортировка:год постановки на учёт (по убыванию)+фамилия (по возрастанию)",
                  sorted_owners)
    input("\nНажмите Enter для продолжения...")

def handle_report_2(owners):
    # Обработка запроса на отчет 2
    if not owners:
        print("\nОшибка:данные не загружены.")
        input("\nНажмите Enter для продолжения...")
        return

    sorted_vaz_owners=generate_report_2(owners)
    display_report("ОТЧЕТ 2:ВЛАДЕЛЬЦЫ АВТОМОБИЛЕЙ ВАЗ\nСортировка:год выпуска (по убыванию)+объём двигателя (по возрастанию)+фамилия (по возрастанию)",
                  sorted_vaz_owners)
    input("\nНажмите Enter для продолжения...")

def handle_report_3(owners):
    # Обработка запроса на отчет 3
    if not owners:
        print("\nОшибка:данные не загружены.")
        input("\nНажмите Enter для продолжения...")
        return

    print("\nВведите год для фильтрации автомобилей.")
    print("Будут показаны автомобили,выпущенные ранее этого года.")
    year=get_year_input("Год выпуска (например,2015):")

    sorted_old_car_owners=generate_report_3(owners,year)
    display_report(f"ОТЧЕТ 3:АВТОМОБИЛИ СТАРШЕ {year} ГОДА\nСортировка:год выпуска (по убыванию)+марка автомобиля (по возрастанию)",
                  sorted_old_car_owners)
    input("\nНажмите Enter для продолжения...")

def show_welcome_message():
    # Отображение приветственного сообщения
    clear_screen()
    print("               ПРОГРАММА 'УЧЕТ В ГИБДД'              ")
    print("               Вариант 4 - Автовладельцы             ")
    print("Функции программы:                                  ")
    print(" 1.Полный список всех автомобилистов                 ")
    print(" 2.Список владельцев ВАЗ                             ")
    print(" 3.Список автомобилей старше заданного года          ")
    print("                                                    ")
    print("Используется сортировка обменом по нескольким ключам")
    input("\nНажмите Enter для начала работы...")
