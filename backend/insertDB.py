from models import *
import sqlite3
import pandas as pd

books = pd.read_excel("books.xlsx", sheet_name="3 Users")
print(books)
conn = sqlite3.connect("instance/library.sqlite3")
cursor = conn.cursor()
# print(len(books),books[0])
for i in range(len(books)):
    row = books.iloc[i]
    # print(row['Book_ID'])
    cursor.execute(f"""
        INSERT INTO Users (user_id, user_name, password, email, ph_no, last_loged, gender, doj, dob) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (row['User_ID'], row['User_Name'], row['Password'], row['Email'], f"{row['Phone_No']}", f"{row['Last_Loged']}", row['Gender'], f"{row['DOJ']}", f"{row['DOB']}"))
conn.commit()
conn.close()
