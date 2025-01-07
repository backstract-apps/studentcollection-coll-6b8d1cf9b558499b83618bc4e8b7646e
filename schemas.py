from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Students(BaseModel):
    id: int
    name: str
    roll_number: str
    age: int
    username: str
    password: str
    emailid: str


class ReadStudents(BaseModel):
    id: int
    name: str
    roll_number: str
    age: int
    username: str
    password: str
    emailid: str
    class Config:
        from_attributes = True


