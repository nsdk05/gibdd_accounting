# Модуль для работы с файлами: чтение и запись данных об автовладельцах

import os
from models import CarOwner

def read_owners_from_file(filename):
    # Чтение данных об автовладельцах из файла
    if not os.path.exists(filename):
        print(f"Ошибка:файл '{filename}' не найден.")
        return None

    owners=[]
    try:
        with open(filename,'r',encoding='utf-8') as file:
            for line_num,line in enumerate(file,1):
                line=line.strip()
                if not line:
                    continue

                parts=line.split(',')
                if len(parts)!=8:
                    print(f"Предупреждение:строка {line_num} имеет неверный формат:{line}")
                    continue

                try:
                    owner=CarOwner(
                        last_name=parts[0].strip(),
                        first_name=parts[1].strip(),
                        patronymic=parts[2].strip(),
                        reg_number=parts[3].strip(),
                        car_brand=parts[4].strip(),
                        engine_volume=float(parts[5].strip()),
                        manufacture_year=int(parts[6].strip()),
                        registration_year=int(parts[7].strip())
                    )
                    owners.append(owner)
                except ValueError as e:
                    print(f"Ошибка в строке {line_num}:{e}")
                    continue

        print(f"Успешно загружено {len(owners)} записей.")
        return owners

    except IOError as e:
        print(f"Ошибка при чтении файла:{e}")
        return None

def save_owners_to_file(filename,owners):
    # Сохранение данных об автовладельцах в файл
    try:
        with open(filename,'w',encoding='utf-8') as file:
            for owner in owners:
                file.write(f"{owner.last_name},{owner.first_name},{owner.patronymic},"
                          f"{owner.reg_number},{owner.car_brand},{owner.engine_volume},"
                          f"{owner.manufacture_year},{owner.registration_year}\n")
        print(f"Успешно сохранено {len(owners)} записей в файл '{filename}'.")
        return True
    except IOError as e:
        print(f"Ошибка при сохранении файла:{e}")
        return False
