from .database import db


class User(db.Model):
    __tablename__ = "user"
    user_id =  db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_name = db.Column(db.String,)
    user_mail = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(30), nullable = False)

    # bookings = db.relationship('Booking', backref="user")


class Theater(db.Model):
    __tablename__ = "theater"
    theater_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    theater_name =db.Column(db.String(30), unique = True, nullable = False)
    place =db.Column(db.String(30),nullable = False)
    location =db.Column(db.String(30),nullable = False)
    capacity =db.Column(db.Integer,nullable = False)
    rating = db.Column(db.Float,default = 0)

    shows = db.relationship('Theater_Show', back_populates='theater')


class Show(db.Model):
    __tablename__ = "show"
    show_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    show_name =db.Column(db.String(30), unique = True, nullable = False)
    language =db.Column(db.String(30),nullable = False)
    duration =db.Column(db.String(30),nullable = False)
    rating = db.Column(db.Float,default = 0)

    theaters = db.relationship('Theater_Show', back_populates='show')


class Theater_Show(db.Model):
    __tablename__ = "theater_show"
    theater_show_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    theater_id = db.Column(db.Integer, db.ForeignKey("theater.theater_id"))
    show_id = db.Column(db.Integer, db.ForeignKey("show.show_id"))
    price = db.Column(db.Float, nullable=False)
    show_time = db.Column(db.DateTime)


    show = db.relationship('Show', back_populates ="theaters")
    theater = db.relationship('Theater', back_populates="shows")
    # bookings = db.relationship('Booking', backref="theater_show")


class Booking(db.Model):
    __tablename__ = "booking"
    booking_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    t_s_id = db.Column(db.Integer, db.ForeignKey("theater_show.theater_show_id"))
    booking_time = db.Column(db.DateTime)
    total_ticket_booked = db.Column(db.Integer)
    total_paid = db.Column(db.Float)

    # user = db.relationship('User', backref='bookings')
    # theater_show = db.relationship('Theater_Show', backref = 'bookings')
