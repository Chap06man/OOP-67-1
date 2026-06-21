class Animal:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    @property
    def name(self):
        return self.__name 

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        self.__age = value

class Dog(Animal):
    def make_sound(self):
        return 'Гав-Гав'


class Cat(Animal):
    def make_sound(self):
        return'Мияу-Мияу'

dog = Dog("Алабай",2)
cat = Cat('Кошка',3)
print(dog.make_sound())
print(cat.make_sound())

dog.name = 'Барбос'
dog.age = 3

cat.name = "Джессика"
cat.age = 4

print(f"Имя Собаку:{dog.name}, Лет:{dog.age}")
print(f"Имя Кошку:{cat.name}, Лет:{cat.age}")