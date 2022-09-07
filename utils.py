import os
import requests


def get_path(dir="data", name="result", format="json"):

    return os.path.abspath(os.path.join(os.path.dirname(__file__), dir, name+'.'+format))

def avatar_download(url):
    res = requests.get(url)
   
    img = get_path(name="avatar", format="png")

    with open(img, 'wb') as f:
        f.write(res.content)

def get_resource(name, dir="data"):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), dir, name))