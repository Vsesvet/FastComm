# Универсальные функции

# INSERT INTO users (name, age) VALUES ('Сергей', '25');


# SELECT {value1} FROM {table_name} WHERE {column} = {content}
# UPDATE {table_name} SET {
# UPDATE users SET age = '18' WHERE id = '3';

# DELETE FROM users WHERE id = '10';




def select_all_data(self, table_name):
    """Получение всех строк из базы данных. На входе: {}. На выходе [{}, {}, {}]"""
    select_all_rows = f"SELECT * FROM {table_name}"

    with self.connection.cursor() as cursor:
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()
        return rows



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

    # with self.connection.cursor() as cursor:
    #     cursor.execute(insert_query)
    #     self.connection.commit()


slovar = {'phone_number': '89777194310', 'second_name': 'Ефремов', 'first_name': 'Максим', 'last_name': 'Георгиевич'}
table_name = 'users'
insert_row_to_table(slovar, table_name)



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
        print(item)
        value2 = item.get(value1)
    return value2

def update_row_by_id(id, dict, table_name):
    id_name_request = f"SELECT KU.table_name as TABLENAME,column_name as PRIMARYKEYCOLUMN " \
              f"FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS TC " \
              f"INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS KU" \
              f"ON TC.CONSTRAINT_TYPE = 'PRIMARY KEY'" \
              f"AND TC.CONSTRAINT_NAME = KU.CONSTRAINT_NAME" \
              f"AND KU.table_name='{table_name}'"

    with self.connection.cursor() as cursor:
        cursor.execute(id_name_request)
        id_name = cursor.fetchone()
        self.connection.commit()

    print(id_name)
    content = ""

    for i in dict:
        i.replace("'", "",2)
        i.replace(':','=')
        content += i

    request = f"update {table_name} set {content} where {id_name} = '{id}'"

#рассматриваем получение role из role_id по пользователю
arg1 = 'role_name'
table_name = 'roles'
args = {'role_id': '1'}

#get_value_by_args(arg1, args, table_name)
#print(get_value_by_args.__doc__)