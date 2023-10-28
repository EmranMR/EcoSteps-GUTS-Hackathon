import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()
def post_to_mastodon():
    list_of_embarassing_posts = ["I like pumpkins", "Happy Howl-oween!", "Love at first bite", "Want to hear some skeleton puns? They’re very humerus!", "Witch-ing you a Happy Halloween!", "I have a few vampire puns, but they suck.","Ghosts make the best cheerleaders. They have lots of spirit!"]
    pick_a_post = random.randint(0, len(list_of_embarassing_posts) - 1)
    url = 'https://mastodon.social/api/v1/statuses'
    auth = {'Authorization': os.getenv("MASTODONKEY")}
    params = {'status': f'{pick_a_post}'}
    response = requests.post(url, data=params, headers=auth)
    print(response.json())
""" post_to_mastodon(list_of_embarassing_posts[pick_a_post]) """

post_to_mastodon()