# models.py
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create SQLite engine and session
engine = create_engine('sqlite:///db/restaurant.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define Base for model classes
Base = declarative_base()

# User table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # e.g., Customer, Manager, DeliveryAgent

    def save(self):
        session.add(self)
        session.commit()

    @staticmethod
    def get_all():
        return session.query(User).all()

# MenuItem table
class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def save(self):
        session.add(self)
        session.commit()

    @staticmethod
    def get_all():
        return session.query(MenuItem).all()

# Order table
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('users.id'))
    status = Column(String, default='Pending')
    customer = relationship("User")

    def save(self):
        session.add(self)
        session.commit()

    @staticmethod
    def get_all():
        return session.query(Order).all()

# Rating table
class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Integer, nullable=False)
    customer = relationship("User")

    def save(self):
        session.add(self)
        session.commit()

    @staticmethod
    def get_all():
        return session.query(Rating).all()

# Create all tables
Base.metadata.create_all(engine)