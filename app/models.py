from app import db


class User(db.Model):                                                       #user class on which CRUD operations are performed
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class StaticEmailTemplate(db.Model):                                 #email template class
    eid = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(120))
    subject = db.Column(db.String(120))
    body = db.Column(db.String())
    footer = db.Column(db.String(120))

    def __repr__(self):
        return '<Email Template is {}>'.format(self.header + self.body)
