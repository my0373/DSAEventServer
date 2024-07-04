
import random
from fastapi import FastAPI
from typing import List
from random import randint
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json


app = FastAPI()

def get_random_first_name():
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Olivia']
    return random.choice(first_names)

def get_random_family_name():
    family_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis']
    return random.choice(family_names)

def get_random_age():
    return random.randint(4, 45)

def get_random_swimming_stroke():
    swimming_strokes = ['Freestyle', 'Backstroke', 'Breaststroke', 'Butterfly']
    return random.choice(swimming_strokes)

def get_random_time():
    return random.randint(30, 120)

def get_random_classifier():
    return random.randint(1, 14)

def get_random_swimmer():
    return {
        'first_name': get_random_first_name(),
        'family_name': get_random_family_name(),
        'age': get_random_age(),
        'swimming_stroke': get_random_swimming_stroke(),
        'time': get_random_time(),
        'classifier': get_random_classifier()
    }

@app.get("/swimmer")
def get_swimmer():
    swimmers = [get_random_swimmer() for i in range(1,200)]  
    swim_results = JSONResponse(content=jsonable_encoder(swimmers))
    return swim_results
    
 