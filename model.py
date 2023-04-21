from secrets import token_hex
import uuid
from sqlalchemy import Column, Enum, Float, Integer, String, Boolean, DateTime, ForeignKey
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class Role(Base):

    __tablename__="role"

    roleID =Column(Integer,primary_key=True,index=True, autoincrement=True)
    roleName=Column(String)
    roleDesc =Column(String)


class User(Base):

    __tablename__="user"

    userID=Column(Integer,primary_key=True,index=True, autoincrement=True)
    userName=Column(String,nullable=False)
    pincode=Column(Integer)
    userImage=Column(String)
    lastActive=Column(DateTime,nullable=False)
    role = Column(Integer,ForeignKey('role.roleID'))