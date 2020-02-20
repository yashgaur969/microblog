from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String())

    def __repr__(self):
        return '<User {}>'.format(self.email)


class StaticEmailTemplate(db.Model):  # email template class
    eid = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String())
    header = db.Column(db.String())
    body = db.Column(db.String())

    def __repr__(self):
        return '<Email Template is {}>'.format(self.header + self.body)


class Customer(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    c_first_name = db.Column(db.String())
    c_last_name = db.Column(db.String())
    c_gender = db.Column(db.String())
    c_email = db.Column(db.String())
    c_age = db.Column(db.Integer)
    c_address = db.Column(db.String())
    c_state = db.Column(db.String())
    c_zipcode = db.Column(db.Integer)
    c_phonenumber = db.Column(db.String())
    c_registrationdate = db.Column(db.String())

    def __repr__(self):
        return "Customer details Updated"


class Orders(db.Model):
    oid = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.String())
    total_price = db.Column(db.Integer)

    def __repr__(self):
        return "order details"


class Product(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    product_sku = db.Column(db.String())
    product_name = db.Column(db.String())
    product_brand = db.Column(db.String())
    product_description = db.Column(db.String())
    product_color = db.Column(db.String())
    product_unitprice = db.Column(db.Integer)

    def __repr__(self):
        return "product details"


class Reviews(db.Model):
    rid = db.Column(db.Integer, primary_key=True)
    user_product_id = db.Column(db.Integer)
    product_rating = db.Column(db.String())
    review_title = db.Column(db.String())

    def __repr__(self):
        return "review details"


class UserProductList(db.Model):
    user_product_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    order_id = db.Column(db.Integer)

    def __repr__(self):
        return "UserProductList updated"
