class Backpack:
    def __init__(self,owner,items,max_items):
        self.owner = owner 
        self.items = items    
        self.max_items = max_items

    def __str__(self):
        return f'Владелец рюкзака: {self.owner}, items: {len(self.items)}/{self.max_items}'

    def __len__(self):
        return len(self.items)

    def __contains__(self,items):
        return items in self.items

    def __bool__(self):
        return len(self.items) > 0

    def add_item(self,i):
        if len(self.items) < self.max_items:
            self.items.append(i)
            print(f'{i} добавлен')
        else:
            print('Рюгзак полон')

    def remove_item(self,i):
        if i in self.items:
            self.items.remove(i)
            print(f'{i} удален')
        else:
            print('Такого предмета нет')

backpack = Backpack("Азамат", ["ручка", "тетрадь"], 5)

print(backpack) # <Backpack owner: Азамат, items: 2/5>
print(len(backpack)) # 2
backpack.add_item("книга")
backpack.add_item("телефон")

print("книга" in backpack) # True

backpack.remove_item("ручка")

if backpack:
    print("Рюкзак не пустой")
else:
    print("Рюкзак пустой")


