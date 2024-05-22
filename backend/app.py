from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from models import *
import random
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)


def nextID(id):
    prefix = id[:3]
    alpha = id[3]
    num = id[4:]
    if num == "9999":
        return f"{prefix}{chr(ord(alpha)+1)}0001"
    else:
        return f"{prefix}{alpha}{'0'*(4-len(str(int(num))))}{int(num)+1}"


# Data Retrieval
@app.route("/get-content/books", methods=["GET"])
def getBooks():
    args = request.args.to_dict()
    if "start" in args:
        del args["start"]
    start = request.args.get('start', 0, type=int)

    if args != {}:
        fetcher = Books.query.filter_by(**args).all()
    else:
        fetcher = Books.query.order_by(
            Books.date_added.desc()).offset(start).limit(500).all()

    if fetcher:
        books_list = []
        for book in fetcher:
            books_list.append({
                "book_id": book.book_id,
                "book_name": book.book_name,
                "img": book.img,
                "author_id": book.author_id,
                "section_id": book.section_id,
                "genre": book.genre,
                "date_added": book.date_added,
            })
        return books_list, 200
    else:
        abort(404)


@app.route("/get-content/authors", methods=["GET"])
def getAuthors():
    args = request.args.to_dict()
    if "start" in args:
        del args["start"]
    start = request.args.get('start', 0, type=int)

    if args != {}:
        fetcher = Authors.query.filter_by(**args).all()
    else:
        fetcher = Authors.query.offset(start).limit(500).all()

    if fetcher:
        authors_list = []
        for author in fetcher:
            authors_list.append({
                "author_id": author.author_id,
                "author_name": author.author_name,
                "img": author.img,
                "dob": author.dob,
                "dod": author.dod,
                "country": author.country,
                "avg_rating": author.avg_rating,
            })
        return authors_list, 200
    else:
        abort(404)


@app.route("/get-content/users", methods=["GET"])
def getUsers():
    args = request.args.to_dict()
    if "start" in args:
        del args["start"]
    start = request.args.get('start', 0, type=int)

    if args != {}:
        fetcher = Users.query.filter_by(**args).all()
    else:
        fetcher = Users.query.offset(start).limit(500).all()

    if fetcher:
        users_list = []
        for user in fetcher:
            users_list.append({
                "user_id": user.user_id,
                "user_name": user.user_name,
                "password": user.password,
                "email": user.email,
                "ph_no": user.ph_no,
                "last_loged": user.last_loged,
                "gender": user.gender,
                "doj": user.doj,
                "dob": user.dob,
            })
        return users_list, 200
    else:
        abort(404)


@app.route("/get-content/sections", methods=["GET"])
def getSections():
    args = request.args.to_dict()
    if "start" in args:
        del args["start"]
    start = request.args.get('start', 0, type=int)

    if args != {}:
        fetcher = Sections.query.filter_by(**args).all()
    else:
        fetcher = Sections.query.offset(start).limit(500).all()

    if fetcher:
        sections_list = []
        for section in fetcher:
            sections_list.append({
                "section_id": section.section_id,
                "section_name": section.section_name,
                "date_added": section.date_added,
            })
        return sections_list, 200
    else:
        abort(404)


@app.route("/get-content/ratings", methods=["GET"])
def getRatings():
    args = request.args.to_dict()
    if "start" in args:
        del args["start"]
    start = request.args.get('start', 0, type=int)

    if args != {}:
        fetcher = Ratings.query.filter_by(**args).all()
    else:
        fetcher = Ratings.query.offset(start).limit(500).all()

    if fetcher:
        ratings_list = []
        for rating in fetcher:
            ratings_list.append({
                "sno": rating.sno,
                "book_id": rating.book_id,
                "user_id": rating.user_id,
                "rating": rating.rating,
                "feedback": rating.feedback,
            })
        return ratings_list, 200
    else:
        abort(404)


@app.route("/get-content/issues", methods=["GET"])
def getIssues():
    args = request.args.to_dict()
    if "start" in args:
        del args["start"]
    start = request.args.get('start', 0, type=int)

    if args != {}:
        fetcher = Issues.query.filter_by(**args).all()
    else:
        fetcher = Issues.query.offset(start).limit(500).all()

    if fetcher:
        issues_list = []
        for issue in fetcher:
            issues_list.append({
                "sno": issue.sno,
                "book_id": issue.book_id,
                "user_id": issue.user_id,
                "request_date": issue.request_date,
                "doi": issue.doi,
                "dor": issue.dor,
            })
        return issues_list, 200
    else:
        abort(404)


@app.route("/get-content/requests", methods=["GET"])
def getRequests():
    args = request.args.to_dict()
    if "start" in args:
        del args["start"]
    start = request.args.get('start', 0, type=int)

    if args != {}:
        fetcher = Requests.query.filter_by(**args).all()
    else:
        fetcher = Requests.query.offset(start).limit(500).all()

    if fetcher:
        request_list = []
        for requester in fetcher:
            request_list.append({
                "sno": requester.sno,
                "book_id": requester.book_id,
                "user_id": requester.user_id,
                "request_date":requester.request_date,
            })
        return request_list, 200
    else:
        abort(404)


@app.route("/get-content/recent-book", methods=["GET"])
def getRecentBook():
    book_id = request.args.to_dict()["book_id"]
    fetchBook = Books.query.filter_by(book_id=book_id).first()
    fetchAuthor = Authors.query.filter_by(
        author_id=fetchBook.author_id).first()
    fetchSection = Sections.query.filter_by(
        section_id=fetchBook.section_id).first()
    fetchRating = Ratings.query.filter_by(book_id=book_id).all()
    fetchIssue = Issues.query.filter_by(book_id=book_id).all()
    ratings = []
    sum_rate = 0
    book_avg_rating = 0
    if fetchRating != []:
        for rating in fetchRating:
            sum_rate += float(rating.rating)
            roger = f"http://127.0.0.1:5000/get-content/users?user_id={rating.user_id}"
            fetcher = requests.get(roger).json()[0]
            ratingReturn = {
                "sno": rating.sno,
                "user_id": rating.user_id,
                "rating": rating.rating,
                "feedback": rating.feedback,
            }
            ratingReturn.update(fetcher)
            ratings.append(ratingReturn)

        book_avg_rating = sum_rate/len(fetchRating)
    else:
        book_avg_rating = random.randrange(1, 5)

        ratings = [
            {
                "user_name": "Mateo Novak",
                "gender": "Male",
                "book_avg_rating": 3.5
            },
            {
                "user_name": "Ava Marino",
                "gender": "Female",
                "book_avg_rating": 4.5
            }
        ]
    total_issues = len(fetchIssue)

    universalContent = {
        "book_id": book_id,
        "book_name": fetchBook.book_name,
        "img": fetchBook.img,
        "genre": fetchBook.genre,
        "book_date_added": fetchBook.date_added,
        "author_name": fetchAuthor.author_name,
        "author_img": fetchAuthor.img,
        "dob": fetchAuthor.dob,
        "dod": fetchAuthor.dod,
        "country": fetchAuthor.country,
        "author_avg_rating": fetchAuthor.avg_rating,
        "section_name": fetchSection.section_name,
        "ratings": ratings,
        "book_avg_rating": book_avg_rating,
        "total_issues": total_issues,
    }
    return universalContent, 200


# Data Insertion
@app.route("/push-content/books", methods=["GET", "POST"])
def pushBooks():
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/books?book_name={form['book_name']}"
    fetcher = requests.get(roger)
    if request.method == "POST":
        if fetcher.status_code == 404:
            last_id = Books.query.order_by(
                Books.book_id.desc()).first().book_id
            next_id = nextID(last_id)
            new_book = Books(
                book_id=next_id,
                book_name=form["book_name"],
                img=form["img"],
                author_id=form["author_id"],
                section_id=form["section_id"],
                genre=form["genre"],
                date_added=datetime.strptime(form["date_added"], "%Y-%m-%d")
            )
            db.session.add(new_book)
            db.session.commit()
            return f"New Book added with ID: {next_id}", 200
        else:
            return {"message": "Book already exists."}, 406


@app.route("/push-content/authors", methods=["GET", "POST"])
def pushAuthors():
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/authors?author_name={form['author_name']}"
    fetcher = requests.get(roger)
    if request.method == "POST":
        if fetcher.status_code == 404:
            last_id = Authors.query.order_by(
                Authors.author_id.desc()).first().author_id
            next_id = nextID(last_id)
            new_author = Authors(
                author_id=next_id,
                author_name=form["author_name"],
                img=form["img"],
                dob=datetime.strptime(form["dob"], "%Y-%m-%d"),
                dod=datetime.strptime(form["dod"], "%Y-%m-%d"),
                country=form["country"],
                avg_rating=form["avg_rating"]
            )
            db.session.add(new_author)
            db.session.commit()
            return f"New Author added with ID: {next_id}", 200
        else:
            return {"message": "Author already exists."}, 406


@app.route("/push-content/users", methods=["GET", "POST"])
def pushUsers():
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/users?email={form['email']}"
    fetcher = requests.get(roger)
    if request.method == "POST":
        if fetcher.status_code == 404:
            last_id = Users.query.order_by(
                Users.user_id.desc()).first().user_id
            next_id = nextID(last_id)
            new_user = Users(
                user_id=next_id,
                user_name=form["user_name"],
                password=form["password"],
                email=form["email"],
                ph_no=form["ph_no"],
                last_loged=datetime.strptime(form["last_loged"], "%Y-%m-%d"),
                gender=form["gender"],
                doj=datetime.strptime(form["doj"], "%Y-%m-%d"),
                dob=datetime.strptime(form["dob"], "%Y-%m-%d")
            )
            db.session.add(new_user)
            db.session.commit()
            return f"New User added with ID: {next_id}", 200
        else:
            return {"message": "User already exists."}, 406


@app.route("/push-content/sections", methods=["GET", "POST"])
def pushSections():
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/sections?section_name={form['section_name']}"
    fetcher = requests.get(roger)
    if request.method == "POST":
        if fetcher.status_code == 404:
            last_id = Sections.query.order_by(
                Sections.section_id.desc()).first().section_id
            next_id = nextID(last_id)
            new_section = Sections(
                section_id=next_id,
                section_name=form["section_name"],
                date_added=datetime.strptime(form["date_added"], "%Y-%m-%d")
            )
            db.session.add(new_section)
            db.session.commit()
            return f"New Section added with ID: {next_id}", 200
        else:
            return {"message": "Section already exists."}, 406


@app.route("/push-content/ratings", methods=["GET", "POST"])
def pushRatings():
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/ratings?book_id={form['book_id']}&user_id={form['user_id']}"
    fetcher = requests.get(roger)
    if request.method == "POST":
        if fetcher.status_code == 404:
            last_id = Ratings.query.order_by(Ratings.sno.desc()).first().sno
            next_id = last_id+1
            new_rating = Ratings(
                sno=next_id,
                book_id=form["book_id"],
                user_id=form["user_id"],
                rating=form["rating"],
                feedback=form["feedback"]
            )
            db.session.add(new_rating)
            db.session.commit()
            return f"New Rating added with Sno: {next_id}", 200
        else:
            return {"message": "You have already rated this book, you can't do it again."}, 406


@app.route("/push-content/issues", methods=["GET", "POST"])
def pushIssues():
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/issues?book_id={form['book_id']}&user_id={form['user_id']}"
    fetcher = requests.get(roger)
    if request.method == "POST":
        if fetcher.status_code == 404:
            last_id = Issues.query.order_by(Issues.sno.desc()).first().sno
            next_id = last_id+1
            new_issue = Issues(
                sno=next_id,
                book_id=form["book_id"],
                user_id=form["user_id"],
                request_date=datetime.strptime(
                    form["request_date"], "%Y-%m-%d"),
                doi=datetime.strptime(form["doi"], "%Y-%m-%d"),
                dor=datetime.strptime(form["dor"], "%Y-%m-%d")
            )
            db.session.add(new_issue)
            db.session.commit()
            return f"New Issue added with Sno: {next_id}", 200
        else:
            return {"message": "You have already rated this book, you can't do it again."}, 406


@app.route("/push-content/requests", methods=["GET", "POST"])
def pushRequests():
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/requests?book_id={form['book_id']}&user_id={form['user_id']}"
    fetcher = requests.get(roger)
    if request.method == "POST":
        if fetcher.status_code == 404:
            new_issue = Requests(
                book_id=form["book_id"],
                user_id=form["user_id"],
                request_date=datetime.strptime(
                    form["request_date"], "%Y-%m-%d"),
            )
            db.session.add(new_issue)
            db.session.commit()
            return f"New Requests added Book ID: {form['book_id']} & User ID: {form['user_id']}", 200
        else:
            return {"message": "You have already requested this book, you can't do it again."}, 406


# Data Updation
@app.route("/put-content/books", methods=["GET", "PUT"])
def putBooks():
    form = request.get_json()
    fetcher = Books.query.filter_by(book_id=form["book_id"]).first()
    if request.method == "PUT":
        if fetcher:
            for i in form:
                try:
                    setattr(fetcher, i, datetime.strptime(form[i], "%Y-%m-%d"))
                except:
                    setattr(fetcher, i, form[i])
            db.session.commit()
            roger = f"http://127.0.0.1:5000/get-content/books?book_id={form['book_id']}"
            fetcher = requests.get(roger).json()
            return fetcher, 200
        else:
            return {"message": "Book do not exists."}, 406


@app.route("/put-content/authors", methods=["GET", "PUT"])
def putAuthors():
    form = request.get_json()
    fetcher = Authors.query.filter_by(author_id=form["author_id"]).first()
    if request.method == "PUT":
        if fetcher:
            for i in form:
                try:
                    setattr(fetcher, i, datetime.strptime(form[i], "%Y-%m-%d"))
                except:
                    setattr(fetcher, i, form[i])
            db.session.commit()
            roger = f"http://127.0.0.1:5000/get-content/authors?author_id={form['author_id']}"
            fetcher = requests.get(roger).json()
            return fetcher, 200
        else:
            return {"message": "Author do not exists."}, 406


@app.route("/put-content/users", methods=["GET", "PUT"])
def putUsers():
    form = request.get_json()
    fetcher = Users.query.filter_by(user_id=form["user_id"]).first()
    if request.method == "PUT":
        if fetcher:
            for i in form:
                try:
                    setattr(fetcher, i, datetime.strptime(form[i], "%Y-%m-%d"))
                except:
                    setattr(fetcher, i, form[i])
            db.session.commit()
            roger = f"http://127.0.0.1:5000/get-content/users?user_id={form['user_id']}"
            fetcher = requests.get(roger).json()
            return fetcher, 200
        else:
            return {"message": "User do not exists."}, 406


@app.route("/put-content/sections", methods=["GET", "PUT"])
def putSections():
    form = request.get_json()
    fetcher = Sections.query.filter_by(section_id=form["section_id"]).first()
    if request.method == "PUT":
        if fetcher:
            for i in form:
                try:
                    setattr(fetcher, i, datetime.strptime(form[i], "%Y-%m-%d"))
                except:
                    setattr(fetcher, i, form[i])
            db.session.commit()
            roger = f"http://127.0.0.1:5000/get-content/sections?section_id={form['section_id']}"
            fetcher = requests.get(roger).json()
            return fetcher, 200
        else:
            return {"message": "Section do not exists."}, 406


@app.route("/put-content/ratings", methods=["GET", "PUT"])
def putRatings():
    form = request.get_json()
    fetcher = Ratings.query.filter_by(
        book_id=form["book_id"], user_id=form["user_id"]).first()
    if request.method == "PUT":
        if fetcher:
            for i in form:
                try:
                    setattr(fetcher, i, datetime.strptime(form[i], "%Y-%m-%d"))
                except:
                    setattr(fetcher, i, form[i])
            db.session.commit()
            roger = f"http://127.0.0.1:5000/get-content/ratings?book_id={form['book_id']}&user_id={form['user_id']}"
            fetcher = requests.get(roger).json()
            return fetcher, 200
        else:
            return {"message": "Rating do not exists."}, 406


@app.route("/put-content/issues", methods=["GET", "PUT"])
def putIssues():
    form = request.get_json()
    fetcher = Issues.query.filter_by(
        book_id=form["book_id"], user_id=form["user_id"]).first()
    if request.method == "PUT":
        if fetcher:
            for i in form:
                try:
                    setattr(fetcher, i, datetime.strptime(form[i], "%Y-%m-%d"))
                except:
                    setattr(fetcher, i, form[i])
            db.session.commit()
            roger = f"http://127.0.0.1:5000/get-content/issues?book_id={form['book_id']}&user_id={form['user_id']}"
            fetcher = requests.get(roger).json()
            return fetcher, 200
        else:
            return {"message": "Issues do not exists."}, 406


# Data Deletion
@app.route("/delete-content/books", methods=["GET", "DELETE"])
def deleteBooks():
    args = request.args.to_dict()
    fetcher = Books.query.filter_by(book_id=args["book_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"Book with ID {args['book_id']} deleted"}, 200
    else:
        return {"message": "Book do not exist"}, 406


@app.route("/delete-content/authors", methods=["GET", "DELETE"])
def deleteAuthors():
    args = request.args.to_dict()
    fetcher = Authors.query.filter_by(author_id=args["author_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"Author with ID {args['author_id']} deleted"}, 200
    else:
        return {"message": "Author do not exist"}, 406


@app.route("/delete-content/users", methods=["GET", "DELETE"])
def deleteUsers():
    args = request.args.to_dict()
    fetcher = Users.query.filter_by(user_id=args["user_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"User with ID {args['user_id']} deleted"}, 200
    else:
        return {"message": "User do not exist"}, 406


@app.route("/delete-content/sections", methods=["GET", "DELETE"])
def deleteSections():
    args = request.args.to_dict()
    fetcher = Sections.query.filter_by(section_id=args["section_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"Section with ID {args['section_id']} deleted"}, 200
    else:
        return {"message": "Section do not exist"}, 406


@app.route("/delete-content/ratings", methods=["GET", "DELETE"])
def deleteRatings():
    args = request.args.to_dict()
    fetcher = Ratings.query.filter_by(
        book_id=args["book_id"], user_id=args["user_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"Rating with book id {args['book_id']} & user id {args['book_id']} deleted"}, 200
    else:
        return {"message": "Rating do not exist"}, 406


@app.route("/delete-content/issues", methods=["GET", "DELETE"])
def deleteIssues():
    args = request.args.to_dict()
    fetcher = Issues.query.filter_by(
        book_id=args["book_id"], user_id=args["user_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"Issue with book id {args['book_id']} & user id {args['book_id']} deleted"}, 200
    else:
        return {"message": "Issue do not exist"}, 406


# Table Truncation
@app.route('/delete-content/table', methods=["GET", "DELETE"])
def delete_content():
    table = request.args.to_dict()["table"]
    num_rows_deleted = db.session.query(globals()[table]).delete()
    db.session.commit()
    return f"Deleted {num_rows_deleted} rows from the {table} table."


# with app.app_context():
#     Requests.__table__.create(db.engine)

if __name__ == "__main__":
    app.run(debug=True)
