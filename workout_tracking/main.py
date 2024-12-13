import os
import requests
from datetime import datetime as dt
from dotenv import load_dotenv
load_dotenv()

SHEETY_TOKEN_AUTH=os.environ.get('SHEETY_TOKEN_AUTH')
APP_ID=os.environ.get('APP_ID')
APP_KEY=os.environ.get('APP_KEY')
HOST_DOMAIN="https://trackapi.nutritionix.com"

exercise_endpoint=f"{HOST_DOMAIN}/v2/natural/exercise"
headers={
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
}

parameters={
    'query':input("Tell me which exercise you did: "),
    'weight_kg':89,
    'height_cm':173,
    'age':36
}

response=requests.post(url=exercise_endpoint,json=parameters,headers=headers)
nutri_data=response.json()['exercises']


sheety_url="https://api.sheety.co/96fd27c8901e7407d06fb5078cdc3e3d/workoutTracking/workouts"

sheety_head={
    "Authorization":SHEETY_TOKEN_AUTH,

    }

for workout in nutri_data:
    date=dt.now().strftime("%d/%m/%Y")
    time=dt.now().strftime("%H:%M:%S")
    exercise=workout['name']
    duration=workout['duration_min']
    calories=workout['nf_calories']

    response=requests.get(url=sheety_url,headers=sheety_head)
    data=response.json()

    data_to_parse={
        'workout':{
            'date':date,
            'time':time,
            'exercise':exercise,
            'duration':f"{round(duration)} min",
            'calories':calories,
        }
    }

    response_2=requests.post(url=sheety_url,headers=sheety_head,json=data_to_parse)
    # print(response_2.text)








