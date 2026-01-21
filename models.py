# Модель данных для хранения информации об автовладельцах

class CarOwner:
    # Класс для хранения информации об автовладельце и его автомобиле

    def __init__(self, last_name, first_name, patronymic, reg_number,
                 car_brand, engine_volume, manufacture_year, registration_year):
        # Инициализация объекта автовладельца
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.reg_number = reg_number
        self.car_brand = car_brand
        self.engine_volume = engine_volume
        self.manufacture_year = manufacture_year
        self.registration_year = registration_year

    def __str__(self):
        # Строковое представление объекта
        return f"{self.last_name} {self.first_name} {self.patronymic},Авто:{self.car_brand} {self.reg_number},Объем:{self.engine_volume}л,Выпуск:{self.manufacture_year}г,Учет:{self.registration_year}г"
