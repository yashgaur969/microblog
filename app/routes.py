import csv
import io

from flask import request
from flask_mail import Message

from app import app, db, mail
from app.models import User, StaticEmailTemplate, UserProductList, Customer, Orders, Product, Reviews


@app.route('/')
def indexx():
    return "hello world"


@app.route('/profile/<username>/<email>', methods=['PUT', 'POST', 'GET', 'DELETE'])
def http_method(username, email):
    if request.method == 'PUT':  # update operation
        new_email = 'my_new_email@example.com'
        user = User.query.filter_by(username=username, email=email).first()
        user.email = new_email
        db.session.commit()
        return 'updated email id is ' + new_email

    if request.method == 'GET':  # read operation
        user = User.query.filter_by(username=username, email=email).first()
        return 'email is' + email

    if request.method == 'DELETE':  # delete operation
        user = User.query.filter_by(username=username, email=email).delete()
        db.session.commit()
        return 'success deletion with username {}'.format(username)

    if request.method == 'POST':  # create operation
        u = User(username=username, email=email)
        db.session.add(u)
        db.session.commit()
        return 'create new user with email {}'.format(email)


@app.route('/xyz', methods=['GET'])
def xyzmethod():  # to check what all users are added in the database
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


@app.route('/mail/<eid>', methods=['GET'])  # method to create static email template
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
def dynamic_mail():  # method to create dynamic email template
    if request.method == 'GET':
        users = User.query.all()
        for rr in users:
            msg = Message('Sale Offer', sender='yashgaur969@gmail.com', recipients=[rr.email])
            msg.body = "<h1>New Year Sale</h1><p>hi {}</p><p>Wish you a very happy new year. As you have done " \
                       "shopping worth 7000 this year,we have surprise for you.</p><p>Below is a coupon for this new " \
                       "year sale to bring more joy to in the coming year</p>".format(rr.username)
            msg.html = msg.body  # to display the body of the mail in html format
            mail.send(msg)
        return "Email Sent"


@app.route('/customerList', methods=['POST'])
def updating_customer_list():
    if request.method == 'POST':
        csv_file = request.files['filename']
        csv_file = io.TextIOWrapper(csv_file, encoding="UTF-8")
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            customerlist = Customer(cid=row[0], c_first_name=row[1], c_last_name=row[2], c_gender=row[3],
                                    c_email=row[4], c_age=row[5], c_address=row[6], c_state=row[7], c_zipcode=row[8],
                                    c_phonenumber=row[9], c_registrationdate=row[10])
            db.session.add(customerlist)
        db.session.commit()
        return "customer list updated"


@app.route('/orderList', methods=['POST'])
def updating_order_list():
    if request.method == 'POST':
        csv_file = request.files['filename']
        csv_file = io.TextIOWrapper(csv_file, encoding="UTF-8")
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            orderlist = Orders(oid=row[0], purchase_date=row[1], total_price=row[2])
            db.session.add(orderlist)
        db.session.commit()
        return "order list updated"


@app.route('/productList', methods=['POST'])
def updating_product_list():
    if request.method == 'POST':
        csv_file = request.files['filename']
        csv_file = io.TextIOWrapper(csv_file, encoding="UTF-8")
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            productlist = Product(pid=row[0], product_sku=row[1], product_name=row[2], product_brand=row[3],
                                  product_description=row[4], product_color=row[5], product_unitprice=row[6])
            db.session.add(productlist)
        db.session.commit()
        return "product list updated"


@app.route('/reviewList', methods=['POST'])
def updating_review_list():
    if request.method == 'POST':
        csv_file = request.files['filename']
        csv_file = io.TextIOWrapper(csv_file, encoding="UTF-8")
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            reviewlist = Reviews(rid=row[0], user_product_id=row[1], product_rating=row[2], review_title=row[3])
            db.session.add(reviewlist)
        db.session.commit()
        return "review list updated"


@app.route('/userProductList', methods=['POST'])  # to import the User product list csv file
def updating_user_product_list():
    if request.method == 'POST':
        csv_file = request.files['filename']
        csv_file = io.TextIOWrapper(csv_file, encoding="UTF-8")
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            userproductlist = UserProductList(user_product_id=row[0], user_id=row[1], product_id=row[2],
                                              quantity=row[3], order_id=row[4])
            db.session.add(userproductlist)
        db.session.commit()
        return "user product list updated"


@app.route('/customers/gender/<gender>', methods=['GET'])
def customer_filter_using_gender(gender):
    if request.method == 'GET':
        filter1 = {}
        customer = Customer.query.filter(Customer.c_gender == gender)
        for c in customer:
            filter1.update({c.cid: c.c_first_name})
        return filter1


@app.route('/customers/age/<age>', methods=['GET'])
def customer_filter_using_age(age):
    if request.method == 'GET':
        filter2 = {}
        customer = Customer.query.filter(Customer.c_age == age)
        for c in customer:
            filter2.update({c.cid: c.c_first_name})
        return filter2


@app.route('/customers/state/<state>', methods=['GET'])
def customer_filter_using_state(state):
    if request.method == 'GET':
        filter3 = {}
        customer = Customer.query.filter(Customer.c_state == state)
        for c in customer:
            filter3.update({c.cid: c.c_first_name})
        return filter3

# @app.route('/customers/govUser', methods=['GET'])
# def customer_filter_using_mail():
#     if request.method == 'GET':
#         filter4 = {}
#         customer = Customer.query.filter(".gov" in Customer.c_email)
#         for c in customer:
#             filter4.update({c.cid: c.c_first_name})
#         return filter4
