#from db_config import *
import pymysql


class Mysql:
    """Подключение и работа с базой данных MqSql"""
    def __init__(self):
        try:
            self.connection = pymysql.connect(host=host,
                                              port=port,
                                              user=user,
                                              password=password,
                                              database=database,
                                              cursorclass=pymysql.cursors.DictCursor)
            print("Соединение с базой данных: Статус OK")
        except Exception as ex:
            print("Error connection to db")


    def select_all_data(self, table_name):
        """Получение всех строк из базы данных"""
        select_all_rows = f"SELECT * FROM {table_name}"

        with self.connection.cursor() as cursor:
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

            return rows

    def find_selected(self, dct, table_name):
        """Находим строку (или несколько) по переданным параметрам в dct. На входе: {}, ''. На выходе [{}]"""
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
        return find_dict

    def find_several(self, dct, table_name):
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
        return find_dict

    def select_one_value(self, value1, dct, table_name):
        """Получение одного значения из row. На входе: '', {}, ''. На выходе: {} из row с одним значением"""
        for key, value in dct.items():
            column = key
            content = value
        request = f"SELECT {value1} FROM {table_name} WHERE {column} = {content}"
        with self.connection.cursor() as cursor:
            cursor.execute(request)
            selected_value = cursor.fetchone()
            self.connection.commit()
        return selected_value

    def insert_row_to_table(self, dictionary, table_name):
        """Добавление row в таблицу. На входе: {}, ''. Выход без возврата"""
        column = []
        content = []
        for key, value in dictionary.items():
            column.append(key)
            content.append(value)
        column = str(tuple(column)).replace("'", "")
        content = tuple(content)
        insert_query = f"INSERT INTO {table_name}{column} VALUES{content}"
        print(insert_query)
        with self.connection.cursor() as cursor:
            cursor.execute(insert_query)
            self.connection.commit()

    def create_participant(self, phone_number, second_name, first_name, last_name, role, full_name, city, email, password, comment, disabled):
        """Добавление нового участника в базу данных MySql"""
        # Получаем role_id по role participant
        select_role_id = f"SELECT role_id FROM roles WHERE role_name = '{role}'"
        with self.connection.cursor() as cursor:
            cursor.execute(select_role_id)
            result = cursor.fetchall()
            self.connection.commit()

        role_id = result[0]['role_id']

        insert_query = f"INSERT INTO participants (phone_number, second_name, first_name, last_name, full_name, role_id, city, email, password, comment,disabled) \
        VALUES('{phone_number}', '{second_name}', '{first_name}', '{last_name}', '{full_name}', {role_id}, '{city}', '{email}', '{password}', '{comment}',{disabled})"

        with self.connection.cursor() as cursor:
            cursor.execute(insert_query)
            self.connection.commit()

    def create_user(self, new_user):
        """Добавление нового пользователя в базу данных MySql"""
        select_role_id = f"SELECT role_id FROM roles WHERE role_name = '{new_user['role']}'"
        with self.connection.cursor() as cursor:
            cursor.execute(select_role_id)
            result = cursor.fetchall()
            self.connection.commit()

        insert_query = f"INSERT INTO users (phone_number, second_name, first_name, last_name, full_name, role_id, city, email, password, comment,disabled) \
        VALUES(" \
                       f"'{new_user['phone_number']}'," \
                       f" '{new_user['second_name']}'," \
                       f" '{new_user['first_name']}'," \
                       f" '{new_user['last_name']}'," \
                       f" '{new_user['full_name']}'," \
                       f" '{new_user['role_id']},'" \
                       f" '{new_user['city']}'," \
                       f" '{new_user['email']}'," \
                       f" '{new_user['password']}'," \
                       f" '{new_user['comment']}'," \
                       f" '{new_user['disabled']})"

        with self.connection.cursor() as cursor:
            cursor.execute(insert_query)
            self.connection.commit()

    def create_organization(self, new_org):
        print("here", new_org)
        insert_query = f"INSERT INTO organizations (organization_name, organization_INN, organization_KPP, phone_number) \
                VALUES(" \
                       f"'{new_org['organization_name']}'," \
                       f" '{new_org['organization_INN']}'," \
                       f" '{new_org['organization_KPP']}'," \
                       f" '{new_org['phone_number']}')"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(insert_query)
                self.connection.commit()
                print("New org inserted into database successfully")
        except Exception as ex:
            print("Error to add new org into database")

    def select_all(self, table_name):
        """Выбор всех строк из таблицы. Возвращает все строки"""
        select_all = f"SELECT * FROM {table_name};"
        with self.connection.cursor() as cursor:
            cursor.execute(select_all)
            result = cursor.fetchall()
            self.connection.commit()
        #print(result)
        return result

    def get_role_by_role_id(self, role_id):
        """Получение Роли по id"""
        select_role_name = f"SELECT role_name FROM roles WHERE role_id = {role_id}"
        with self.connection.cursor() as cursor:
            cursor.execute(select_role_name)
            result = cursor.fetchone()
            self.connection.commit()
        return result.get('role_name')


    def get_value_by_arg(self, value_request, dict, table_name):
        """(value_request - запрашиваемое значение, dict - словарь).
        Универсальная функция получения одного значения из row"""
        for key, value in dict.items():
            ls = key
            rs = value
        request = f"SELECT {value_request} FROM {table_name} WHERE {ls} = '{rs}'"
        print(request)
        with self.connection.cursor() as cursor:
            cursor.execute(request)
            responce = cursor.fetchall()
            self.connection.commit()
        for item in responce:
            # value2 = item
            value2 = item.get(value_request)
            print(f'Возвращаемое значение функции get_value_by_arg: {value2}')
        return value2

    def delete_row_by_arg(self, dict, table_name):
        """(dict - словарь, table_name - название таблицы).
        Универсальная функция удаления строки из таблицы"""
        print(dict)
        for key, value in dict.items():
            ls = key
            rs = value
        request = f"DELETE FROM {table_name} WHERE {ls} = '{rs}'"
        print(request)
        with self.connection.cursor() as cursor:
            cursor.execute(request)
            responce = cursor.fetchall()
            self.connection.commit()


    def update_row_by_arg(self, value, check, table_name):
        """СТАРАЯ ВЕРСИЯ ОБНОВЛЕНИЯ СТРОКИ"""
        for key, value in value.items():
            lsv = key
            rsv = value

        for key, value in check.items():
            ls = key
            rs = value

        request = f"UPDATE {table_name} SET {lsv} = '{rsv}' where {ls} = '{rs}'"

        with self.connection.cursor() as cursor:
            cursor.execute(request)
            self.connection.commit()

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

    def update_row_by_id(self, id, dict, table_name):
        """Функция обновления строки в таблице.
           id - значения первичного ключа строки, которую надо обновить,
           dict - устанавливаемые значения,
           table_name - наименование таблицы, в которой необходимо произвести изменения"""
        id_name = self.get_PK_by_table_name(table_name)
        content = ""

        for key, value in dict.items():
            i = f"{key} = '{value}', "
            content += i
        content = content[:-2] # срез последнего пробела и запятой

        request = f"UPDATE {table_name} SET {content} WHERE {id_name} = '{id}'"
        print(request)
        with self.connection.cursor() as cursor:
            cursor.execute(request)
            self.connection.commit()


    def get_participant_id(self, phone_number):
        """Получение ID участника по номеру телефона"""
        select_id = f"SELECT participant_id FROM participants WHERE phone_number = {phone_number}"
        with self.connection.cursor() as cursor:
            cursor.execute(select_id)
            result = cursor.fetchall()
            self.connection.commit()
        print(f'Sql-возврат запроса по участнику: {result}')
        result = result[0]['participant_id']
        return result

    def update_participant_by_id(self, id, values):
        """Обновление данных участника по id. (role_id по умолч. = 4)"""
        update_by_id = f"UPDATE participants SET phone_number = '{values[0]}' ,"  \
                       f"                        second_name  = '{values[1]}' ,"  \
                       f"                        first_name   = '{values[2]}' ,"  \
                       f"                        last_name    = '{values[3]}' ,"  \
                       f"                        full_name    = '{values[4]}' ,"  \
                       f"                        role_id      = '4'           ,"  \
                       f"                        email        = '{values[5]}' ,"  \
                       f"                        city         = '{values[6]}' ,"  \
                       f"                        password     = '{values[7]}' ,"  \
                       f"                        comment      = '{values[8]}'  WHERE participant_id = {id}"
        with self.connection.cursor() as cursor:
            cursor.execute(update_by_id)
            self.connection.commit()

    def delete_participant_by_id(self, id):
        """Удаление участника по id из таблицы participants"""
        delete_by_id = f"DELETE FROM participants WHERE participant_id = {id}"
        with self.connection.cursor() as cursor:
            cursor.execute(delete_by_id)
            self.connection.commit()

    def __del__(self):
        """Закрытие сессии соединения с базой данных"""
        try:
            self.connection.close()
        except Exception as ex:
            print("Can not close connection due to absence openning connection")