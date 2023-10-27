import mysql.connector

import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/mojabazadotestow',echo=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f"<User -> name: {self.name}, full name: {self.fullname}, nick name: {self.nickname}>"


Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

us1 = User(name='Marcin',fullname='Marcin Albiniak',nickname='al')
session.add(us1)

us2 = User(name='Ewa',fullname='Ewa Kot',nickname='ewcia')
session.add(us2)

us3 = User(name='Olaf',fullname='Olaf Knot',nickname='alfi')
session.add(us3)

us4 = User(name='Maria',fullname='Maria Nowak',nickname='mari')
session.add(us4)

session.commit()
print("_"*45)

for s in session.query(User).all():
    print(s)

print("_"*45)

for s in session.query(User).filter(User.nickname=='alfi'):
    print(s.fullname)
