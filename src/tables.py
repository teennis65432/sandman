from webapp import app, db
from src.models import User
from src.models import Shift
from sqlalchemy import asc
from datetime import datetime, timedelta, date
import src.shiftHelper as shiftHelper


def createTables():
    with app.app_context():
        db.create_all()


def getTables():
    with app.app_context():
        return db.engine.table_names()


def getColumns(table):
    with app.app_context():
        if not db.engine.has_table(table):
            return "table " + table + " does not exist"
        conn = db.engine.connect()
        return conn.execute("SELECT * FROM " + table).keys()


def addUser(user_id, name, password, manager):
    newUser = User(user_id=user_id, name=name, password=password, manager=manager)
    with app.app_context():
        db.session.add(newUser)
        db.session.commit()


def removeUser(id):
        user = getUserByID(id)
        with app.app_context():
            if user is not None:
                db.session.delete(user)
                db.session.commit()


def getAllUsers():
    with app.app_context():
        users = User.query.all()
        return users

def getUserByID(id):
    with app.app_context():
        employee = User.query.filter_by(id=id).first()
        return employee

    return None

def getUser(user_id):
    with app.app_context():
        employee = User.query.filter_by(user_id=user_id).first()
        return employee

    return None


def checkLogin(user, password):
    with app.app_context():
        employee = User.query.filter_by(user_id=user).first()
        if employee is not None:
            if employee.password == password:
                return employee

    return None


def addShift(user_id, start, end):
    newShift = Shift(user_id=user_id, start=start, end=end)
    with app.app_context():
        db.session.add(newShift)
        db.session.commit()

def removeShift(id):
        shift = getShiftByID(id)
        with app.app_context():
            if shift is not None:
                db.session.delete(shift)
                db.session.commit()

def getShiftByID(id):
    with app.app_context():
        shift = Shift.query.filter_by(id=id).first()
        return shift

    return None

def getAllShifts():
    with app.app_context():
        shifts = Shift.query.order_by(asc(Shift.start)).all()
        return shifts

def getTodayShift(userid):
    with app.app_context():
        todays_datetime = datetime(datetime.today().year, datetime.today().month, datetime.today().day)

        shift = Shift.query.filter_by(user_id=userid).filter(Shift.start>=todays_datetime).order_by(asc(Shift.start)).first()
        return shift

def getWeekShifts(day):
    with app.app_context():
        
        sunday = shiftHelper.convertToDateTime(day)

        shifts = Shift.query.filter(Shift.start>=sunday).order_by(asc(Shift.start)).all()
        return shifts

def clockIn(shift_id):
    with app.app_context():
        s = Shift.query.get(shift_id)
        s.clockin = datetime.now()
        db.session.commit()

def clockOut(shift_id):
    with app.app_context():
        s = Shift.query.get(shift_id)
        s.clockout = datetime.now()
        db.session.commit()

def getUserShifts(userid):
    with app.app_context():
        todays_datetime = datetime(datetime.today().year, datetime.today().month, 1)

        shifts = Shift.query.filter_by(user_id=userid).filter(Shift.start>=todays_datetime).order_by(asc(Shift.start)).all()
        return shifts