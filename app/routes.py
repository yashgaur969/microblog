from flask import request

from app import app, db
from app.models import User, StaticEmailTemplate


@app.route('/profile/<username>/<email>', methods=['PUT', 'POST', 'GET', 'DELETE'])
def http_method(username, email):
    if request.method == 'PUT':                                                  #update operation
        new_email = 'my_new_email@example.com'
        user = User.query.filter_by(username=username, email=email).first()
        user.email = new_email
        db.session.commit()
        return 'updated email id is ' + new_email

    if request.method == 'GET':                                                   #read operation
        user = User.query.filter_by(username=username, email=email)
        user = user.first()
        return 'email is {}'.format(user.email)

    if request.method == 'DELETE':                                                 #delete operation
        user = User.query.filter_by(username=username, email=email).delete()
        db.session.commit()
        return 'success deletion with username {}'.format(username)

    if request.method == 'POST':                                                  #create operation
        u = User(username=username, email=email)
        db.session.add(u)
        db.session.commit()
        return 'create new user with email {}'.format(email)


@app.route('/xyz', methods=['GET'])
def xyzmethod():                                                                  #to check what all users are added in the database
    if request.method == 'GET':
        app.logger.info("xyz is called")
        u = User.query.all()
        return 'user list {}'.format(u)


@app.route('/email', methods=['PUT', 'POST', 'GET', 'DELETE'])
def email_template():
    if request.method == 'POST':
        email_structure = request.get_json(force=True)
        subject = email_structure['subject']
        header = email_structure['header']
        body = email_structure['body']
        new_email_template = StaticEmailTemplate(subject=subject, header=header, body=body)
        db.session.add(new_email_template)
        db.session.commit()
    return email_structure
