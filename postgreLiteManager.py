import psycopg2
from tkinter import messagebox


class PostgresManager:

    def __init__(self, database_name="", user="", password="", host="", port=1):

        self.connect = psycopg2.connect("dbname=%s"
                                        " user = %s password = %s"
                                        " host = %s port = %s " % (database_name, user, password, host, port))
        self.cur = self.connect.cursor()
        self.createTable()

    def createTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS BookStore (Title TEXT, author TEXT, year INTEGER, ISBN TEXT)")
        self.connect.commit()

    def addProducts(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO BookStore  VALUES(%s,%s,%s,%s)", (title, author, year, isbn))
        self.connect.commit()

    def searchFor(self, title="", author="", year=None, isbn=""):
        self.cur.execute("SELECT * FROM BookStore WHERE Title =%s OR  author = %s OR "
                         " year = %s OR  ISBN = %s", (title, author, year, isbn))
        return self.cur.fetchall()

    def deleteItem(self, title):
        self.cur.execute("DELETE FROM BookStore WHERE Title=%s", (title,))
        self.connect.commit()

    def update(self, title, author, year, isbn):
        self.cur.execute("UPDATE BookStore SET author =%s, year = %s, ISBN = %s, WHERE Title =%s",
                         (author, year, isbn, title))
        self.connect.commit()

    def view(self):
        self.cur.execute("SELECT * FROM BookStore")
        return self.cur.fetchall()

    def __del__(self):
        try:
            self.connect.close()
        except AttributeError:
            messagebox.showwarning("ERROR", "DATABASE WAS NOT FOUND!")


if __name__ == '__main__':
    postgreManager = PostgresManager()
    print(postgreManager.view())
