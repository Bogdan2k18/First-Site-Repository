import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
class loginForm(FlaskForm):
    username = StringField('Логин')
    password = PasswordField('Пароль')

class registerForm(FlaskForm):
    username = StringField('Логин ')
    password = PasswordField('Пароль ')
    phone_number = IntegerField('Номер телефона: +380 -')
    address = StringField('Електронная почта ')


def get_gallary():
    files = os.listdir("static/images/gallary")
    images = filter(lambda x: x.endswith('.jpg'), files) 
    return images


user_list = []

class User():
    def __init__(self, name, password, phone = '', address = ''):
        self.name = name
        self.password = password
        self.phone = phone
        self.address = address
        self.status = self.check_all()
    def check(self):
        for user in user_list:
            if user.name == self.name:
                return True
        return False
    def check_all(self):
        for user in user_list:
            if user.name == self.name and user.password == self.password:
                return True
        return False
    @staticmethod
    def add_new(name, password, phone, address):
        try:
            phone = int(phone)
        except:
            return ["Введены неверные данные (номер телефона)", True, "#fc9b55"]
        if name.strip() != "" and password.strip() != "" and address.strip() != "":
            user = User(name, password)
            if not user.status:
                user_list.append(user)
                return ["Аккаун зарегистрирован успешно", False, '#42f46e']
            else:
                return ["Данный пользователь уже зарегистрирован", True, '#e8f441']
        else:
            return ["Введены неверные данные", True, '#fc7d58']
user_list.append(User('Bogdan', '12345'))