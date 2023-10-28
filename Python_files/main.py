from fitness_api_test import get_weight_data
from firestore_connection import fetch_users, get_user_health_data, add_data
from twitter_api_test import post_to_mastodon
import datetime

#Get weight data for me
""" a = get_weight_data()
print(a)
for x in a['weight']:
    print(x['value']) """

#final day update of weight
if(datetime.datetime.now().strftime("%H:%M")=="23:59"):
    a=get_today_weight_data("hyep", datetime.date.today().strftime('%Y-%m-%d'))
    if(a):
        update_data("Ian Samir Yep Manzano", "isym444", 5000, a, datetime.date.today().strftime('%Y-%m-%d'))
    else:
        add_data("Ian Samir Yep Manzano", "isym444", 5000, a, datetime.date.today().strftime('%Y-%m-%d'))


#At 11:59pm if weight is more than 70kg, post to mastodon and donate to charity
if(datetime.datetime.now().strftime("%H:%M")=="23:59" and print(get_today_weight_data("hyep", datetime.date.today().strftime('%Y-%m-%d')))>70):
    post_to_mastodon()
    #donate_to_charity()