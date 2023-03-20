from tabulate import tabulate

import mysql.connector

con = mysql.connector.connect(
    host="localhost", user="root", password="", database="python_db", port=3309
)


def insert(name, age, city):
    res = con.cursor()
    sql = "insert into users (name,age,city) values (%s,%s,%s)"
    user = (name, age, city)
    res.execute(sql, user)
    con.commit()
    print("Data Inserted Successfully")


def update(name, age, city, id):
    res = con.cursor()
    sql = "update users set name=%s,age=%s,city=%s where id=%s"
    user = (name, age, city, id)
    res.execute(sql, user)
    con.commit()
    print()
    print("Data Updated Successfully")


def select():
    res = con.cursor()
    sql = "SELECT ID, NAME, AGE, CITY from users"
    res.execute(sql)
    # result=res.fetchone()
    # result=res.fetchmany(2)
    result = res.fetchall()
    print()
    print(tabulate(result, headers=["ID", "NAME", "AGE", "CITY"]))


def delete(id):
    res = con.cursor()
    sql = "delete from users where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print()
    print("Data Deleted Successfully")


while True:
    print()
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Select Data")
    print("4. Delete Data")
    print("5. Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        name = input("Enter Your Name : ")
        age = input("Enter Your Age : ")
        city = input("Enter Your City : ")
        insert(name, age, city)

    elif choice == 2:
        id = input("Enter The Id : ")
        name = input("Enter Your Name : ")
        age = input("Enter Your Age : ")
        city = input("Enter Your City : ")
        update(name, age, city, id)

    elif choice == 3:
        select()

    elif choice == 4:
        id = int(input("Enter The Id to Delete : "))
        delete(id)

    elif choice == 5:
        print()
        print("Program Exited Successfully")
        break

    else:
        print()
        print("Invalid Selection")