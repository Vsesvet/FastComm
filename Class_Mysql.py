
from db_config import host, port, user, password, db_name

import pymysql
import pymysql.cursors

class Mysql:
    """Подключение и работа с базой данных MqSql"""
    def __init__(self, host, port, user, password, db_name):
        host = "127.0.0.1"
        port = 3306
        user = "root"
        password = "root"
        db_name = "logistics_db"
        try:
            self.connection = pymysql.connect(host=host, port=port, user=user, password=password, database=db_name, cursorclass=pymysql.cursors.DictCursor)
            print("Соединение с базой данных успешно проведено")
        except Exception as ex:
            print("Error connection to db")


    def select_all_data(self, table_name):
        """Получение всех строк из базы данных"""
        select_all_rows = f"SELECT * FROM {table_name}"

        with self.connection.cursor() as cursor:
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

            return rows


    def create_participant(self, phone_number, second_name, first_name, last_name, role, full_name, city, email, password, comment, disabled):
        """Добавление нового участника в базу данных MySql"""
        # Получаем role_id по role participant
        select_role_id = f"SELECT role_id FROM roles WHERE  role_name = '{role}'"
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
        select_role_id = f"SELECT role_id FROM roles WHERE  role_name = '{new_user['role']}'"
        with self.connection.cursor() as cursor:
            cursor.execute(select_role_id)
            result = cursor.fetchall()
            self.connection.commit()

        insert_query = f"INSERT INTO participant (phone_number, second_name, first_name, last_name, full_name, role_id, city, email, password, comment,disabled) \
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
            result = cursor.fetchall()
            self.connection.commit()
        for i in result:
            role_name = i.get('role_name')
        return role_name


    def get_participant_id(self, phone_number):
        """Получение ID участника по номеру телефона"""
        select_id = f"SELECT participant_id FROM participants WHERE phone_number = {phone_number}"
        with self.connection.cursor() as cursor:
            cursor.execute(select_id)
            result = cursor.fetchall()
            self.connection.commit()
        #print(result)
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
        self.connection.close()

