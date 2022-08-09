import os
import requests


def get_astronomy_pic_of_day():
    r = requests.get(
        f'https://api.nasa.gov/planetary/apod?api_key={os.getenv("API_KEY")}')
    if (r.status_code == 200):
        return r.json()


def get_mars_pic(date_to_get):
    r = requests.get(
        f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date_to_get}&page-1&api_key={os.getenv("API_KEY")}')
    if (r.status_code == 200):
        return r.json()
