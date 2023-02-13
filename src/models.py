import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table user follower
    # Notice that each column is also a normal Python instance attribute
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_from = relationship(User, foreign_keys=[user_from_id])
    user_to = relationship(User, foreign_keys=[user_to_id])

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table user comment
    # Notice that each column is also a normal Python instance attribute
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
   
    post = relationship("Post")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table user post
    # Notice that each column is also a normal Python instance attribute
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table user media
    # Notice that each column is also a normal Python instance attribute
    id = Column(Integer, primary_key=True)
    media_type = Column(String, nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
     
    post = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e