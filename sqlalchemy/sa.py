from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.sqlite', echo=True)

Session = sessionmaker(bind=engine)
s = Session()

Base = declarative_base(bind=engine)

class User(Base):
	__tablename__ = 'user'
	id = Column('user_id', Integer, primary_key=True)

# remove the User object that exists in metadata from the db (will error if it can't be found?) issues:
# >>> DROP TABLE user
Base.metadata.drop_all()
# create the User object that exists in metadata. issues:
"""
CREATE TABLE user (
        user_id INTEGER NOT NULL,
        PRIMARY KEY (user_id)
)
"""
Base.metadata.create_all()
