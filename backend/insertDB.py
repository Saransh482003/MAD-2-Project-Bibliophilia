from models import *
import sqlite3
import pandas as pd

books = pd.read_excel("books.xlsx", sheet_name="1 Books")
print(books)
conn = sqlite3.connect("instance/library.sqlite3")
cursor = conn.cursor()
# print(len(books),books[0])
for i in range(len(books)):
    row = books.iloc[i]
    # print(row['Author_ID'])
    cursor.execute(f"""
        INSERT INTO Books (book_id, book_name, img, author_id, author_name, section_id, genre, date_added) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (row['Book_ID'], row['Title'], row['Img'], row['Author_ID'], row['Author_Name'], row['Section_ID'], row['Genre'], f"{row['Date_Added']}"))
conn.commit()
conn.close()
