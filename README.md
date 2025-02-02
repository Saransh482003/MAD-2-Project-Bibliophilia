# Bibliophilia : Library Management Application
![Biblo1](https://github.com/user-attachments/assets/f0938fb8-4643-4fa1-9f32-134c5ae48d81)
This project was created to fulfill the requirements for the MAD-2 Project of the **BS in Data Science and Application** degree program from **Indian Institute of Technology, Madras (IIT Madras)**.

Bibliophilia is a role-based library management application designed to provide book enthusiasts with a seamless and enjoyable experience. The application features a Vue.js frontend and a robust Flask backend, managed by a single librarian who oversees all operations, including accepting requests, adding new books, and managing user accounts.

Kindly watch this video demostration of the project: [Go to Video Demo](https://drive.google.com/file/d/1u6c1jiQ3QPmCvZ7iAZFHSoC-_7nwuaia/view?usp=sharing)

## Technologies Used

Multiple technologies ranging from frontend to backend flanks were used to develop this project. 
![techs](https://github.com/user-attachments/assets/d17f0949-ce31-42a8-b846-1fb703af2b15)
- **Frontend:** Vue.js, Chart.js
- **Backend:** Flask, Flask-Restful, Flask-SQLAlchemy
- **Database:** SQLite
- **Caching & Task Scheduling:** Redis, Celery

## System Architecture

The application is divided into three main components:

1. **Database Management:** Powered by SQLite, with models designed using Flask-SQLAlchemy.
2. **Backend:** Built with Flask, handling API endpoints, Redis caching, and Celery batch jobs.
3. **Frontend:** Developed using Vue.js, with dynamic data population and real-time updates.

### Database Models

The database models are meticulously designed with appropriate constraints to ensure data integrity. Below is a snippet of the `Books` model:

```python
class Books(db.Model):
    book_id = db.Column(db.String, primary_key=True)
    book_name = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    author_id = db.Column(db.String, nullable=False)
    author_name = db.Column(db.String, nullable=False)
    section_id = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False, default="fiction")
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.strftime(datetime.today(), "%d-%m-%Y"))
```

## API Management

The database's CRUD operations are exclusively executed through APIs, leveraging Flask-Restful to implement essential functionalities such as GET, POST, PUT, and DELETE operations at specific endpoints. This ensures a robust and standardized mechanism for interacting with the database.

## User and Librarian Functionalities

Readers and the Librarian are the two types of users who differ in levels of functionalities and authority.

### Reader Features:
- View all books
- Request books
- Return issued books
- View dashboard and statistics
- Give feedback

### Librarian Features:
- Add/Edit/Delete books, authors, sections, etc.
- Ban/Interdict users
- View overall statistics
- Manage issue requests

## Celery Batch Jobs

Three types of asynchronous batch jobs have been implemented:

1. **Daily Task:** Triggered daily for routine operations.
2. **Monthly Task:** Triggered monthly for periodic operations.
3. **User-Triggered Task:** Triggered by user actions.

