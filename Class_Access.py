import sys
from db_config import *
from Class_Journal import *
from Class_Mysql import *

class Access:
    """Access module. Проверка данных Входа и роли пользователя, для совершения действия"""
    def __init__(self):
        self.mysql = Mysql()
    def login(self, input_phone, input_password):
        """Сверяет данные логина и пароля"""
        table_name = "users"
        db = self.mysql.select_all(table_name)
        for db_user in db:
            # Не верный пароль flag_access == 2.
            if db_user['phone_number'] == input_phone and db_user['password'] != input_password:
                journal.log(f"Попытка входа в систему. {db_user['second_name']} {db_user['first_name']} ({db_user['role_id']})"
                            f" Неверный пароль: {input_password}")
                flag_access = 2
                return db_user, flag_access

            # Если телефон и пароль верные то flag_access == 0.
            elif db_user['phone_number'] == input_phone and db_user['password'] == input_password:
                flag_access = 0
                journal.log(f"Успешный вход в систему. {db_user['second_name']} {db_user['first_name']} ({db_user['role_id']})")
                return db_user, flag_access

        # Если телефон не найден в БД то flag_access == 1.
        journal.log(f'Отклонен вход в систему: Логин: {input_phone}, Пароль: {input_password}.'
                    f'Не найден телефон в БД.')
        flag_access = 1
        db_user = 0
        journal.log(f'Отключение от базы данных')
        return db_user, flag_access

    def get_username_and_role(self, user_login):
        username = f"{user_login['second_name']} {user_login['first_name']}"
        role_name = self.mysql.get_role_by_role_id(user_login['role_id'])
        username_login_role = f'{username} ({role_name})'
        return username_login_role

    def check_role_sysadmin(self, user_login):
        """Проверка роли системного администратора"""
        role = user_login['role']
        if role == 'sysadmin':
            return True
        else:
            return False

    def check_role_admin(self, user_login):
        """Проверка роли Администратора пользователя для совершения действия"""
        role = user_login['role']
        if role == 'sysadmin':
            return True
        elif role == 'admin':
            return True
        else:
            return False

    def check_role_member(self, user_login):
        """Проверка роли - приндалежность к Участнику"""
        role = user_login['role']
        if role == 'participant':
            return True
        else:
            return False

    def check_role_inspector(self, user_login):
        """Проверка роли - принадлежность к Инспектору"""
        role = user_login['role']
        if role == 'inspector':
            return True
        else:
            return False


journal = Journal()
