class User:
    user_count  = 0
    default_password = "1234567890"

    def __init__(self,name,phone):
        self.name = name 
        self.phone = phone
        self.role = 'user'
        self.password = User.default_password
        User.user_count += 1 


    @classmethod
    def get_user_count(cls):
        return cls.user_count

    @classmethod
    def create_admin(cls,name,phone):
        user = User(name,phone)
        user.role = 'admin'
        user.password = 'qwerty123'
        return user

print(f'Всего пользователей: {User.user_count}')
user1 =User('Sardar','999777888555')
print(user1.password)
print(f'Всего пользователей: {User.user_count}')
admin1 = User.create_admin('Anel','996888777555')
print(User.create_admin)
print(User.get_user_count())
