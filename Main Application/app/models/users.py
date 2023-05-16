# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

#from flask_login import UserMixin

#from sqlalchemy.orm import relationship
#from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

#from app import login_manager

#from app.authentication.util import hash_pass

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression as exp
from sqlalchemy import Column,String,DateTime,ForeignKey,Boolean,LargeBinary
from sqlalchemy import func,text
from . import Base

class Users(Base):

    __tablename__ = 'users'

    id                 = Column(UUID(True), primary_key=True, server_default=text('gen_random_uuid()'))
    username           = Column(String(64), unique=True)
    email              = Column(String(64), unique=True)
    password           = Column(LargeBinary)
    is_authenticated   = Column(Boolean)
    is_active          = Column(Boolean, server_default='t')
    is_anonymous       = Column(Boolean, server_default='f')
    dateCreated        = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    dateLastLogin      = Column(DateTime(timezone=True))
    dateLastEdited     = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            #if property == 'password':
            #    value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)
    
    def get_id(self):
        return str(self.id)


#@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


#@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None

'''
class OAuth(OAuthConsumerMixin, Base):
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete="cascade"), nullable=False)
    user = db.relationship(Users)
'''
