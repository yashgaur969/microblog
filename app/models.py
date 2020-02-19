from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class StaticEmailTemplate(db.Model):                                 #email template class
    eid = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String())
    header = db.Column(db.String())
    body = db.Column(db.String())

    def __repr__(self):
        return '<Email Template is {}>'.format(self.header + self.body)
