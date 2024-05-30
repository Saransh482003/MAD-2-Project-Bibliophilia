from flask import Flask, jsonify, request, abort
from sqlalchemy.sql.expression import func
from flask_cors import CORS
from models import *
import random
import requests
import math
from datetime import date, datetime
from dateutil import parser

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
        fetcher = Books.query.filter_by(**args).limit(500).all()
    else:
        fetcher = Books.query.offset(start).limit(200).all()

    if fetcher:
        books_list = []
        for book in fetcher:
            books_list.append({
                "book_id": book.book_id,
                "book_name": book.book_name,
                "img": book.img,
                "author_id": book.author_id,
                "author_name": book.author_name,
                "section_id": book.section_id,
                "genre": book.genre,
                "date_added": book.date_added,
            })
        return books_list, 200
    else:
        abort(404)


@app.route("/get-content/latestBooks", methods=["GET"])
def getLatestBooks():
    fetcher = Books.query.order_by(
        Books.date_added.desc()).limit(500).all()

    if fetcher:
        books_list = []
        for book in fetcher:
            books_list.append({
                "book_id": book.book_id,
                "book_name": book.book_name,
                "img": book.img,
                "author_id": book.author_id,
                "author_name": book.author_name,
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
        fetcher = Authors.query.offset(start).limit(100).all()

    if fetcher:
        authors_list = []
        for author in fetcher:
            authors_list.append({
                "author_id": author.author_id,
                "author_name": author.author_name,
                "img": author.img,
                "dob": author.dob.strftime("%Y-%m-%d"),
                "dod": author.dod.strftime("%Y-%m-%d"),
                "country": author.country,
                "avg_rating": round(author.avg_rating, 1),
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
        fetcher = Users.query.offset(start).limit(200).all()

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
                "img": section.img,
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
                "request_date": requester.request_date,
            })
        return request_list, 200
    else:
        abort(404)


@app.route("/get-content/genres", methods=["GET"])
def getGenres():
    args = request.args.to_dict()
    if "start" in args:
        del args["start"]
    start = request.args.get('start', 0, type=int)

    if args != {}:
        fetcher = Books.query.filter_by(**args).all()
    else:
        fetcher = Books.query.offset(start).limit(1000).all()

    if fetcher:
        genre_list = []
        for genre in fetcher:
            genre_list.append(genre.genre)
        return sorted(list(set(genre_list))), 200
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


@app.route("/search-content", methods=["GET"])
def searchBooks():
    keyword = request.args.to_dict()['keyword']
    fetcher = Books.query.filter(
        Books.book_name.like(f"%{keyword}%")).limit(500).all()
    if fetcher:
        books_list = []
        for book in fetcher:
            books_list.append({
                "book_id": book.book_id,
                "book_name": book.book_name,
                "img": book.img,
                "author_id": book.author_id,
                "author_name": book.author_name,
                "section_id": book.section_id,
                "genre": book.genre,
                "date_added": book.date_added.strftime('%d %b %Y'),
            })
        return books_list, 200
    else:
        abort(404)


@app.route("/search-content/my-books", methods=["GET"])
def searchMyBooks():
    keyword = request.args.to_dict()['keyword']
    user_id = request.args.to_dict()['user_id']
    fetcher = db.session.query(Issues, Books).join(Books, Books.book_id == Issues.book_id).filter(
        Issues.user_id == user_id, Books.book_name.like(f"%{keyword}%")).all()
    if fetcher:
        books_list = []
        for book in fetcher:
            books_list.append({
                "book_id": book[1].book_id,
                "book_name": book[1].book_name,
                "img": book[1].img,
                "author_id": book[1].author_id,
                "author_name": book[1].author_name,
                "section_id": book[1].section_id,
                "genre": book[1].genre,
                "date_added": book[1].date_added.strftime('%d %b %Y'),
                "request_date": book[0].request_date.strftime('%d %b %Y'),
                "doi": book[0].doi.strftime('%d %b %Y'),
                "dor": book[0].dor.strftime('%d %b %Y'),
            })
        return books_list, 200
    else:
        abort(404)


@app.route("/get-content/myBooks", methods=["GET"])
def myBooks():
    args = request.args.to_dict()
    user_id = args['user_id']

    roger = f"http://127.0.0.1:5000/get-content/issues?user_id={user_id}"
    fetcher = requests.get(roger).json()[::-1]

    today_date = datetime.now()
    books_list = {"Current": [], "History": []}
    for issue in fetcher:
        bookDetails = f"http://127.0.0.1:5000/get-content/books?book_id={issue['book_id']}"
        fetcherBooks = requests.get(bookDetails).json()[0]
        request_date = parser.parse(issue["request_date"])
        doi = parser.parse(issue["doi"][:-3])
        dor = parser.parse(issue["dor"][:-3])
        finalResponse = {
            "book_id": fetcherBooks["book_id"],
            "book_name": fetcherBooks["book_name"],
            "img": fetcherBooks["img"],
            "author_id": fetcherBooks["author_id"],
            "author_name": fetcherBooks["author_name"],
            "request_date": request_date.strftime("%d %b %Y"),
            "doi": doi.strftime("%d %b %Y"),
            "dor": dor.strftime("%d %b %Y"),
        }
        if today_date < dor:
            books_list["Current"].append(finalResponse)
        else:
            books_list["History"].append(finalResponse)
    return books_list, 200


@app.route("/get-content/randomBooks", methods=["GET"])
def randomBooks():
    fetcher = Books.query.order_by(func.random()).limit(10).all()

    if fetcher:
        books_list = []
        for book in fetcher:
            books_list.append({
                "book_id": book.book_id,
                "book_name": book.book_name,
                "img": book.img,
                "author_id": book.author_id,
                "author_name": book.author_name,
                "section_id": book.section_id,
                "genre": book.genre,
                "date_added": book.date_added,
            })
        return books_list, 200
    else:
        abort(404)


@app.route("/get-statistics", methods=["GET"])
def getUserStatistics():
    try:
        user_id = request.args.to_dict()["user_id"]

        fetchRequests = Requests.query.order_by(
            Requests.request_date.desc()).filter_by(user_id=user_id).all()
        fetchIssues = Issues.query.order_by(
            Issues.request_date.desc()).filter_by(user_id=user_id).all()

        fetchData = [i for i in fetchRequests]
        fetchData.extend([i for i in fetchIssues])
        dates = [[i.request_date.strftime(
            '%b'), i.request_date.year] for i in fetchData]
        year = sorted(list(set([i[1] for i in dates])))[::-1]
        barData = {}
        for i in year:
            months = [j[0] for j in dates if j[1] == i]
            monDict = {i: months.count(i) for i in months[::-1]}
            barData[i] = monDict

        finalBarData = []
        counter = 0
        for i in barData:
            for j in dict(reversed(list(barData[i].items()))):
                if counter < 10:
                    finalBarData.append([f"{j}'{i%100}", barData[i][j]])
                    counter += 1
                else:
                    break

        books = []
        for i in fetchData:
            book = Books.query.filter_by(book_id=i.book_id).first()
            books.append(book.genre)

        pieData = dict(sorted({i: books.count(i)
                               for i in books}.items(), key=lambda x: x[1], reverse=True))
        if len(pieData) > 5:
            pieData = dict(list(pieData.items())[:5])
        finalPieData = [[i, pieData[i]] for i in pieData]

        fetchUser = requests.get(
            f"http://127.0.0.1:5000/get-content/users?user_id={user_id}")
        fetchUser = fetchUser.json()[0]

        active_month = ""
        index = 0
        activity = 0
        for j, i in enumerate(finalBarData):
            if i[1] > activity:
                activity = i[1]
                index = j
        if len(finalBarData) > 0:
            active_month = finalBarData[index][0]
        ratings = Ratings.query.filter_by(user_id=user_id).all()
        now = f"{datetime.now()}"
        days_last_loged = (datetime.strptime(now, "%Y-%m-%d %H:%M:%S.%f") -
                           datetime.strptime(fetchUser["last_loged"], "%a, %d %b %Y %H:%M:%S %Z")).days
        cardData = {
            "total_issued": len(fetchIssues),
            "total_requests": len(fetchRequests),
            "most_active_month": active_month,
            "total_ratings": len(ratings),
            "days_last_loged": days_last_loged
        }

        fetchUser["last_loged"] = datetime.strptime(
            f"{fetchUser['last_loged']}", "%a, %d %b %Y %H:%M:%S %Z").strftime("%d %b %Y")
        fetchUser["doj"] = datetime.strptime(
            f"{fetchUser['doj']}", "%a, %d %b %Y %H:%M:%S %Z").strftime("%d %b %Y")
        fetchUser["dob"] = datetime.strptime(
            f"{fetchUser['dob']}", "%a, %d %b %Y %H:%M:%S %Z").strftime("%d %b %Y")

        fetchRating = requests.get(
            f"http://127.0.0.1:5000/get-content/ratings?user_id={user_id}")
        avg_rate = 0.0
        if fetchRating.status_code==200:
            fetchRating = fetchRating.json()
            avg_rate = round(sum([float(i['rating']) for i in fetchRating])/len(fetchRating),1)
        else:
            fetchRating = fetchRating.json()
        score = 100*len(fetchIssues) + 250*len(fetchRating)
        # score = score*0
        rank = "Sage" if score >= 13750 else "Scholar" if score >= 5000 else "Literati" if score >= 1750 else "Reader" if score >= 500 else "No"
        next_criteria = {
            "No": [
                "Read 5 Books"
            ],
            "Reader": [
                "Read 10 Books",
                "Review 3 Books",
            ],
            "Literati": [
                "Read 25 Books",
                "Review 10 Books",
            ],
            "Scholar": [
                "Read 75 Books",
                "Review 25 Books",
            ],
            "Sage": [
                "Congratulations!! on reaching the pinnacle."
            ]
        }
        next_points = {
            "No": 500,
            "Reader": 1750,
            "Literati": 5000,
            "Scholar": 13750,
        }
        return {"barchart": finalBarData[::-1], "piechart": finalPieData, "user_info": fetchUser, "cardData": cardData, "score": score, "rank": rank, "next_criteria": next_criteria[rank], "next_points": next_points[rank], "numIssues": len(fetchIssues),"numRequests": len(fetchRequests), "avg_rating": avg_rate}, 200
    except:
        abort(404, description="No Statistics Available")


@app.route("/get-feedbacks", methods=["GET"])
def getUserFeedbacks():
    user_id = request.args.to_dict()["user_id"]
    fetchRating = requests.get(
        f"http://127.0.0.1:5000/get-content/ratings?user_id={user_id}")
    fetchRating = fetchRating.json()
    fetchIssues = requests.get(
        f"http://127.0.0.1:5000/get-content/issues?user_id={user_id}")
    fetchIssues = fetchIssues.json()
    ratings = set([i['book_id'] for i in fetchRating])
    issues = set([i['book_id'] for i in fetchIssues])
    notrated = list(issues.difference(ratings))
    rated = list(ratings)
    notRatedBooks = []
    for i in notrated:
        booker = requests.get(
            f"http://127.0.0.1:5000/get-content/books?book_id={i}")
        booker = booker.json()[0]
        notRatedBooks.append(booker)
    ratedBooks = []
    for i in rated:
        booker = requests.get(
            f"http://127.0.0.1:5000/get-content/books?book_id={i}")
        booker = booker.json()[0]
        feedback = requests.get(
            f"http://127.0.0.1:5000/get-content/ratings?book_id={i}&user_id={user_id}")
        feedback = feedback.json()[0]

        booker["rating"] = math.ceil(float(feedback["rating"]))
        booker["feedback"] = feedback["feedback"]
        ratedBooks.append(booker)
    return {"Not Rated": notRatedBooks, "Rated": ratedBooks}, 200


@app.route("/get-librarian/previewBook", methods=["GET"])
def getLibrarianBooks():
    book_id = request.args.to_dict()["book_id"]
    booker = requests.get(
        f"http://127.0.0.1:5000/get-content/books?book_id={book_id}")
    booker = booker.json()[0]
    issues = requests.get(
        f"http://127.0.0.1:5000/get-content/issues?book_id={book_id}")
    if issues.status_code == 200:
        issues = issues.json()
    else:
        issues = []
    requester = requests.get(
        f"http://127.0.0.1:5000/get-content/requests?book_id={book_id}")
    if requester.status_code == 200:
        requester = requester.json()
    else:
        requester = []
    rater = requests.get(
        f"http://127.0.0.1:5000/get-content/ratings?book_id={book_id}")
    if rater.status_code == 200:
        rater = [float(i['rating']) for i in rater.json()]
    else:
        rater = []
    return {"book": booker, "issues": len(issues), "requests": len(requester), "avg_rating": sum(rater)/len(rater) if len(rater) != 0 else 0}


@app.route("/get-librarian/previewSection", methods=["GET"])
def getLibrarianSections():
    section_id = request.args.to_dict()["section_id"]
    sectioner = requests.get(
        f"http://127.0.0.1:5000/get-content/sections?section_id={section_id}")
    sectioner = sectioner.json()[0]
    return sectioner, 200


@app.route("/get-librarian/previewAuthor", methods=["GET"])
def getLibrarianAuthor():
    author_id = request.args.to_dict()["author_id"]
    sectioner = requests.get(
        f"http://127.0.0.1:5000/get-content/authors?author_id={author_id}")
    sectioner = sectioner.json()[0]
    booker = requests.get(
        f"http://127.0.0.1:5000/get-content/books?author_id={author_id}")
    if booker.status_code == 200:
        booker = booker.json()
    else:
        booker = []
    return {"authorData": sectioner, "numBooks": len(booker)}, 200


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
                author_name=form["author_name"],
                section_id=form["section_id"],
                genre=form["genre"],
                date_added=datetime.strptime(form["date_added"], "%Y-%m-%d")
            )
            db.session.add(new_book)
            db.session.commit()
            return f"New Book added with ID: {next_id}", 200
        else:
            return {"message": "Book already exists."}, 406


@app.route("/push-content/newBook", methods=["GET", "POST"])
def pushNewBooks():
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/books?book_name={form['book_name']}"
    fetcher = requests.get(roger)
    if request.method == "POST":
        if fetcher.status_code == 404:
            rogerAuthor = f"http://127.0.0.1:5000/get-content/authors?author_name={form['author_name']}"
            fetcherAuthor = requests.get(rogerAuthor)
            if fetcherAuthor.status_code == 404:
                abort(
                    406, description=f"Author with name: {form['author_name']} not found. Create new author.")
                # return jsonify(message=f"Author with name: {form['author_name']} not found. Create new author."), 406
            else:
                last_id = Books.query.order_by(
                    Books.book_id.desc()).first().book_id
                next_id = nextID(last_id)
                new_book = Books(
                    book_id=next_id,
                    book_name=form["book_name"],
                    img=form["img"],
                    author_id=fetcherAuthor.json()[0]["author_id"],
                    author_name=form["author_name"],
                    section_id=form["section_id"],
                    genre=form["genre"],
                    date_added=datetime.now(),
                )
                db.session.add(new_book)
                db.session.commit()
                return jsonify(message=f"New Book added with ID: {next_id}"), 200
        else:
            return jsonify(message="Book already exists."), 406


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
            return jsonify(message=f"New Section added with ID: {next_id}"), 200
        else:
            return jsonify(message=f"Section already exists: {next_id}"), 404


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
                img=form["img"],
                date_added=datetime.now()
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


@app.route("/push-content/requests", methods=["GET"])
def pushRequests():
    form = request.args.to_dict()
    # roger = f"http://127.0.0.1:5000/get-content/requests?book_id={form['book_id']}&user_id={form['user_id']}"
    # fetcher = requests.get(roger)
    # if fetcher.status_code == 404:
    new_issue = Requests(
        book_id=form["book_id"],
        user_id=form["user_id"],
        request_date=datetime.strptime(
            form["request_date"], "%Y-%m-%d"),
    )
    db.session.add(new_issue)
    db.session.commit()
    return f"New Requests added Book ID: {form['book_id']} & User ID: {form['user_id']}", 200
    # else:
    #     abort(406)


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


@app.errorhandler(406)
def not_acceptable(e):
    response = jsonify(error=str(e.description))
    response.status_code = 406
    return response

# with app.app_context():
#     Books.__table__.create(db.engine)


if __name__ == "__main__":
    app.run(debug=True)
