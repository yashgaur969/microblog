from flask import request
from flask_mail import Message

from app import app, db, mail
from app.models import User, StaticEmailTemplate


@app.route('/profile/<username>/<email>', methods=['PUT', 'POST', 'GET', 'DELETE'])
def http_method(username, email):
    if request.method == 'PUT':                                                          # update operation
        new_email = 'my_new_email@example.com'
        user = User.query.filter_by(username=username, email=email).first()
        user.email = new_email
        db.session.commit()
        return 'updated email id is ' + new_email

    if request.method == 'GET':                                                           # read operation
        user = User.query.filter_by(username=username, email=email)
        user = user.first()
        return 'email is {}'.format(user.email)

    if request.method == 'DELETE':                                                         # delete operation
        user = User.query.filter_by(username=username, email=email).delete()
        db.session.commit()
        return 'success deletion with username {}'.format(username)

    if request.method == 'POST':                                                            # create operation
        u = User(username=username, email=email)
        db.session.add(u)
        db.session.commit()
        return 'create new user with email {}'.format(email)


@app.route('/xyz', methods=['GET'])
def xyzmethod():                                                                          # to check what all users are added in the database
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
    return new_email_template.header + new_email_template.body


@app.route('/mail/<eid>', methods=['GET'])                                                     # method to create static email template
def index(eid):
    if request.method == 'GET':
        users = User.query.all()
        template = StaticEmailTemplate.query.filter_by(eid=eid).first()
        for r in users:
            msg = Message(sender='yashgaur969@gmail.com', recipients=[r.email])
            msg.body = template.header + " " + template.body
            msg.subject = template.subject
            msg.html = msg.body
            mail.send(msg)
        return "Email Sent"


@app.route('/dynamic-email', methods=['GET'])
def dynamic_mail():                                                                             #method to create dynamic email template
    if request.method == 'GET':
        users = User.query.all()
        for rr in users:
            msg = Message('Sale Offer', sender='yashgaur969@gmail.com', recipients=[rr.email])
            msg.body = "<h1>New Year Sale</h1><p>hi {}</p><p>Wish you a very happy new year. As you have done " \
                       "shopping worth 7000 this year,we have surprise for you.</p><p>Below is a coupon for this new " \
                       "year sale to bring more joy to in the coming year</p>".format(rr.username)
            msg.html = msg.body
            mail.send(msg)
        return "Email Sent"
