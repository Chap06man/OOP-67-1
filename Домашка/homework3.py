from datetime import datetime  # импортируем модуль для работы с датой


class Person:
    def __init__(self, name, birth_day, occupation, higher_edu):
        self.name = name

        # сохраняем дату рождения как объект datetime
        self.__birth_day = datetime.strptime(birth_day, "%d.%m.%Y")

        # приватные атрибуты
        self.__occupation = occupation
        self.__higher_edu = higher_edu

    # получаем дату рождения
    @property
    def birth_day(self):
        return self.__birth_day.strftime("%d.%m.%Y")

    # получаем профессию
    @property
    def occupation(self):
        return self.__occupation

    # получаем информацию о высшем образовании
    @property
    def higher_edu(self):
        return self.__higher_edu

    # автоматически считаем возраст
    @property
    def age(self):
        today = datetime.today()
        age = today.year - self.__birth_day.year

        # если день рождения ещё не был в этом году,
        # уменьшаем возраст на 1
        if (today.month, today.day) < (self.__birth_day.month, self.__birth_day.day):
            age -= 1

        return age

    # информация о человеке
    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, "
            f"я родился {self.birth_day}, "
            f"работаю {self.occupation}"
        )


# класс одногруппника
class Classmate(Person):
    def __init__(self, name, birth_day, occupation, higher_edu, group_name):
        super().__init__(name, birth_day, occupation, higher_edu)
        self.group_name = group_name

    # переопределяем метод introduce
    def introduce(self):
        if self.higher_edu:
            education = "У меня есть высшее образование."
        else:
            education = "У меня нет высшего образования."

        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Я учился в группе {self.group_name}. "
            f"{education}"
        )


# класс друга
class Friend(Person):
    def __init__(self, name, birth_day, occupation, higher_edu, hobby):
        super().__init__(name, birth_day, occupation, higher_edu)
        self.hobby = hobby

    # переопределяем метод introduce
    def introduce(self):
        if self.higher_edu:
            education = "У меня есть высшее образование."
        else:
            education = "У меня нет высшего образования."

        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Моё хобби {self.hobby}. "
            f"{education}"
        )


# создаем объект одногруппника
cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()
print("Возраст:", cl1.age)

# создаем объект друга
fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()
print("Возраст:", fr1.age)