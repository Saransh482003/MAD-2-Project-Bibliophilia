import smtplib
import ssl
from email.message import EmailMessage
from celery import shared_task
from celery.contrib.abortable import AbortableTask
from models import *
from datetime import datetime, timedelta
from app import app

# @shared_task(bind=True, base=AbortableTask, ignore_result=False)
def send_email_reminder():
    with app.app_context():
        last_logers = db.session.query(Users.user_id, Users.user_name, Users.email, Users.ph_no, Users.last_loged, Users.gender).filter(Users.last_loged <= datetime.now() - timedelta(days=15)).group_by(Users.user_id).all()
        returner = db.session.query(Users.user_id, Users.user_name, Users.email, Users.ph_no, Users.last_loged, Users.gender, Issues.book_id, Books.book_name).join(Issues, Issues.user_id == Users.user_id).join(Books, Books.book_id == Issues.book_id).filter(Issues.dor == datetime.now()+timedelta(days=1)).group_by(Users.user_id).all()

        email_sender = 'saini.saransh03@gmail.com'
        email_password = 'qctm tkdc bkch xbkj'
        em = EmailMessage()
        context = ssl.create_default_context()

        subject = 'Bibliophilia - Daily Reminder'
        for i in last_logers:
            body = f"""
            Hi {i[1]},
            It's been {(datetime.now() - i[4]).days} days since your last visit. Login now to dive again into the world of books.

            Regards,
            Librarian,
            Bibliophilia
            """

            em['From'] = email_sender
            # em['To'] = i[2]
            em['To'] = "ss2077@dseu.ac.in"
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, "ss2077@dseu.ac.in", em.as_string())


        rem = EmailMessage()

        subject_books = 'Bibliophilia - Book Return Approaching'
        for i in returner:
            body = f"""
            Hi {i[1]},
            The return date for the book: {i[7]} is tommorrow i.e. {datetime.now() + timedelta(days=1)}. You can return the book earlier if you wish otherwise you can re-issue after the Return Date.

            Regards,
            Librarian,
            Bibliophilia
            """

            rem['From'] = email_sender
            # rem['To'] = i[2]
            rem['To'] = "ss2077@dseu.ac.in"
            rem['Subject'] = subject_books
            rem.set_content(body)


            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, "ss2077@dseu.ac.in", rem.as_string())
        return {"message":f"Emails sent to {len(last_logers)} inactive users and {len(returner)} return date approaching users."}

print(send_email_reminder())