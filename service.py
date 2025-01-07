from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_students(db: Session, id: int):

    students_all = db.query(models.Students).order_by(models.Students.id).all()


    students_name: str = name


    

    students_name = name


    students_name1: str = students_name

    res = {
        'students_all': students_all,
    }
    return res

async def get_students_id(db: Session, id: int):

    students_one = db.query(models.Students).filter(models.Students.id == 'id').first()
    res = {
        'students_one': students_one,
    }
    return res

async def post_students(db: Session, id: int, name: str, roll_number: str, age: int, username: str, password: str, emailid: str):

    record_to_be_added = {'id': id, 'name': name, 'roll_number': roll_number, 'age': age, 'username': username, 'password': password, 'emailid': emailid}
    new_students = models.Students(**record_to_be_added)
    db.add(new_students)
    db.commit()
    db.refresh(new_students)
    students_inserted_record = new_students


    student_data: int = id


    

    codeblock_students1=id

    

    codeblock_students2 = 2

    

    codeblock_name= students_inserted_record.name


    students_inserted_record.age: str = age



    students_alldata = {}  # Creating new dict

    res = {
        'students_inserted_record': students_inserted_record,
        'students_id': student_data,
        'students_name': student_records,
        'Student_id': id,
    }
    return res

async def put_students_id(db: Session, raw_data: dict):
    id:int = raw_data.get('id')
    name:str = raw_data.get('name')
    roll_number:str = raw_data.get('roll_number')
    age:int = raw_data.get('age')
    username:str = raw_data.get('username')
    password:str = raw_data.get('password')
    emailid:str = raw_data.get('emailid')


    students_edited_record = db.query(models.Students).filter(models.Students.id == age).first()
    for key, value in {'id': id, 'name': name, 'roll_number': roll_number, 'age': age, 'username': username, 'password': password, 'emailid': emailid}.items():
          setattr(students_edited_record, key, value)
    db.commit()
    db.refresh(students_edited_record)
    students_edited_record = students_edited_record

    res = {
        'students_edited_record': students_edited_record,
    }
    return res

async def delete_students_id(db: Session, id: int):

    students_deleted = None
    record_to_delete = db.query(models.Students).filter(models.Students.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        students_deleted = record_to_delete
    res = {
        'students_deleted': students_deleted,
    }
    return res

