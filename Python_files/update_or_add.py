import datetime
from firestore_connection import *

a = {'weight': [{'value': 73, 'startTimeMillis': '1698139553420', 'endTimeMillis': '1698225953420', 'startTime': '28 Oct 2023 09:25 am', 'endTime': '25 Oct 2023 09:25 am'}, {'value': 71, 'startTimeMillis': '1698398753420', 'endTimeMillis': '1698451201000', 'startTime': '27 Oct 2023 09:25 am', 'endTime': '28 Oct 2023 12:00 am'}]}
#print(a)

def word_to_number(y):
    if y=="Jan":
        return "01"
    elif y=="Feb":
        return "02"
    elif y=="Mar":
        return "03"
    elif y=="Apr":
        return "04"
    elif y=="May":
        return "05"
    elif y=="Jun":
        return "06"
    elif y=="Jul":
        return "07"
    elif y=="Aug":
        return "08"
    elif y=="Sep":
        return "09"
    elif y=="Oct":
        return "10"
    elif y=="Nov":
        return "11"
    elif y=="Dec":
        return "12"

def change_date_format(x):
    x=x[0:11]
    x=x.split(" ")
    x[1]=word_to_number(x[1])
    b=x[0]+"-"+x[1]+"-"+x[2]
    #print(b)
    return(b)

change_date_format("24 Oct 2023 09:25 am")

#Whether or not the user has data for today
def exists(username):
    for x in get_user_health_data(username):
        #print(x["Date"])
        if(x["Date"]==datetime.date.today().strftime('%Y-%m-%d')):
            print("true")
            return True
    #print(f"testing: {get_user_health_data(username)}")
    return False

def add_or_update_user_data_for_today(name, username, date):
    #If exists, update steps/weight
    if(exists(username)==False):
        for x in a['weight']:
            print(datetime.date.today().strftime('%d-%m-%Y'))
            print(change_date_format(x['startTime']))
            if(datetime.date.today().strftime('%d-%m-%Y')==change_date_format(x['startTime'])):
                print(f"test: {x['value']}")
                update_data(name, username, 5000, x['value'], date)
            #print(change_date_format(x['startTime']))
            #print(x['value'])
    #If doesn't exist, add a new entry
    else:
        for x in a['weight']:
            print(datetime.date.today().strftime('%d-%m-%Y'))
            print(change_date_format(x['startTime']))
            if(datetime.date.today().strftime('%d-%m-%Y')==change_date_format(x['startTime'])):
                print(f"test: {x['value']}")
                add_data(name, username, 5000, x['value'], date)
        #modify steps of existing date
        print("test2")