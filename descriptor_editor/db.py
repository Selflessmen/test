import sqlite3


class DataBase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exist(self, chat_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `manofactures` WHERE `id` = ?", (str(chat_id),)).fetchmany(1)
            return result

    def add_user(self, user_id, name):
        self.cursor.execute("INSERT INTO `manofactures` (`id`, `name`) VALUES(?, ?)", (str(user_id), name))
        self.connection.commit()
        return self.cursor.lastrowid

    def set_smile(self, smiile, id_chat):
        with self.connection:
            return self.cursor.execute("UPDATE `manofactures` SET `smile` = ? WHERE `id` = ?", (smiile, str(id_chat),))

    def get_smile(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT `smile` FROM `manofactures` WHERE `id` = ?", (str(id),)).fetchone()
            return result
