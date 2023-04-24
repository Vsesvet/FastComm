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
            journal.log("Error connection to db")

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
        journal.log(f"Select_one. Результат: {find_dict}")
        return find_dict

    def select_every(self, dct, table_name):
        """Находим строку (или несколько) по переданным параметрам в dct. На входе: {}, ''. На выходе [{}]"""
        content = ''
        for key, value in dct.items():
            i = f"{key} = '{value}' OR "
            content += i
        content = content[:-4]

        select_query = f'SELECT * FROM {table_name} WHERE {content}'
        journal.log(f"{select_query}")
        with self.connection.cursor() as cursor:
            cursor.execute(select_query)
            find_dict = cursor.fetchall()
            self.connection.commit()
        # journal.log(f"Select_every. Результат: {find_dict}")
        return find_dict

    def select_all(self, table_name):
        """Получение всех строк из базы данных"""
        select_all_rows = f"SELECT * FROM {table_name}"

        with self.connection.cursor() as cursor:
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
        # journal.log(f"SELECT_ALL. Результат: {select_all_rows}")
        return rows


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
            if value == None:
                continue
            i = f"{key} = '{value}', "
            content += i
        content = content[:-2] # срез последнего пробела и запятой

        request = f"UPDATE {table_name} SET {content} WHERE id = '{dct['id']}'"
        with self.connection.cursor() as cursor:
            cursor.execute(request)
            self.connection.commit()
        journal.log(f"UPDATE {table_name} SET {content} WHERE id = '{dct['id']}'")

    def delete_row(self, dct, table_name):
        """Функция удаления строки из таблицы. """
        for key, value in dct.items():
            ls = key
            rs = value
        request = f"DELETE FROM {table_name} WHERE {ls} = '{rs}'"
        with self.connection.cursor() as cursor:
            cursor.execute(request)
            self.connection.commit()
        journal.log(f'DELETE FROM {table_name} WHERE {ls} = {rs}')

    def find_partial_matching(self, dct, table_name):
        """Поиск по частичному совпадению параметров"""
        # SELECT * FROM table_name WHERE dct[key] LIKE 'some-date%'
        for key, value in dct.items():
            dct_key = key
            dct_value = '%' + value + '%'

        select_query = f"SELECT * FROM {table_name} WHERE {dct_key} LIKE '{dct_value}'"
        with self.connection.cursor() as cursor:
            cursor.execute(select_query)
            find_dict = cursor.fetchall()
            self.connection.commit()
        journal.log(f"Select_partial_matching: {find_dict}")
        return find_dict

    def select_by_range(self, dct, table_name):
        """Выбор данных между диапазоном дат"""
        # SELECT * from event_db.events where date_time >= '2023-03-25' and date_time < '2023-05-10'
        select_query = f"SELECT * FROM {table_name} WHERE date_time >= '{dct['start_date']}' AND date_time < '{dct['end_date']}'"
        with self.connection.cursor() as cursor:
            cursor.execute(select_query)
            find_dict = cursor.fetchall()
            self.connection.commit()
        # journal.log(f"Select_by_range. Результат: {find_dict}")
        return find_dict

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
            journal.log(f"Can not close connection due to absence openning connection")

journal = Journal()