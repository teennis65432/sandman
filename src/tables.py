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
                return 'table ' + table + ' does not exist'
        conn = db.engine.connect()
        return conn.execute('SELECT * FROM ' + table).keys()

def addUser(name, password, manager):
        newUser = User(name=name, password=password, manager=manager)
        with app.app_context():
                db.session.add(newUser)
                db.session.commit()

def getAllUsers():
        with app.app_context():
                users = User.query.all()

                for user in users:
                        print(user)
                        print(user.name)

def getUser(id):
        with app.app_context():
                employee = User.query.filter_by(id=id).first()
                return employee
                
        return None

def checkLogin(user, password):
        with app.app_context():
                employee = User.query.filter_by(name=user).first()
                if (employee is not None):
                        print(employee)
                        print(employee.password)
                        if(employee.password == password):
                                return True
                
        return False
        
