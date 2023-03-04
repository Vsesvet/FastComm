# Запросы:

# f"SELECT * FROM {table_name}"
# f"SELECT phone_number FROM {table_name}"
# f"SELECT * FROM worker WHERE phone_number = '89771234567' AND password = 'gnt6alwe'"
# f"SELECT phone_number, second_name, first_name FROM {table_name}"
# f"SELECT * FROM users WHERE role_id > 1"
# f"SELECT COUNT(*) FROM {table_name}"
# f"SELECT * FROM participants ORDER BY DESC" - в порядке убывания
# f"SELECT * FROM participants ORDER BY second_name, first_name"

# f"INSERT INTO {table_name}{column} VALUES{content}"
# f"INSERT INTO participants (phone_number, second_name...) VALUES ('89777194310', 'Ефремов'...)"

# UPDATE users SET age = '18', country = 'Россия' WHERE id = '3';
# f"UPDATE {table_name} SET {content} WHERE {id_name} = '{id}'"

# DELETE FROM users WHERE id = '10';


# ==========================================================================================
#                                       SELECT функции:
# ==========================================================================================
def select_all_data(self, table_name):
    """Получение всех строк из базы данных. На входе: ''. На выходе [{}, {}, ...]"""
    select_query = f"SELECT * FROM {table_name}"
    with self.connection.cursor() as cursor:
        cursor.execute(select_query)
        rows = cursor.fetchall()
    return rows


def find_selected(self, dct, table_name):
    """Находим строку (или несколько) по переданным параметрам в dct. На входе: {}, ''. На выходе [{}, {}, ...]"""
    content = ''
    for key, value in dct.items():
        i = f"{key} = '{value}' AND "
        content += i
    content = content[:-5]

    select_query = f'SELECT * FROM {table_name} WHERE {content}'
    with self.connection.cursor() as cursor:
        cursor.execute(select_query)
        find_list = cursor.fetchall()
    return find_list


def select_one_value(value1, dct, table_name):
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


def get_PK_by_table_name(self, table_name):
    """Функция возвращающая наименование первичного ключа по наименованию таблицы"""
    id_name_request = f"SELECT KU.table_name as TABLENAME, column_name as PRIMARYKEYCOLUMN " \
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


def select_count(self, table_name):
    select_query = f"SELECT COUNT(*) FROM {table_name}"
    with self.connection.cursor() as cursor:
        cursor.execute(select_query)
        count = cursor.fetchall()
    return count

# ==========================================================================================
#                                       INSERT функции
# ==========================================================================================
def insert_row_to_table(dictionary, table_name):
    """Добавление row в таблицу. На входе: {}, ''. Выход без возврата"""
    column = []
    content = []
    for key in dictionary.keys():
        column.append(key)
    for value in dictionary.values():
        content.append(value)

    column = str(tuple(column)).replace("'", "")
    content = tuple(content)
    insert_query = f"INSERT INTO {table_name}{column} VALUES{content};"
    print(insert_query)

    with self.connection.cursor() as cursor:
        cursor.execute(insert_query)
        self.connection.commit()

# ==========================================================================================
#                                       UPDATE функции
# ==========================================================================================

def update_row_by_id(self, id, dict, table_name):
    """Обновление row в таблице. На входе: {}, {}, ''. Выход без возврата
       id - ключ и значение первичного ключа строки, которую надо обновить,
       dict - устанавливаемые значения,
       table_name - наименование таблицы, в которой необходимо произвести изменения"""
    id_name = self.get_PK_by_table_name(table_name)
    content = ""

    for key, value in dict.items():
        i = f"{key} = '{value}', "
        content += i
    content = content[:-2] # срез последнего пробела и запятой

    update_query = f"UPDATE {table_name} SET {content} WHERE {id_name} = '{id}'"
    print(f'Проведено обновление строки: ({update_query})')
    with self.connection.cursor() as cursor:
        cursor.execute(request)
        self.connection.commit()


# ==========================================================================================
#                                       DELETE функции
# ==========================================================================================

def delete_row(self, id, table_name):
    """Удаление строки из таблицы. На входе: {}, ''. Выход без возврата."""
    for key, value in id:
        id_name = key
        id_value = value
    delete_by_id = f"DELETE FROM {table_name} WHERE {id_name} = '{id_value}'"
    with self.connection.cursor() as cursor:
        cursor.execute(delete_by_id)
        self.connection.commit()