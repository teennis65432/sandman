from webapp import app, db
from src.models import User


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
        print(employee)
        if employee is not None:
            if employee.password == password:
                return employee

    return None
