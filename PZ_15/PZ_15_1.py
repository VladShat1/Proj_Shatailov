# Приложение ХИМЧИСТКА для некоторой организации.
# БД должна содержать таблицу Услуги со следующей структурой записи:
# ФИО мастера, ФИО клиента, тип чистки, стоимость, скидка.

import sqlite3 as sq

def insert():
    data = tuple(input('Введите через запятую фио мастера, фио клиента, тип чистки, цену, скидку\n').split(','))

    with sq.connect('dry_cleaning.db') as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO services VALUES(?,?,?,?,?)", [data])
        print(data)

def search1():
    with sq.connect('dry_cleaning.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM services WHERE cost>1000")
        result = cur.fetchall()
        print(result)

def search2():
    with sq.connect('dry_cleaning.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM services WHERE discount<0.20")
        result = cur.fetchall()
        print(result)

def search3():
    with sq.connect('dry_cleaning.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM services WHERE Clining_type='wet'")
        result = cur.fetchall()
        print(result)


def delete1():
    with sq.connect('dry_cleaning.db') as con:
        cur = con.cursor()
        cur.execute('DELETE FROM services WHERE cost>10000')
        pass

def delete2():
        with sq.connect('dry_cleaning.db') as con:
            cur = con.cursor()
            cur.execute('DELETE FROM services WHERE Discount=0.04')
            pass
def delete3():
        with sq.connect('dry_cleaning.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM services WHERE Master_fio='Speedy Willy Forachilly'")
            pass


def update1():
    with sq.connect('dry_cleaning.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE services SET Clining_type='dry' WHERE cost>50000")
        pass

def update2():
    with sq.connect('dry_cleaning.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE services SET cost=999.99 WHERE Master_fio='Speedy Willy Forachilly'")
        pass

def update3():
    with sq.connect('dry_cleaning.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE services SET discount=0.10 WHERE Clining_type='dry'")
        pass