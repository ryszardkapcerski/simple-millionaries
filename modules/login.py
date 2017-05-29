from database import Database
from passlib.hash import bcrypt


class Login(object):
    @staticmethod
    def check_login(username, password):
        user_data = Login.find_user(username)
        if user_data is not None and bcrypt.verify(password, user_data['password']):
            return True
        return False

    @staticmethod
    def create_account(username, password, admin):
        Database.insert('users', {'username': username, 'password': bcrypt.hash(password), 'admin': admin})

    @staticmethod
    def find_user(username):
        return Database.find_one(collection='users', query={'username': username})

    @staticmethod
    def check_admin(username):
        admin_data = Database.find_one(collection='users', query={'username': username, 'admin': True})
        if admin_data is not None:
            return True
        return False

    @staticmethod
    def register_admin():
        if_admin = input('Are you an admin?: ')
        if if_admin == 'yyy':
            return True
        return False
