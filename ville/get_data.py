import requests
import json


api_key = "a96c171390f89ff8a8b893e7844f4a4c"


def get_cities(api_key, limit):

    ## cette fonction return cities data for x cities
    
    url = f"https://api.aviationstack.com/v1/cities?access_key={api_key}&limit={limit}"
    response = requests.get(url)
    return response.json()


def get_airports(api_key, limit):
     # Cette function return les airports

     url = f"https://api.aviationstack.com/v1/airports?access_key={api_key}&limit={limit}"
     r = requests.get(url)
     return r.json()

# Call functions
airports = get_airports(api_key, 10000)
cities = get_cities(api_key, 9400)


## Funtion recuperer le resultat de get_cities et les stock qlq part (ex.fichier json / BDD SQL)
with open("airoports_data.json", "w") as json_file:
    json.dump(airports, json_file, indent=4)

## Function avec paramettre cille, return les details dúne cille 
   
print("Well Done! Le document a été sauvegardé")