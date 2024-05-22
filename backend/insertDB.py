from models import *
import sqlite3
import pandas as pd

books = pd.read_excel("books.xlsx",sheet_name="7 Request Logs")
print(books)
conn = sqlite3.connect("instance/library.sqlite3")
cursor = conn.cursor()
# print(len(books),books[0])
for i in range(len(books)):
    row = books.iloc[i]
    cursor.execute(f"""
        INSERT INTO Requests (book_id, user_id, request_date) 
        VALUES (?, ?, ?)
    """, (row['Book_ID'], row['User_ID'], f"{row['Request_Date']}"))
conn.commit()
conn.close()