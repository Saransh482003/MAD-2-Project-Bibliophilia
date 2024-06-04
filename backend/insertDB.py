from models import *
import sqlite3
import pandas as pd

books = pd.read_excel("books.xlsx", sheet_name="2 Authors")
print(books)
conn = sqlite3.connect("instance/library.sqlite3")
cursor = conn.cursor()
# print(len(books),books[0])
for i in range(len(books)):
    row = books.iloc[i]
    # print(row['Author_ID'])
    cursor.execute(f"""
        INSERT INTO Authors (author_id, author_name, img, dob, dod, country, avg_rating) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (row['Author_ID'], row['Name'], row['Img'], f"{row['DOB']}", f"{row['DOD']}", row['Country'], row['Avg. Rating']))
conn.commit()
conn.close()
