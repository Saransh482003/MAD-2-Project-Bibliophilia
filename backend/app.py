from flask import Flask, jsonify, request, abort
from functools import wraps
import jwt
from sqlalchemy.sql.expression import func, desc, case
from flask_cors import CORS
from models import *
import random
import requests
import math
import calendar
from datetime import date, datetime, timedelta
from dateutil import parser

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "3T9rFtQxZ1jA77sKJiy_mT6YvFP_W0C6eM67oNOxO0Y"

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


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user_id = data['sub']
        except Exception as e:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(*args, **kwargs)
    
    return decorated


def librarian_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_role = data['sub']
        except Exception as e:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(*args, **kwargs)
    
    return decorated

@app.route("/librarian-signin", methods=["GET","POST"])
def librarianSignin():
    form = request.get_json()
    if form["user_name"] == "Nairarbil069" and form["password"] == "SHEL@20$tt#":
        token = jwt.encode({
        'sub': "librarian",
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(hours=2)},
        app.config['SECRET_KEY'])
        return {"message": f"Welcome Librarian", "code": 801, "token": token}, 200
    else:
        return {"message": f"Incorrect credentials. Please try again.", "code": 802}, 200

# Signin Signup
@app.route("/signin", methods=["GET", "POST"])
def signin():
    form = request.get_json()
    fetchUser = Users.query.filter_by(
        user_name=form["user_name"], password=form["password"]).first()
    
    if fetchUser:
        fetchBan = Blacklists.query.filter_by(
            user_id=fetchUser.user_id).first()
        
        token = jwt.encode({
        'sub': fetchUser.user_id,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(hours=6)},
        app.config['SECRET_KEY'])
        if fetchBan:
            if fetchBan.ban_type == "Perma":
                return {"message": "You have been permanently banned. If you believe this is a mistake, please contact the librarian.", "code": 802}, 200
            else:
                if fetchBan.ban_date >= datetime.now() + timedelta(days=30):
                    fetchUser.last_loged = datetime.now()
                    db.session.commit()
                    return {"message": f"Welcome {fetchUser.user_name}", "code": 801, "user_id": fetchUser.user_id, "token": token}, 200
                else:
                    ban_end = fetchBan.ban_date + timedelta(days=30)
                    ban_date_str = ban_end.strftime("%d %b %Y")
                    days_left = (ban_end - datetime.now()).days
                    return {"message": f"You have been temporarily banned by the librarian. The ban would be lifted on {ban_date_str} ({days_left} days left).", "code": 803}, 200
        else:
            fetchUser.last_loged = datetime.now()
            db.session.commit()
            return {"message": f"Welcome {fetchUser.user_name}", "code": 801, "user_id": fetchUser.user_id, "token": token}, 200
    else:
        return {"message": "Incorrect credentials. Please try again.", "code": 804}, 200


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = request.get_json()
    fetchUser = Users.query.filter_by(
        user_name=form["user_name"], password=form["password"]).first()
    if not fetchUser:
        last_id = Users.query.order_by(Users.user_id.desc()).first().user_id
        next_id = nextID(last_id)
        new_user = Users(
            user_id=next_id,
            user_name=form["user_name"],
            password=form["password"],
            email=form["email"],
            ph_no=form["phone"],
            last_loged=datetime.now(),
            gender=form["gender"],
            doj=datetime.now(),
            dob=datetime.strptime(form["dob"], "%Y-%m-%d")
        )
        db.session.add(new_user)
        db.session.commit()
        
        token = jwt.encode({
            'sub': next_id,
            'iat':datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(hours=6)},
            app.config['SECRET_KEY'])
        return {"message": f"Welcome {form['user_name']}", "code": 801, "user_id": next_id, "token": token}, 200
    else:
        return {"message": "You are already a member. Please signin to proceed", "code": 805}, 200

# Data Retrieval
@app.route("/get-content/books", methods=["GET"])
@token_required
def getBooks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
@token_required
def getLatestBooks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
@token_required
def getAuthors():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
@token_required
def getUsers():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    args = request.args.to_dict()
    if "start" in args:
        del args["start"]
    start = request.args.get('start', 0, type=int)

    if args != {}:
        fetcher = Users.query.filter_by(**args).all()
    else:
        fetcher = Users.query.all()

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


@app.route("/get-content/librarian/users", methods=["GET"])
@librarian_token_required
def getLibrarianUsers():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    args = request.args.to_dict()
    if "start" in args:
        del args["start"]
    start = request.args.get('start', 0, type=int)

    if args != {}:
        fetcher = Users.query.filter_by(**args).all()
    else:
        fetcher = Users.query.all()

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
@token_required
def getSections():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
@token_required
def getRatings():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
@token_required
def getIssues():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
@token_required
def getRequests():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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


@app.route("/get-content/blacklists", methods=["GET"])
@token_required
def getBan():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    args = request.args.to_dict()
    if "start" in args:
        del args["start"]
    start = request.args.get('start', 0, type=int)

    if args != {}:
        fetcher = Blacklists.query.filter_by(**args).all()
    else:
        fetcher = Blacklists.query.offset(start).limit(500).all()

    if fetcher:
        request_list = []
        for requester in fetcher:
            request_list.append({
                "sno": requester.sno,
                "user_id": requester.user_id,
                "ban_type": requester.ban_type,
                "ban_date": requester.ban_date.strftime("%d %b %Y"),
                "ban_end_date": (requester.ban_date + timedelta(days=30)).strftime("%d %b %Y"),
            })
        return request_list, 200
    else:
        abort(404)


@app.route("/get-content/genres", methods=["GET"])
@token_required
def getGenres():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
@token_required
def getRecentBook():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
            fetcher = requests.get(roger,headers=headers).json()[0]
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
@token_required
def searchBooks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    keyword = request.args.to_dict()['keyword']
    fetcherBooks = Books.query.filter(
        Books.book_name.like(f"%{keyword}%")).limit(100).all()
    fetcherAuthors = Books.query.filter(
        Books.author_name.like(f"%{keyword}%")).limit(100).all()
    fetcherSections = db.session.query(Books).join(Sections, Books.section_id == Sections.section_id).filter(
        Sections.section_name.like(f"%{keyword}%")).limit(100).all()
    fetcherGenre = Books.query.filter(
        Books.genre.like(f"%{keyword}%")).limit(100).all()

    byParts = {"titles": fetcherBooks, "authors": fetcherAuthors,
               "sections": fetcherSections, "genres": fetcherGenre}
    allData = {}
    for part in byParts:
        books_list = []
        for book in byParts[part]:
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
        allData[part] = books_list
    print(allData)
    return allData, 200



@app.route("/search-content/my-books", methods=["GET"])
@token_required
def searchMyBooks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
@token_required
def myBooks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    args = request.args.to_dict()
    user_id = args['user_id']

    roger = f"http://127.0.0.1:5000/get-content/issues?user_id={user_id}"
    fetcher = requests.get(roger,headers=headers).json()[::-1]

    today_date = datetime.now()
    books_list = {"Current": [], "History": []}
    for issue in fetcher:
        bookDetails = f"http://127.0.0.1:5000/get-content/books?book_id={issue['book_id']}"
        fetcherBooks = requests.get(bookDetails,headers=headers).json()[0]
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
@token_required
def randomBooks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
@token_required
def getUserStatistics():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    user_id = request.args.to_dict()["user_id"]
    fetchRequests = db.session.query(func.strftime("%Y-%m", Requests.request_date).label('month_year'), func.count(Requests.sno)).filter(
        Requests.user_id == user_id).group_by(func.strftime("%Y-%m", Requests.request_date)).order_by(desc(func.strftime('%Y-%m', Requests.request_date))).limit(10).all()
    
    fetchIssues = db.session.query(func.strftime("%Y-%m", Issues.request_date).label('month_year'), func.count(Issues.sno)).filter(
        Issues.user_id == user_id).group_by(func.strftime("%Y-%m", Issues.request_date)).order_by(desc(func.strftime('%Y-%m', Issues.request_date))).limit(10).all()
        
    fetchUser = Users.query.filter_by(user_id = user_id).first()
    user_data = {
        "user_name": fetchUser.user_name,
        "last_loged": fetchUser.last_loged.strftime("%d %b %Y"),
        "doj": fetchUser.doj.strftime("%d %b %Y"),
        "email": fetchUser.email,
        "gender": fetchUser.gender,
    }
    fetchRating = Ratings.query.filter_by(user_id=user_id).all()
    fetchIssueCount = Issues.query.filter_by(user_id=user_id).all()
    ratings = Ratings.query.filter_by(user_id=user_id).all()
    try:
        fetchIssueDict = {i[0]: i[1] for i in fetchIssues}
        month_dict = {index: calendar.month_abbr[index] for index in range(1, 13)}
        for i in fetchRequests:
            if i[0] in fetchIssueDict:
                fetchIssueDict[i[0]] += i[1]
        barData = [[f"{month_dict[int(i[-2:])]}'{i[2:4]}", fetchIssueDict[i]]
                for i in fetchIssueDict]


        fetchGenres = db.session.query(Books.genre, func.count(Issues.sno).label("issue_count")).join(Books, Books.book_id == Issues.book_id).filter(
            Issues.user_id == user_id).group_by(Books.genre).order_by(desc(func.count(Issues.sno))).order_by(Books.genre).limit(5).all()
        pieData = [[i[0], i[1]] for i in fetchGenres]

        barvals = [i[1] for i in barData]
        active_month = barData[barvals.index(max([i[1] for i in barData]))][0]

        
        days_last_loged = (datetime.now() - fetchUser.last_loged).days
        cardData = {
            "total_issued": len(fetchIssueCount),
            "total_requests": len(fetchRequests),
            "most_active_month": active_month,
            "total_ratings": len(ratings),
            "days_last_loged": days_last_loged
        }

        avg_rate_fetcher = db.session.query(func.avg(Ratings.rating).label(
            "avg_rating")).filter(Ratings.user_id == user_id).first()
        avg_rate = round(avg_rate_fetcher[0], 1) if avg_rate_fetcher else 0.0

        
        score = 100*len(fetchIssueCount) + 250*len(fetchRating)
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
        return {"barchart": barData[::-1], "piechart": pieData, "user_info": user_data, "cardData": cardData, "score": score, "rank": rank, "next_criteria": next_criteria[rank], "next_points": next_points[rank], "numIssues": len(fetchIssueCount), "numRequests": len(fetchRequests), "avg_rating": avg_rate}, 200
    except:
        barData = []
        for i in range(9):
            deltaData = datetime.now() - timedelta(days=30*i)
            barData.append([[f"{deltaData.strftime('%b')}'{deltaData.strftime('%y')}",0]])
        pieData = [["No Genre",1]]
        cardData = {
            "total_issued": len(fetchIssueCount),
            "total_requests": len(fetchRequests),
            "most_active_month": "-",
            "total_ratings": len(ratings),
            "days_last_loged": (datetime.now() - fetchUser.last_loged).days
        }
        score = random.randint(0,400)
        rank = "No"
        next_criteria = ["Read 5 Books"]
        next_pointer = 500
        numIssues = len(fetchIssueCount)
        numRequests = len(fetchRequests)
        avg_rate = 0.0
        return {"barchart": barData[::-1], "piechart": pieData, "user_info": user_data, "cardData": cardData, "score": score, "rank": rank, "next_criteria": next_criteria, "next_points": next_pointer, "numIssues": numIssues, "numRequests": numRequests, "avg_rating": avg_rate}, 200



@app.route("/get-feedbacks", methods=["GET"])
@token_required
def getUserFeedbacks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    user_id = request.args.to_dict()["user_id"]
    fetchRating = requests.get(
        f"http://127.0.0.1:5000/get-content/ratings?user_id={user_id}",headers=headers)
    fetchRating = fetchRating.json()
    fetchIssues = requests.get(
        f"http://127.0.0.1:5000/get-content/issues?user_id={user_id}",headers=headers)
    fetchIssues = fetchIssues.json()
    ratings = set([i['book_id'] for i in fetchRating])
    issues = set([i['book_id'] for i in fetchIssues])
    notrated = list(issues.difference(ratings))
    rated = list(ratings)
    notRatedBooks = []
    for i in notrated:
        booker = requests.get(
            f"http://127.0.0.1:5000/get-content/books?book_id={i}",headers=headers)
        booker = booker.json()[0]
        notRatedBooks.append(booker)
    ratedBooks = []
    for i in rated:
        booker = requests.get(
            f"http://127.0.0.1:5000/get-content/books?book_id={i}",headers=headers)
        booker = booker.json()[0]
        feedback = requests.get(
            f"http://127.0.0.1:5000/get-content/ratings?book_id={i}&user_id={user_id}",headers=headers)
        feedback = feedback.json()[0]

        booker["rating"] = math.ceil(float(feedback["rating"]))
        booker["feedback"] = feedback["feedback"]
        ratedBooks.append(booker)
    return {"Not Rated": notRatedBooks, "Rated": ratedBooks}, 200


@app.route("/get-librarian/previewBook", methods=["GET"])
@librarian_token_required
def getLibrarianBooks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    book_id = request.args.to_dict()["book_id"]
    booker = requests.get(
        f"http://127.0.0.1:5000/get-content/books?book_id={book_id}",headers=headers)
    booker = booker.json()[0]
    issues = requests.get(
        f"http://127.0.0.1:5000/get-content/issues?book_id={book_id}",headers=headers)
    if issues.status_code == 200:
        issues = issues.json()
    else:
        issues = []
    requester = requests.get(
        f"http://127.0.0.1:5000/get-content/requests?book_id={book_id}",headers=headers)
    if requester.status_code == 200:
        requester = requester.json()
    else:
        requester = []
    rater = requests.get(
        f"http://127.0.0.1:5000/get-content/ratings?book_id={book_id}",headers=headers)
    if rater.status_code == 200:
        rater = [float(i['rating']) for i in rater.json()]
    else:
        rater = []
    return {"book": booker, "issues": len(issues), "requests": len(requester), "avg_rating": sum(rater)/len(rater) if len(rater) != 0 else 0}


@app.route("/get-librarian/previewSection", methods=["GET"])
@librarian_token_required
def getLibrarianSections():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    section_id = request.args.to_dict()["section_id"]
    sectioner = requests.get(
        f"http://127.0.0.1:5000/get-content/sections?section_id={section_id}",headers=headers)
    sectioner = sectioner.json()[0]
    return sectioner, 200


@app.route("/get-librarian/previewAuthor", methods=["GET"])
@librarian_token_required
def getLibrarianAuthor():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    author_id = request.args.to_dict()["author_id"]
    sectioner = requests.get(
        f"http://127.0.0.1:5000/get-content/authors?author_id={author_id}",headers=headers)
    sectioner = sectioner.json()[0]
    booker = requests.get(
        f"http://127.0.0.1:5000/get-content/books?author_id={author_id}",headers=headers)
    if booker.status_code == 200:
        booker = booker.json()
    else:
        booker = []
    return {"authorData": sectioner, "numBooks": len(booker)}, 200


@app.route("/get-librarian/requests", methods=["GET"])
@librarian_token_required
def getLibrarianRequests():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    requests = db.session.query(Requests, Books, Users).join(Books, Books.book_id == Requests.book_id).join(
        Users, Users.user_id == Requests.user_id).order_by(Requests.request_date.desc()).all()
    allRequests = []
    for request, book, user in requests:
        allRequests.append({
            "sno": request.sno,
            "book_id": book.book_id,
            "book_name": book.book_name,
            "user_id": user.user_id,
            "user_name": user.user_name,
            "request_date": request.request_date.strftime("%d %b %Y"),
        })
    return jsonify(allRequests), 200


@app.route("/get-librarian/issues", methods=["GET"])
@librarian_token_required
def getLibrarianIssues():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    requests = db.session.query(Issues, Books, Users).join(Books, Books.book_id == Issues.book_id).join(
        Users, Users.user_id == Issues.user_id).order_by(Issues.doi.desc()).limit(100).all()
    allIssues = []
    now = datetime.now()
    for issue, book, user in requests:
        allIssues.append({
            "sno": issue.sno,
            "book_id": book.book_id,
            "book_name": book.book_name,
            "user_id": user.user_id,
            "user_name": user.user_name,
            "doi": issue.doi.strftime("%d %b %Y"),
            "dor": issue.dor.strftime("%d %b %Y"),
            "current_issue": True if now < issue.dor else False
        })
    return jsonify(allIssues), 200


@app.route("/get-librarian/current-user-issues")
@librarian_token_required
def getLibrarianCurrentIssues():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    user_id = request.args.to_dict()["user_id"]
    try:
        requests = db.session.query(Issues).join(
            Users, Users.user_id == Issues.user_id).filter(Users.user_id == user_id).all()
        current_issues = 0
        now = datetime.now()
        for issue in requests:
            if now < issue.dor:
                current_issues += 1
    except:
        current_issues = 0

    return jsonify({"count": current_issues}), 200

# Librarian Dashboard Statistics


@app.route("/get-statistics/librarian/users")
@librarian_token_required
def getStatisticsLibrarianUsers():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    issue_scores = db.session.query(Users.user_id, Users.user_name, func.count(Issues.sno).label(
        "issue_count")).join(Issues, Users.user_id == Issues.user_id).group_by(Users.user_id).all()
    rating_scores = db.session.query(Users.user_id, Users.user_name, func.count(Ratings.sno).label(
        "rating_count")).join(Ratings, Users.user_id == Ratings.user_id).group_by(Users.user_id).all()

    user_scores = []
    for issue, rating in zip(issue_scores, rating_scores):
        user_scores.append({
            "user_id": issue[0],
            "user_name": issue[1],
            "score": issue[2]*100 + rating[2]*250
        })
    scores = [i["score"] for i in user_scores]

    league_count = {"Sage": 0, "Scholar": 0,
                    "Literati": 0, "Reader": 0, "No": 0}
    for i in user_scores:
        scorer = i["score"]
        rank = "Sage" if scorer >= 13750 else "Scholar" if scorer >= 5000 else "Literati" if scorer >= 1750 else "Reader" if scorer >= 500 else "No"
        league_count[rank] += 1

    gender_fetch = db.session.query(Users.gender, func.count(
        Users.gender)).group_by(Users.gender).all()
    gender_count = [[gender_fetch[0][0], gender_fetch[0][1]],
                    [gender_fetch[1][0], gender_fetch[1][1]]]

    day_offset = datetime.now() - timedelta(days=15)
    dataValues = {
        "total_users": len(issue_scores),
        "total_active_users": Users.query.filter(Users.last_loged >= day_offset).count(),
        "most_active_user": issue_scores[scores.index(max(scores))][1],
        "banned_users": Blacklists.query.count()
    }

    active = db.session.query(
        func.strftime("%Y-%m", Issues.request_date).label('month_year'),
        func.count(Issues.sno).label('count'),
    ).group_by(
        func.strftime("%Y-%m", Issues.request_date)
    ).order_by(
        desc(func.strftime('%Y-%m', Issues.request_date))
    ).limit(10)

    month_dict = {
        str(index): calendar.month_abbr[index] for index in range(1, 13)}
    activity_data = [
        [f"{month_dict[str(int(i[0][-2:]))]}'{i[0][:4]}", i[1]] for i in active]
    return {"barData": activity_data[::-1], "pieData": gender_count, "dataValues": dataValues, "userLeague": league_count}, 200


@app.route("/get-statistics/librarian/books")
@librarian_token_required
def getStatisticsLibrarianBooks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    genre_issues = db.session.query(Books.genre, func.count(Issues.sno).label(
        "issue_count")).join(Issues, Books.book_id == Issues.book_id).group_by(Books.genre).order_by(desc(func.count(Issues.sno))).order_by(Books.genre).limit(5).all()
    male_genres = db.session.query(
        Books.genre,
        func.count(Issues.sno).label("issue_count")).join(Issues, Books.book_id == Issues.book_id).join(Users, Users.user_id == Issues.user_id).filter(Users.gender == "Male").group_by(Books.genre).order_by(desc(func.count(Issues.sno))).order_by(Books.genre).limit(5).all()
    female_genres = db.session.query(
        Books.genre,
        func.count(Issues.sno).label("issue_count")).join(Issues, Books.book_id == Issues.book_id).join(Users, Users.user_id == Issues.user_id).filter(Users.gender == "Female").group_by(Books.genre).order_by(desc(func.count(Issues.sno))).order_by(Books.genre).offset(3).limit(5).all()

    today = datetime.today()
    year_diff = func.julianday(today) - func.julianday(Users.dob)
    age = year_diff / 365.25

    age_young = db.session.query(Books.genre, func.count(Issues.sno).label("issue_count")).join(Issues, Books.book_id == Issues.book_id).join(
        Users, Users.user_id == Issues.user_id).filter(age.between(15, 30)).group_by(Books.genre).order_by(desc(func.count(Issues.sno))).order_by(Books.genre).limit(5).all()
    age_middle = db.session.query(Books.genre, func.count(Issues.sno).label("issue_count")).join(Issues, Books.book_id == Issues.book_id).join(
        Users, Users.user_id == Issues.user_id).filter(age.between(31, 60)).group_by(Books.genre).order_by(desc(func.count(Issues.sno))).order_by(Books.genre).offset(5).limit(5).all()
    age_old = db.session.query(Books.genre, func.count(Issues.sno).label("issue_count")).join(Issues, Books.book_id == Issues.book_id).join(
        Users, Users.user_id == Issues.user_id).filter(age.between(61, 80)).group_by(Books.genre).order_by(desc(func.count(Issues.sno))).order_by(Books.genre).offset(3).limit(5).all()

    dataValues = {
        "most_issued": db.session.query(Books.img, (func.count(Issues.sno).label("issue_count"))).join(Issues, Books.book_id == Issues.book_id).group_by(Books.book_id).order_by(desc(func.count(Issues.sno))).limit(1).all()[0][0],
        "most_rated": db.session.query(Books.img, (func.count(Ratings.sno).label("rating_count"))).join(Ratings, Books.book_id == Ratings.book_id).group_by(Books.book_id).order_by(desc(func.count(Ratings.sno))).limit(1).all()[0][0],
        "highest_rated": db.session.query(Books.img, (func.avg(Ratings.rating).label("rating_avg"))).join(Ratings, Books.book_id == Ratings.book_id).group_by(Books.book_id).order_by(desc(func.avg(Ratings.rating))).offset(5).limit(1).all()[0][0],
        "least_rated": db.session.query(Books.img, (func.avg(Ratings.rating).label("rating_avg"))).join(Ratings, Books.book_id == Ratings.book_id).filter(Ratings.rating > 0).group_by(Books.book_id).order_by(func.avg(Ratings.rating)).offset(5).limit(1).all()[0][0],
        "latest_book": db.session.query(Books.img).order_by(desc(Books.date_added)).limit(1).all()[0][0],
    }
    return {"general_genres": [[i[0], i[1]] for i in genre_issues], "male_genres": [[i[0], i[1]] for i in male_genres], "female_genres": [[i[0], i[1]] for i in female_genres], "age_young": [[i[0], i[1]] for i in age_young], "age_middle": [[i[0], i[1]] for i in age_middle], "age_old": [[i[0], i[1]] for i in age_old], "dataValues": dataValues}, 200


@app.route("/get-statistics/librarian/authors")
@librarian_token_required
def getStatisticsLibrarianAuthors():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    avg_country = db.session.query(Authors.country, func.avg(Authors.avg_rating).label(
        "avg_rating")).group_by(Authors.country).order_by(desc(func.avg(Authors.avg_rating))).limit(10).all()
    count_country = db.session.query(Authors.country, func.count(Authors.avg_rating).label(
        "count")).group_by(Authors.country).order_by(desc(func.count(Authors.avg_rating))).limit(5).all()

    today = datetime.today()
    year_diff = func.julianday(today) - func.julianday(Authors.dob)
    age = year_diff / 365.25

    age_group = case(
        (age.between(20, 40), 'Age 20-40'),
        (age.between(40, 70), 'Age 40-70'),
        (age.between(70, 130), 'Above 70'),
        else_='Unknown'
    )
    age_range = case(
        (age.between(30, 40), '30-40'),
        (age.between(40, 50), '40-50'),
        (age.between(50, 60), '50-60'),
        (age.between(60, 70), '60-70'),
        (age.between(70, 80), '70-80'),
        (age.between(80, 90), '80-90'),
        (age.between(90, 100), '90-100'),
        (age.between(100, 110), '100-110'),
        (age.between(110, 120), '110-120'),
        (age.between(120, 130), '120-130'),
        else_='Unknown'
    )
    avg_age = db.session.query(age_range.label("age_range"), func.avg(Authors.avg_rating).label(
        "avg_rating")).group_by(age_range).order_by(desc(Authors.dob)).limit(10).all()
    count_age = db.session.query(age_group.label("age_group"), func.count(
        Authors.avg_rating).label("count")).group_by(age_group).all()

    dataValues = {
        "most_issued": [i for i in db.session.query(Authors.img.label('author_img'), Authors.author_name, func.count(Issues.sno).label("issue_count")).join(Books, Books.author_id == Authors.author_id).join(Issues, Books.book_id == Issues.book_id).group_by(Authors.author_id).order_by(desc(func.count(Issues.sno))).limit(1).all()[0]],
        "most_popular": [i for i in db.session.query(Authors.img.label('author_img'), Authors.author_name, Authors.avg_rating).order_by(desc(Authors.avg_rating)).limit(1).all()[0]],
        "least_popular": [i for i in db.session.query(Authors.img.label('author_img'), Authors.author_name, Authors.avg_rating).order_by(Authors.avg_rating).limit(1).all()[0]],
        "highest_book_rating": [i for i in db.session.query(Authors.img.label('author_img'), Authors.author_name, func.avg(Ratings.rating).label("avg_rating")).join(Books, Books.author_id == Authors.author_id).join(Ratings, Books.book_id == Ratings.book_id).group_by(Authors.author_id).order_by(desc(func.avg(Ratings.rating))).limit(1).all()[0]],
        "lowest_book_rating": [i for i in db.session.query(Authors.img.label('author_img'), Authors.author_name, func.avg(Ratings.rating).label("avg_rating")).join(Books, Books.author_id == Authors.author_id).join(Ratings, Books.book_id == Ratings.book_id).group_by(Authors.author_id).order_by(func.avg(Ratings.rating)).limit(1).all()[0]],
    }
    return {"avg_country": [[i[0], round(i[1], 3)] for i in avg_country], "count_country": [[i[0], i[1]] for i in count_country], "avg_age": [[i[0], round(i[1], 3)] for i in avg_age], "count_age": [[i[0], i[1]] for i in count_age], "dataValues": dataValues}, 200


# Data Insertion
@app.route("/push-content/books", methods=["GET", "POST"])
@librarian_token_required
def pushBooks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/books?book_name={form['book_name']}"
    fetcher = requests.get(roger,headers=headers)
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
@librarian_token_required
def pushNewBooks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/books?book_name={form['book_name']}"
    fetcher = requests.get(roger,headers=headers)
    if request.method == "POST":
        if fetcher.status_code == 404:
            rogerAuthor = f"http://127.0.0.1:5000/get-content/authors?author_name={form['author_name']}"
            fetcherAuthor = requests.get(rogerAuthor,headers=headers)
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
@librarian_token_required
def pushAuthors():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/authors?author_name={form['author_name']}"
    fetcher = requests.get(roger,headers=headers)
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
@librarian_token_required
def pushUsers():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/users?email={form['email']}"
    fetcher = requests.get(roger,headers=headers)
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
@librarian_token_required
def pushSections():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/sections?section_name={form['section_name']}"
    fetcher = requests.get(roger,headers=headers)
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
@token_required
def pushRatings():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/ratings?book_id={form['book_id']}&user_id={form['user_id']}"
    fetcher = requests.get(roger,headers=headers)
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
@librarian_token_required
def pushIssues():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/issues?book_id={form['book_id']}&user_id={form['user_id']}"
    fetcher = requests.get(roger,headers=headers)
    if request.method == "POST":
        if fetcher.status_code == 404:
            last_id = Issues.query.order_by(Issues.sno.desc()).first().sno
            next_id = last_id+1
            new_issue = Issues(
                sno=next_id,
                book_id=form["book_id"],
                user_id=form["user_id"],
                request_date=datetime.now() if "request_date" not in form else datetime.strptime(
                    form["request_date"], "%Y-%m-%d"),
                doi=datetime.now() if "doi" not in form else datetime.strptime(
                    form["doi"], "%Y-%m-%d"),
                dor=datetime.now() +
                timedelta(days=7) if "dor" not in form else datetime.strptime(
                    form["dor"], "%Y-%m-%d"),
            )
            db.session.add(new_issue)
            db.session.commit()
            return f"New Issue added with Sno: {next_id}", 200
        else:
            return {"message": "You have already rated this book, you can't do it again."}, 406


@app.route("/push-content/requests", methods=["GET"])
@token_required
def pushRequests():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    form = request.args.to_dict()
    # roger = f"http://127.0.0.1:5000/get-content/requests?book_id={form['book_id']}&user_id={form['user_id']}"
    # fetcher = requests.get(roger,headers=headers)
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


@app.route("/push-content/blacklists", methods=["GET", "POST"])
@librarian_token_required
def pushBan():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    form = request.get_json()
    roger = f"http://127.0.0.1:5000/get-content/blacklists?user_id={form['user_id']}"
    fetcher = requests.get(roger,headers=headers)
    if fetcher.status_code == 404:
        new_ban = Blacklists(
            user_id=form["user_id"],
            ban_type=form["ban_type"],
            ban_date=datetime.now(),
        )
        db.session.add(new_ban)
        db.session.commit()
        return f"New Ban added User ID: {form['user_id']}", 200
    else:
        abort(406)


# Data Updation
@app.route("/put-content/books", methods=["GET", "PUT"])
@librarian_token_required
def putBooks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
            fetcher = requests.get(roger,headers=headers).json()
            return fetcher, 200
        else:
            return {"message": "Book do not exists."}, 406


@app.route("/put-content/authors", methods=["GET", "PUT"])
@librarian_token_required
def putAuthors():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
            fetcher = requests.get(roger,headers=headers).json()
            return fetcher, 200
        else:
            return {"message": "Author do not exists."}, 406


@app.route("/put-content/users", methods=["GET", "PUT"])
@librarian_token_required
def putUsers():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
            fetcher = requests.get(roger,headers=headers).json()
            return fetcher, 200
        else:
            return {"message": "User do not exists."}, 406


@app.route("/put-content/sections", methods=["GET", "PUT"])
@librarian_token_required
def putSections():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
            fetcher = requests.get(roger,headers=headers).json()
            return fetcher, 200
        else:
            return {"message": "Section do not exists."}, 406

## Special Case
@app.route("/put-content/ratings", methods=["GET", "PUT"])
@token_required
def putRatings():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
            fetcher = requests.get(roger,headers=headers).json()
            return fetcher, 200
        else:
            return {"message": "Rating do not exists."}, 406

## Special Case
@app.route("/put-content/issues", methods=["GET", "PUT"])
@token_required
def putIssues():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    form = request.get_json()
    fetcher = Issues.query.filter_by(
        book_id=form["book_id"], user_id=form["user_id"]).first()
    if request.method == "PUT":
        if fetcher:
            fetcher.dor = datetime.now() if "dor" not in form else datetime.strptime(
                form["dor"], "%Y-%m-%d")
            db.session.commit()
            return {"message": "Issues do not exists."}, 200
        else:
            return {"message": "Issues do not exists."}, 406


@app.route("/put-content/librarian/issues", methods=["GET", "PUT"])
@librarian_token_required
def putLibrarianIssues():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    form = request.get_json()
    fetcher = Issues.query.filter_by(
        book_id=form["book_id"], user_id=form["user_id"]).first()
    if request.method == "PUT":
        if fetcher:
            fetcher.dor = datetime.now() if "dor" not in form else datetime.strptime(
                form["dor"], "%Y-%m-%d")
            db.session.commit()
            return {"message": "Issues do not exists."}, 200
        else:
            return {"message": "Issues do not exists."}, 406


@app.route("/put-content/blacklists", methods=["GET", "PUT"])
@librarian_token_required
def putBan():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    form = request.get_json()
    fetcher = Blacklists.query.filter_by(user_id=form["user_id"]).first()
    if request.method == "PUT":
        if fetcher:
            for i in form:
                try:
                    setattr(fetcher, i, datetime.strptime(form[i], "%Y-%m-%d"))
                except:
                    setattr(fetcher, i, form[i])
            db.session.commit()
            return {"message": "Ban changed"}, 200
        else:
            return {"message": "Blacklists do not exists."}, 406


# Data Deletion
@app.route("/delete-content/books", methods=["GET", "DELETE"])
@librarian_token_required
def deleteBooks():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    args = request.args.to_dict()
    fetcher = Books.query.filter_by(book_id=args["book_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"Book with ID {args['book_id']} deleted"}, 200
    else:
        return {"message": "Book do not exist"}, 406


@app.route("/delete-content/authors", methods=["GET", "DELETE"])
@librarian_token_required
def deleteAuthors():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    args = request.args.to_dict()
    fetcher = Authors.query.filter_by(author_id=args["author_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"Author with ID {args['author_id']} deleted"}, 200
    else:
        return {"message": "Author do not exist"}, 406


@app.route("/delete-content/users", methods=["GET", "DELETE"])
@librarian_token_required
def deleteUsers():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    args = request.args.to_dict()
    fetcher = Users.query.filter_by(user_id=args["user_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"User with ID {args['user_id']} deleted"}, 200
    else:
        return {"message": "User do not exist"}, 406


@app.route("/delete-content/sections", methods=["GET", "DELETE"])
@librarian_token_required
def deleteSections():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    args = request.args.to_dict()
    fetcher = Sections.query.filter_by(section_id=args["section_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"Section with ID {args['section_id']} deleted"}, 200
    else:
        return {"message": "Section do not exist"}, 406


@app.route("/delete-content/ratings", methods=["GET", "DELETE"])
@librarian_token_required
def deleteRatings():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
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
@librarian_token_required
def deleteIssues():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    args = request.args.to_dict()
    fetcher = Issues.query.filter_by(
        book_id=args["book_id"], user_id=args["user_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"Issue with book id {args['book_id']} & user id {args['book_id']} deleted"}, 200
    else:
        return {"message": "Issue do not exist"}, 406


@app.route("/delete-content/requests", methods=["GET", "DELETE"])
@librarian_token_required
def deleteRequests():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    args = request.args.to_dict()
    fetcher = Requests.query.filter_by(
        book_id=args["book_id"], user_id=args["user_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"Request with book id {args['book_id']} & user id {args['book_id']} deleted"}, 200
    else:
        return {"message": "Request do not exist"}, 406


@app.route("/delete-content/blacklists", methods=["GET", "DELETE"])
@librarian_token_required
def deleteBan():
    token = request.headers.get('x-access-token')
    headers = {
        'x-access-token': token
    }
    args = request.args.to_dict()
    fetcher = Blacklists.query.filter_by(user_id=args["user_id"]).first()
    if fetcher:
        db.session.delete(fetcher)
        db.session.commit()
        return {"message": f"Ban with user id {args['user_id']} deleted"}, 200
    else:
        return {"message": "Ban do not exist"}, 406


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
#     Blacklists.__table__.create(db.engine)


if __name__ == "__main__":
    app.run(debug=True)
