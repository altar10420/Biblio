import sqlite3


class Database:

    # constructor of a class
    # "self" is just a convention, in reality it could be any parameter name
    # it is needed because python sends object instance argument to __init__ method and some parameter has to take it
    # if we didn't have "self", we would get "TypeError: takes 0 positional arguments but 1 was given"
    # when creating object, python sends object to the self parameter, and then other arguments to remaining parameters
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title LIKE ('%' || ? || '%') AND author LIKE ('%' || ? || '%')"
                         " AND year LIKE ('%' || ? || '%') AND isbn LIKE ('%' || ? || '%')", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title="", author="", year="", isbn=""):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    # could be used and for example triggered by some button, instead adding a commit to all the methods
    # def commit(self):
    #     self.conn.commit()

    # destructor - method for destructing object - for example to close connection to database
    def __del__(self):
        self.conn.close()



#insert("Old man and sea", "Ernest Hemingway", 1929, 132315678997654)

#print(view())

#print(search(year=1929))
