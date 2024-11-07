import json
import os

def create_profile():
    profile = "test"
    print(os.path.dirname(__file__), "testidk")
    print(f'\\password_data\\{profile}.json')
    try:
        open(f'./final-project/final-project2/password_data/{profile}.json', 'x')
    except:
        pass

create_profile()