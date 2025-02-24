import requests 
import json 

api_key = "a96c171390f89ff8a8b893e7844f4a4c"


def get_departure(iataCode,api_key, type="departure"):

    url = f"https://api.aviationstack.com/v1/timetable?iataCode={iataCode}&type={type}&access_key={api_key}"
    r = requests.get(url)
    return r.json()


def get_arrival(iataCode,api_key, type="arrival"):

    url = f"https://api.aviationstack.com/v1/timetable?iataCode={iataCode}&type={type}&access_key={api_key}"
    r = requests.get(url)
    return r.json()


# Apres avoir définit les functions, il faut donc les appeler
departs = get_departure("ORY",api_key)
#print(departs)

arrives = get_arrival("CAJ", api_key)
print(arrives)