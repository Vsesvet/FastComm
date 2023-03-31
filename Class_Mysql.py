from db_config import *
import pymysql
from Class_Journal import *


class Mysql:
    """Подключение и работа с базой данных MqSql"""
    def __init__(self):
        """Подключение к базе данных."""
        try:
            self.connection = pymysql.connect(host=host,
                                              port=port,
                                              user=user,
                                              password=password,
                                              database=database,
                                              cursorclass=pymysql.cursors.DictCursor)
            # print("Обращение к базе данных: Статус OK")
        except Exception as ex:
            print("Error connection to db")

    def select_one(self, dct, table_name):
        """Находим строку по переданным параметрам в dct. На входе: {}, ''. На выходе {}"""
        content = ''
        for key, value in dct.items():
            i = f"{key} = '{value}' AND "
            content += i
        content = content[:-5]

        select_query = f'SELECT * FROM {table_name} WHERE {content}'
        with self.connection.cursor() as cursor:
            cursor.execute(select_query)
            find_dict = cursor.fetchone()
            self.connection.commit()
        journal.log(f"Выборка из БД, функция select_one. Результат: {find_dict}")
        return find_dict

    def select_every(self, dct, table_name):
        """Находим строку (или несколько) по переданным параметрам в dct. На входе: {}, ''. На выходе [{}]"""
        content = ''
        for key, value in dct.items():
            i = f"{key} = '{value}' OR "
            content += i
        content = content[:-4]

        select_query = f'SELECT * FROM {table_name} WHERE {content}'
        print(select_query)
        with self.connection.cursor() as cursor:
            cursor.execute(select_query)
            find_dict = cursor.fetchall()
            self.connection.commit()
        journal.log(f"Выборка из БД, функция select_every. Результат: {find_dict}")
        return find_dict

    def select_all(self, table_name):
        """Получение всех строк из базы данных"""
        select_all_rows = f"SELECT * FROM {table_name}"

        with self.connection.cursor() as cursor:
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

            return rows
        journal.log(f"SELECT_ALL. Результат: {select_all_rows}")

    def insert_row(self, dct, table_name):
        """Добавление row в таблицу. На входе: {}, ''. Выход без возврата"""
        column = []
        content = []
        for key, value in dct.items():
            column.append(key)
            content.append(value)
        column = str(tuple(column)).replace("'", "")
        content = tuple(content)
        insert_query = f"INSERT INTO {table_name}{column} VALUES{content}"
        with self.connection.cursor() as cursor:
            cursor.execute(insert_query)
            self.connection.commit()
        journal.log(f"В таблицу {table_name} добавлена новая запись {content}")

    def update_row(self, dct, table_name):
        """Универсальная функция обновления row в таблице"""
        content = ""
        for key, value in dct.items():
            i = f"{key} = '{value}', "
            content += i
        content = content[:-2] # срез последнего пробела и запятой

        request = f"UPDATE {table_name} SET {content} WHERE id = '{dct['id']}'"
        print(request)
        with self.connection.cursor() as cursor:
            cursor.execute(request)
            self.connection.commit()

    def delete_row(self, dct, table_name):
        """Функция удаления строки из таблицы. """
        print(dct)
        for key, value in dct.items():
            ls = key
            rs = value
        request = f"DELETE FROM {table_name} WHERE {ls} = '{rs}'"
        print(request)
        with self.connection.cursor() as cursor:
            cursor.execute(request)
            self.connection.commit()

    # def create_user(self, new_user):
    #     """Добавление нового пользователя в базу данных MySql"""
    #     select_role_id = f"SELECT role_id FROM roles WHERE role_name = '{new_user['role']}'"
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(select_role_id)
    #         result = cursor.fetchone()
    #         self.connection.commit()
    #
    #     insert_query = f"INSERT INTO users (phone_number, second_name, first_name, last_name, full_name, role_id, city, email, password, comment,disabled) \
    #     VALUES(" \
    #                    f"'{new_user['phone_number']}'," \
    #                    f" '{new_user['second_name']}'," \
    #                    f" '{new_user['first_name']}'," \
    #                    f" '{new_user['last_name']}'," \
    #                    f" '{new_user['full_name']}'," \
    #                    f" '{new_user['role_id']},'" \
    #                    f" '{new_user['city']}'," \
    #                    f" '{new_user['email']}'," \
    #                    f" '{new_user['password']}'," \
    #                    f" '{new_user['comment']}'," \
    #                    f" '{new_user['disabled']})"
    #
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(insert_query)
    #         self.connection.commit()

    def get_role_by_role_id(self, role_id):
        """Получение Роли по id"""
        select_role_name = f"SELECT role_name FROM roles WHERE id = {role_id}"
        with self.connection.cursor() as cursor:
            cursor.execute(select_role_name)
            result = cursor.fetchone()
            self.connection.commit()
        return result.get('role_name')

    def get_PK_by_table_name(self, table_name):
        """Функция возвращающая наименование первичного ключа по наименованию таблицы"""
        id_name_request = f"SELECT KU.table_name as TABLENAME,column_name as PRIMARYKEYCOLUMN " \
                          f"FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS TC INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS KU " \
                          f"ON TC.CONSTRAINT_TYPE = 'PRIMARY KEY'  " \
                          f"AND TC.CONSTRAINT_NAME = KU.CONSTRAINT_NAME  " \
                          f"AND KU.table_name='{table_name}'"

        with self.connection.cursor() as cursor:
            cursor.execute(id_name_request)
            id_name = cursor.fetchone()
            self.connection.commit()

        id_name = id_name['PRIMARYKEYCOLUMN']
        return id_name


    def __del__(self):
        """Закрытие сессии соединения с базой данных"""
        try:
            self.connection.close()
        except Exception as ex:
            print("Can not close connection due to absence openning connection")

journal = Journal()