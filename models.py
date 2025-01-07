from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    roll_number = Column(String, primary_key=False)
    age = Column(Integer, primary_key=False)
    username = Column(String, primary_key=False)
    password = Column(String, primary_key=False)
    emailid = Column(String, primary_key=False)

