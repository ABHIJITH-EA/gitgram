import apis
import json

from utils import avatar_download, get_path

if __name__ == '__main__':
    
    user = apis.API('Ea37')

    with open(get_path(), 'r') as f:
        user_details = json.load(f)

    # avatar_download(user_details['avatar_url'])

    followers = user.get_followers(user_details['followers_url'])
    followings = user.get_followings(user_details['following_url'])

    for follower in followers:
        print(follower['login'])

    for follow in followings:
        print(follow['html_url'])