class Backpack:
    def __init__(self, owner, items, max_items):
        self.owner = owner
        self.items = items
        self.max_items = max_items

    def __str__(self):
        return f'<Backpack owner: {self.owner}, items: {len(self.items)}/{self.max_items}>'

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __bool__(self):
        return len(self.items) > 0

    def add_item(self, item):
        if len(self.items) < self.max_items:
            self.items.append(item)
            print(f'{item} добавлен')
        else:
            raise ValueError('Рюкзак полон')

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f'{item} удален')
        else:
            raise ValueError('Такого предмета нет')

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