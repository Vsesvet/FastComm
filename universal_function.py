# Универсальные функции
# 1. Считать все строки из таблицы: select_all_row(table) +
# 2. Добавить новую строку в таблицу: insert_row_to_table(table, dict) +
# 3. Найти и вернуть строку: find_string(table_name, column, content) +
# 4. Найти и вернуть строку с ID! : get_id(table, column, content) +
# 5. Заменить строку: update_row(table_name, content) +-
# 6. Удалить строку: delete_row_from_table(table_name, id) (сначала пункт 4) +

# Table: Users, Participans, Participants_data, Participants_data_for certain event


# INSERT INTO users (name, age) VALUES ('Сергей', '25');

# INSERT INTO {table_name}{column} VALUES{content};
# SELECT {value1} FROM {table_name} WHERE {column} = {content}
# UPDATE {table_name} SET {
# UPDATE users SET age = '18' WHERE id = '3';
# UPDATE users SET age = '18', country = 'Россия' WHERE id = '3';
# DELETE FROM users WHERE id = '10';



def insert_row_to_table(dictionary, table_name):
    """Универсальная функция добавления row (словаря) в таблицу"""
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


slovar = {'phone_number': '89777194310', 'second_name': 'Ефремов', 'first_name': 'Максим', 'last_name': 'Георгиевич'}
table_name = 'users'
insert_row_to_table(slovar, table_name)


# ====================================================================



def get_value_by_args(value1, args, table_name):
    """(value1 - строка, args - словарь). Универсальная функция получения одного значения из row"""
    for key, value in args.items():
        column = key
        content = value
    request = f"SELECT {value1} FROM {table_name} WHERE {column} = {content}"
    with self.connection.cursor() as cursor:
        cursor.execute(request)
        responce = cursor.fetchall()
        self.connection.commit()
    for item in responce:
        value2 = item.get(value1)
    return value2


#рассматриваем получение role из role_id по пользователю
arg1 = 'role_name'
table_name = 'roles'
args = {'role_id': '1'}

get_value_by_args(arg1, args, table_name)
print(get_value_by_args.__doc__)