import requests

api_key = "ab644e1b1208139b5384e1a720cc6530"


def get_cities(api_key, limit):
    """
    cette function return cities data for x limit
    """
    url = f"https://api.aviationstack.com/v1/cities?access_key={api_key}&limit={limit}"
    response = requests.get(url)
    return response.json()


## Fuction recuperer le resultat de get_cities et les stocks qlq part (ex.fichier json / BDD Sql)

## Function avec paramettre ville, return les details d'une ville 

cities = get_cities(api_key, 100)
print(cities)