class Hero:
    def __init__(self,name,lvl,hp):
        self.hero_name = name 
        self.hero_name = lvl 
        self.hero_name = hp 
    
    def action(self):
        print(f"{self.hero_name} Bace action")

    def rest(self):
        print(f"{self.hero_name} rest !!")

naruto = Hero('Naruto',100,1000)
saske = Hero('Asuna',111,1111)

naruto.action()
saske.rest()
print()