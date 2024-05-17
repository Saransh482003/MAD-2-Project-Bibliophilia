from models import *
import sqlite3
import pandas as pd

books = pd.read_excel("books.xlsx",sheet_name="6 Issue Logs")
print(books)
conn = sqlite3.connect("instance/library.sqlite3")
cursor = conn.cursor()
# print(len(books),books[0])
for i in range(len(books)):
    row = books.iloc[i]
    cursor.execute(f"""
        INSERT INTO Issues (sno, book_id, user_id, request_date, doi, dor) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, (i+1,row['Book_ID'], row['User_ID'], f"{row['Request_Date']}", f"{row['DOI']}", f"{row['DOR']}"))
conn.commit()
conn.close()