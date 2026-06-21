# Класс для создания объектов человека
class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    # Метод представления человека
    def introduce(self):
        if self.higher_education:
            education = "высшее образование есть"
        else:
            education = "высшего образования нет"

        print(
            f"Меня зовут {self.name}, "
            f"я родился {self.birth_date}, "
            f"по профессии {self.occupation}, "
            f"{education}."
        )


# Создание экземпляров класса
person_1 = Person("Сардар", "15.12.2006", "Программист", True)
person_2 = Person("Ислам", "27.06.2007", "Хирург", False)
person_3 = Person("Санжар", "16.10.2007", "Юрист", True)

# Вывод атрибутов каждого экземпляра
print(person_1.name, person_1.birth_date, person_1.occupation, person_1.higher_education)
print(person_2.name, person_2.birth_date, person_2.occupation, person_2.higher_education)
print(person_3.name, person_3.birth_date, person_3.occupation, person_3.higher_education)

# Вызов метода introduce
person_1.introduce()
person_2.introduce()
person_3.introduce()