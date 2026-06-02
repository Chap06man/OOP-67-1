class Animals:
    def speak(self):
        print('Издаёт звук')

    def body(self, color, razmer, tip):
        self.color = color
        self.razmer = razmer
        self.tip = tip
        print(self.color,self.razmer,self.tip)


class Dog(Animals):
    pass


dog = Dog()

dog.body('black', 2, 'zloy')
dog.speak()