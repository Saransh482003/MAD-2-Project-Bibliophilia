# Bibliophilia : Library Management Application
![Biblo1](https://github.com/user-attachments/assets/f0938fb8-4643-4fa1-9f32-134c5ae48d81)
This project was created to fulfill the requirements for the MAD-2 Project of the **BS in Data Science and Application** degree program from **Indian Institute of Technology, Madras (IIT Madras)**.

Bibliophilia is a role-based library management application designed to provide book enthusiasts with a seamless and enjoyable experience. The application features a Vue.js frontend and a robust Flask backend, managed by a single librarian who oversees all operations, including accepting requests, adding new books, and managing user accounts.

Kindly watch this video demostration of the project: [Go to Video Demo](https://drive.google.com/file/d/1u6c1jiQ3QPmCvZ7iAZFHSoC-_7nwuaia/view?usp=sharing)

LinkedIn Post: [Go to LinkedIn Post]([https://drive.google.com/file/d/1u6c1jiQ3QPmCvZ7iAZFHSoC-_7nwuaia/view?usp=sharing](https://www.linkedin.com/posts/saranshsaini48_linkedin-vuejs-flask-activity-7252158841109295104-Gj8p?utm_source=share&utm_medium=member_desktop))

## Technologies Used

Multiple technologies ranging from frontend to backend flanks were used to develop this project. 

![techs](https://github.com/user-attachments/assets/d17f0949-ce31-42a8-b846-1fb703af2b15)

- **Frontend:** Vue.js, Chart.js
- **Backend:** Flask, Flask-Restful, Flask-SQLAlchemy
- **Database:** SQLite
- **Caching & Task Scheduling:** Redis, Celery

## System Architecture

![image](https://github.com/user-attachments/assets/73aa3eff-c6ae-439a-8b1f-c1d84c569241)

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

## Multi-User Functionalities and Features

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

![image](https://github.com/user-attachments/assets/3408465f-da33-4628-bd2c-7e7cba60f143)

Three types of asynchronous batch jobs have been implemented:

1. **Daily Task:** Triggered daily for routine operations.
2. **Monthly Task:** Triggered monthly for periodic operations.
3. **User-Triggered Task:** Triggered by user actions.


## Frontend

![image](https://github.com/user-attachments/assets/67d553ac-526e-49de-a5a9-dd90ffb8f297)

The frontend is designed to offer a seamless and user-friendly experience. Key features include:

- **View Navigation Bar:** Allows users to navigate between different pages.
- **Side Navigation Bar:** Facilitates smooth transitions between various tabs on the same page.
- **Preview Panel:** Enables users to view comprehensive details of the selected book and offers options to either request the book for issue or save it for later.

## Database Schema

![image](https://github.com/user-attachments/assets/4c40ef13-6cf7-4acd-ab64-9154536f5aec)

|Books|Authors|Users|Sections|
|------|------|-----|------------|
|book_id|author_id|section_id|section_name|
|book_name|author_name|section_id|img|
|img|img|img|date_added|
|author_id|dob|date_added||
|author_name|dod|||
|section_id|country|||
|genre|org_rating|||
|date_added|||

## Additional Features

A league/ranking system has been implemented for users, determined by their activity level using the formula:

![image](https://github.com/user-attachments/assets/5be1b9fe-59ab-4cd2-9f87-5fcaa4ae02e6)

```python
100 × Number of Books Issued + 250 × Number of Books Rated
```

Users are categorized into four leagues in ascending order of rank:

1. Reader
2. Literati
3. Scholar
4. Sage

Advancement to higher leagues requires meeting specific criteria. All relevant information is displayed on the user's dashboard.

## Conclusion

Developing this application was an enjoyable and rewarding experience. Transitioning from ReactJS to VueJS was relatively straightforward, while working with Redis and Celery provided valuable hands-on experience.
