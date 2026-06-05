import datetime

class Person:
    def __init__(self, name, birth_day, occupation, higher_edu):
        self.name = name
        self.__birth_day = birth_day
        self.__occupation = occupation
        self.__higher_edu = higher_edu
      
    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_edu(self):
        return self.__higher_edu

    @property
    def age(self):
        return self.age


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


class Friend(Person):
    def __init__(self,name, birth_day, occupation, higher_edu, hobby):
        super().__init__(name, birth_day, occupation, higher_edu)
        self.hobby = hobby

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


cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()


fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()
