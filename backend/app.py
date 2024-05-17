from flask import Flask, jsonify, request
from flask_cors import CORS
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)

def nextID(id):
    prefix = id[:3]
    alpha = id[3]
    num = id[4:]
    if num=="9999":
        return f"{prefix}{chr(ord(alpha)+1)}0001"
    else:
       return f"{prefix}{alpha}{int(num)+1}" 

## Data Insertion
@app.route("/add-content/books", methods=["GET","POST"])
def addBooks():
    if request.method == "POST":
        form = request.form
        last_id = Books.query.order_by(Books.book_id.desc()).first()
        return last_id

## Table Truncation
@app.route('/delete_content',methods=["GET"])
def delete_content():
    num_rows_deleted = db.session.query(Issues).delete()
    db.session.commit()
    return f"Deleted {num_rows_deleted} rows from the books table."
    

if __name__ == "__main__":
    app.run(debug=True)
