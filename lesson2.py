class Car:
    def __init__(self,color,model):
        self.color = color 
        self.model = model 

    def drive_to(self,destination):
        print(f'Машина моделы {self.model} едет в {destination}')

    def change_color(self,new_color):
        self.color = new_color



class bus(Car):
    def drive_to(self, destination, color,number):
        return super().drive_to(destination)
        super().__init__(color)
        self.number = number





car_1 = Car('black','BMw')
print(car_1.color)
car_1.drive_to('Каракол')
car_1.change_color('blue')
print(car_1.color)
