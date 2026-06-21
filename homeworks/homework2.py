class Person:
    def __init__(self, name, birth_day, occupation, higher_edu):
        self.name = name
        self.birth_day = birth_day
        self.occupation = occupation
        self.higher_edu = higher_edu

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, "
            f"я родился {self.birth_day}, "
            f"работаю {self.occupation}"
        )


class Classmate(Person):
    def __init__(self, name, birth_day, occupation, higher_edu, group_name):
        super().__init__(name, birth_day, occupation, higher_edu)
        self.group_name = group_name

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, "
            f"я одногруппник, "
            f"родился {self.birth_day}, "
            f"работаю {self.occupation}, "
            f"моя группа: {self.group_name}"
        )


class Friend(Person):
    def __init__(self, name, birth_day, occupation, higher_edu, hobby):
        super().__init__(name, birth_day, occupation, higher_edu)
        self.hobby = hobby

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, "
            f"я друг, "
            f"родился {self.birth_day}, "
            f"работаю {self.occupation}, "
            f"моё хобби: {self.hobby}"
        )


# 2 объекта Classmate
classmate1 = Classmate(
    "Али", "12.05.2006", "Студент", False, "Python-67"
)

classmate2 = Classmate(
    "Бек", "20.08.2005", "Студент", True, "Python-67"
)

# 2 объекта Friend
friend1 = Friend(
    "Сардор", "01.01.2007", "Программист", True, "Футбол"
)

friend2 = Friend(
    "Эмир", "15.03.2006", "Дизайнер", False, "Игры"
)

# Вызов методов
classmate1.introduce()
classmate2.introduce()

friend1.introduce()
friend2.introduce()