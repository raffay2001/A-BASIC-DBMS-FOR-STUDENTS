import sqlite3
import sys

def show_all():
    conn = sqlite3.connect('students.db')

    cursor = conn.cursor()

    cursor.execute("SELECT rowid, * FROM student_data")

    all_records = cursor.fetchall()

    if len(all_records) == 0:
        print(f"There's No Records in the Table")
    
    else:
        for record in all_records:
            print(list(record))

    
    conn.commit()
    
    conn.close()


def make_table():

    conn = sqlite3.connect('students.db')

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE student_data(
            
            Name text,
            Roll_No integer,
            Age integer,
            Phone integer)"""
        )
    
    conn.commit()
    
    conn.close()

    
def add_record():

    conn = sqlite3.connect('students.db')

    cursor = conn.cursor()

    name = input(f"Enter your Full Name: ")
    roll_no = input(f"Enter Roll Number: ")
    age = input(f"Enter your age: ")
    phone = input(f"Enter your Phone Number: ")

    cursor.execute("INSERT INTO student_data VALUES (?,?,?,?)",(name,roll_no,age,phone))

    conn.commit()
    
    conn.close()



def delete_record():
    conn = sqlite3.connect('students.db')

    cursor = conn.cursor()

    id = input(f"Enter the row_id of the record which you want to delete: ")

    cursor.execute("DELETE FROM student_data WHERE rowid = (?)",id)

    print(f"The record has been Deleted!!")

    conn.commit()
    
    conn.close()
    

def search_records():

    choice = int(input(f"On which field of the record do you want to perform the search?\n1-Name\n2-Roll Number\n3-Age\n4-Phone\nEnter the designated key to search: "))

    if choice == 1:
        conn = sqlite3.connect('students.db')

        cursor = conn.cursor()

        name = input(f"Enter the name by which you want to search: ")

        cursor.execute("SELECT rowid,* FROM student_data WHERE Name = (?)",(name,))

        all_records = cursor.fetchall()

        for record in all_records:
            print(list(record))

        conn.commit()
    
        conn.close()
        

    elif choice == 2:
        conn = sqlite3.connect('students.db')

        cursor = conn.cursor()

        roll = input(f"Enter the Roll Number by which you want to search: ")

        cursor.execute("SELECT rowid,* FROM student_data WHERE Roll_No = (?)",(roll,))

        all_records = cursor.fetchall()

        for record in all_records:
            print(list(record))

        conn.commit()
    
        conn.close()

    elif choice == 3:
        conn = sqlite3.connect('students.db')

        cursor = conn.cursor()

        age = input(f"Enter the Age by which you want to search: ")

        cursor.execute("SELECT rowid,* FROM student_data WHERE Age = (?)",(age,))

        all_records = cursor.fetchall()

        for record in all_records:
            print(list(record))

        conn.commit()
    
        conn.close()


    elif choice == 4:
        conn = sqlite3.connect('students.db')

        cursor = conn.cursor()

        phone = input(f"Enter the Phone Number by which you want to search: ")

        cursor.execute("SELECT rowid,* FROM student_data WHERE Phone = (?)",(phone,))

        all_records = cursor.fetchall()

        for record in all_records:
            print(list(record))

        conn.commit()
    
        conn.close()


def menu():

    print(f"WELCOME TO THE DATABASE MANAGEMENT SYSTEM FOR STUDENTS HERE'S THE MENU:\n1-SHOW ALL THE RECORDS\n2-ADD A RECORD\n3-DELETE A RECORD\n4-SEARCH A RECORD\n5-EXIT")


def run():
    while not None:
        menu()

        choice = int(input(f"ENTER YOUR CHOICE NUMBER: "))

        if choice == 1:
            show_all()

        elif choice == 2:
            add_record()

        elif choice == 3: 
            delete_record()

        elif choice == 4:
            search_records()

        elif choice == 5:
            sys.exit(0)

        else:
            print(f"Please Enter a Valid!!")
            pass

if __name__ == "__main__":
    run()