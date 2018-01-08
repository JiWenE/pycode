import requests


def get_city():
    url = 'http://www.pm25.in/api/querys.json&token=5j1znBVAsnSf5xQyNQyq'
    json = requests.get(url).text
    print(json)


get_city()