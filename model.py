from secrets import token_hex
import uuid
from sqlalchemy import Column, Enum, Float, Integer, String, Boolean, DateTime, ForeignKey
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship
import enum

class Priority(enum.Enum):
    HIGH="High"
    MEDIUM="Medium"
    LOW="Low"

class Status(enum.Enum):
    PENDING="Pending"
    INPROCESS="In Process"
    COMPLETED="Completed"


class Role(enum.Enum):
    USER="User"
    ACTIVIST="Activist"


class Users(Base):

    __tablename__="user"

    user_id=Column(Integer,primary_key=True,index=True, autoincrement=True)
    user_name=Column(String,nullable=False)
    pincode=Column(Integer)
    user_image=Column(String)
    last_active=Column(DateTime,nullable=False)
    role = Column(Enum(Role))

    activists=relationship('Activists', back_populates='users')


class Activists(Base):
    __tablename__="activist_profile"

    activist_id=Column(Integer,primary_key=True,index=True, autoincrement=True)
    user_id =Column(Integer, ForeignKey('user.user_id'))
    expertise_in =Column(String)

    users=relationship('Users', back_populates='activists')

class Issues(Base):

    __tablename__="issue"

    issue_id=Column(Integer,primary_key=True,index=True, autoincrement=True)
    priority=Column(Enum(Priority))
    title=Column(String)
    description=Column(String)
    status=Column(Enum(Status))
    assigned_to =Column(Integer, ForeignKey('user.user_id'))
