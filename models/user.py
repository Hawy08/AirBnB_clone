#!/usr/bin/python3
from base_model import BaseModel

class User(BaseModel):
    def __init__(self):
        super().__init__()
        self.email = "" 
        self.password = "" 
        self.first_name = ""
        self.last_name = ""