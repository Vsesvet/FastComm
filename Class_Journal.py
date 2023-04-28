"""//////////////////////////////////////////////"""
""""////////------IMPORT LIBRARIES-------////////"""
"""//////////////////////////////////////////////"""
import os
from datetime import datetime


class Journal:
    """Логирование работы программы в файл журнала"""
    def time_now(self):
        dt_now = str(datetime.now())
        dt_now.split('.')
        dt_now = dt_now[:-7]
        return dt_now

    def log(self, info):
        """Логирование событий"""
        # Получаем текущее время из datetime
        dt_now = self.time_now()

        self.info = info
        self.path_dir_journal = r'/home/efremov/Event'
        self.path_journal_log = r'/home/efremov/Event/journal.log'

        # Стандартная запись лога события
        if os.path.isfile(self.path_journal_log):
            with open(self.path_journal_log, 'a') as file:
                file.write(f"{dt_now} {info} \n")
        elif not os.path.isdir(self.path_dir_journal):
            self.create_path_dir_journal()

        # Проверка существования journal.log
        elif not os.path.isfile(self.path_journal_log):
            self.create_file_journal(self.info)

    def create_path_dir_journal(self):
        """Создание директорий для хранения journal.log"""
        os.makedirs(self.path_dir_journal)
        print(f'Journal.log() Создание структуры папок для размещения файла журнала: {self.path_dir_journal}')
        self.create_file_journal(self.info)

    def create_file_journal(self, info):
        """Создание файла journal.log"""
        # Получаем текущее время из datetime
        dt_now = self.time_now()

        print(f'Файл journal.log по пути {self.path_journal_log} не найден, поэтому был создан')
        with open(self.path_journal_log, 'w') as file:
            file.write(f"{dt_now} {info} \n")
            info_dir = (f'Journal.log() Создание структуры папок для размещения файла журнала: {self.path_dir_journal}')
            info_file = (f'Journal.log() Создан файл журнала: {self.path_journal_log}')
            file.write(f"{dt_now} {info_dir} \n")
            file.write(f"{dt_now} {info_file} \n")

    def start_log(self):
        """Запись в лог строки о старте программы"""
        self.log(f'---------------RUN LOGIN WINDOW---------------')

    def close_login(self):
        # dt_now = self.time_now()
        """Завершение программы по нажатию на кнопку 'крестик' из окна Логина """
        self.log(f' Пользователь закрыл окно программы')
        self.log(f'----------Program finished----------')

    def finish_log(self, username_login):
        """Последние строки лога перед завершением программы"""
        self.log(f'Выход пользователя {username_login} из системы')
        self.log(f'----------Program finished----------')
