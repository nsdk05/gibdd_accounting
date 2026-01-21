# Главный модуль программы "Учёт в ГИБДД"
# Координация работы всех компонентов системы

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from file_operations import read_owners_from_file
from menu import show_welcome_message, show_main_menu, handle_report_1, handle_report_2, handle_report_3


def create_sample_database(filename="car_owners_db.txt"):
    # Создание тестовой базы данных с 25 записями
    sample_data = [
        "Иванов,Иван,Иванович,А123ВС,Toyota,2.0,2015,2020",
        "Петров,Петр,Петрович,В234СД,Honda,1.6,2018,2021",
        "Сидоров,Сидор,Сидорович,С345ДФ,Nissan,2.5,2016,2019",
        "Кузнецов,Алексей,Викторович,Е456ФГ,ВАЗ,1.6,2010,2015",
        "Смирнов,Дмитрий,Александрович,Ж567ГХ,ВАЗ,1.4,2012,2017",
        "Алексеев,Андрей,Сергеевич,З678ХЦ,ВАЗ,1.6,2014,2018",
        "Борисов,Борис,Борисович,И789ЦЧ,Lada,1.4,2011,2016",
        "Васильев,Василий,Васильевич,К890ЧШ,ВАЗ,1.8,2013,2019",
        "Григорьев,Григорий,Григорьевич,Л901ШЩ,лада,1.6,2009,2014",
        "Дмитриев,Дмитрий,Дмитриевич,М012ЩЪ,Lada,1.4,2015,2020",
        "Егоров,Егор,Егорович,Н123ЪЫ,Volkswagen,1.8,2005,2010",
        "Жуков,Жук,Жукович,П234ЫЬ,Ford,2.0,2007,2012",
        "Зайцев,Захар,Захарович,Р345ЬЭ,Opel,1.6,2003,2008",
        "Ильин,Илья,Ильич,С456ЭЮ,ВАЗ,1.5,2000,2005",
        "Кириллов,Кирилл,Кириллович,Т567ЮЯ,Chevrolet,1.4,2008,2013",
        "Лебедев,Леонид,Леонидович,У678ЯА,Mazda,2.2,2017,2022",
        "Михайлов,Михаил,Михайлович,Ф789АБ,ВАЗ,1.7,2019,2023",
        "Николаев,Николай,Николаевич,Х890БВ,Hyundai,1.6,2014,2019",
        "Олегов,Олег,Олегович,Ц901ВГ,Kia,1.8,2016,2021",
        "Павлов,Павел,Павлович,Ч012ГД,ВАЗ,1.4,2011,2016",
        "Романов,Роман,Романович,Ш123ДЕ,Skoda,1.6,2012,2017",
        "Сергеев,Сергей,Сергеевич,Щ234ЕЖ,ВАЗ,1.8,2008,2013",
        "Тарасов,Тарас,Тарасович,Ъ345ЖЗ,Lada,1.6,2017,2022",
        "Устинов,Устин,Устинович,Ы456ЗИ,Volvo,2.0,2015,2020",
        "Федоров,Федор,Федорович,Ь567ИЙ,ВАЗ,1.4,2013,2018",
        "Харитонов,Харитон,Харитонович,Э678ЙК,ВАЗ,1.6,2010,2015"
    ]

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for line in sample_data:
                f.write(line + '\n')
        print(f"Создана тестовая база данных:{filename}")
        print(f"Добавлено {len(sample_data)} записей.")
        return True
    except IOError as e:
        print(f"Ошибка при создании базы данных:{e}")
        return False


def main():
    # Главная функция программы
    show_welcome_message()

    db_filename = "car_owners_db.txt"

    if not os.path.exists(db_filename):
        print(f"\nБаза данных '{db_filename}' не найдена.")
        print("Создаем тестовую базу данных...")
        if not create_sample_database(db_filename):
            print("Ошибка:не удалось создать базу данных.")
            input("Нажмите Enter для выхода...")
            return

    print(f"\nЗагрузка данных из файла '{db_filename}'...")
    owners = read_owners_from_file(db_filename)

    if not owners:
        print("Ошибка:не удалось загрузить данные.")
        input("Нажмите Enter для выхода...")
        return

    while True:
        try:
            choice = show_main_menu()

            if choice == 1:
                handle_report_1(owners)
            elif choice == 2:
                handle_report_2(owners)
            elif choice == 3:
                handle_report_3(owners)
            elif choice == 4:
                print("\nСпасибо за использование программы 'Учет в ГИБДД'!")
                print("До свидания!")
                break

        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            break
        except Exception as e:
            print(f"\nПроизошла неожиданная ошибка:{e}")
            input("Нажмите Enter для продолжения...")


if __name__ == "__main__":
    main()
