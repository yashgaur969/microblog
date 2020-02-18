from flask import request

from app import app, db
from app.models import User


@app.route('/profile/<username>/<email>', methods=['PUT', 'POST', 'GET', 'DELETE'])
def http_method(username, email):
    if request.method == 'PUT':
        new_email = 'my_new_email@example.com'
        user = User.query.filter_by(username=username, email=email).first()
        user.email = new_email
        db.session.commit()
        return 'updated email id is ' + new_email

    if request.method == 'GET':
        user = User.query.filter_by(username=username, email=email)
        user = user.first()
        return 'email is {}'.format(user.email)

    if request.method == 'DELETE':
        user = User.query.filter_by(username=username, email=email).delete()
        db.session.commit()
        return 'success deletion with username {}'.format(username)

    if request.method == 'POST':
        u = User(username=username, email=email)
        db.session.add(u)
        db.session.commit()
        return 'create new user with email {}'.format(email)



