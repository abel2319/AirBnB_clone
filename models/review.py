#!/usr/bin/python3
'''Module for class review
'''
from models import BaseModel


class Review(BaseModel):
    '''class Review that inherits from BaseModel
    '''
    place_id = ""
    user_id = ""
    text = ""
