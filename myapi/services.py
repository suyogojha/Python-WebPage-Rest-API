from django.contrib.sites import requests


def get_posts(title, content):
    url = 'http://127.0.0.1:8000/posts/'
    params = {'title': title, 'content': content}
    r = requests.get(url, params=params)
    posts = str(r)
    post_list = {'posts': posts['results']}
    return post_list
