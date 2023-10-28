from google.cloud import firestore
import os
import json
import copy
import random
import string
import datetime

# Set GOOGLE_APPLICATION_CREDENTIALS as an environment variable or use it directly in code
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".vscode/gutsdb-6a7a2-firebase-adminsdk-992kj-f3c2ac8f57.json"

# Initialize Firestore client
db = firestore.Client()

list_of_users = []

def random_string(length=10):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# Fetch data from Firestore
def fetch_users():
    users_ref = db.collection('Users')
    docs = list(users_ref.stream())
    #print(docs)

    user_ids = [user_id.id for user_id in docs]
    #print(user_ids)
    # Convert to list of dictionaries
    data_list = [doc.to_dict() for doc in docs]
    #print(data_list)
    # Convert to JSON (optional)
    data_json = json.dumps(data_list)
    #print(data_json)
    return user_ids



def get_user_health_data(user_id):
    # Reference to a specific user document
    user_ref2 = db.collection('Users').document(user_id)

    # Reference to the orders subcollection of the user
    health_data_ref = user_ref2.collection('Health_Data')
    health_data = health_data_ref.stream()
    #print(health_data)
    health_data_list = [x.to_dict() for x in health_data]
    #print(health_data_list)
    return(health_data_list)

def get_today_weight_data(user_id, date):
    # Reference to a specific user document
    user_ref2 = db.collection('Users').document(user_id)

    # Reference to the orders subcollection of the user
    health_data_ref = user_ref2.collection('Health_Data')
    health_data = health_data_ref.stream()
    #print(health_data)
    health_data_list = [x.to_dict() for x in health_data]
    for y in health_data_list:
        #print(y["Date"])
        #print(y["Weight"])
        if(y["Date"]==date):
            #print("yay")
            return(y["Weight"])

#get_weight_data("hyep", datetime.date.today().strftime('%d-%m-%Y'))

def add_data(name, username, steps, weight, date):
    temp_health_id = date
    doc_ref = db.collection('Users').document(username)
    doc_ref.set({
        'Name': name,
        'Username': username
    })
    doc_ref2 = db.collection('Users').document(username).collection('Health_Data').document(temp_health_id)
    print(type(datetime.date.today().strftime('%Y-%m-%d')))
    doc_ref2.set({
        'Date': datetime.date.today().strftime('%Y-%m-%d'),
        'Steps': steps,
        'Weight': weight
    })

def add_user(new_name, new_username, new_steps, new_weight):
    switch= False
    for x in fetch_users():
        if(x==new_username):
            switch=True
    if(switch==False):
        add_data(new_name,new_username, new_steps, new_weight, datetime.date.today().strftime('%Y-%m-%d'))

def add_hardcoded_data(name, username, steps, weight):
    temp_user_id = "7kNM25MjTDKw26wJMNyu"
    temp_health_id = random_string(10)
    doc_ref = db.collection('Users').document(temp_user_id)
    doc_ref.set({
        'Name': "Ian Samir Yep Manzano",
        'Username': "isym444"
    })
    doc_ref2 = db.collection('Users').document(temp_user_id).collection('Health_Data').document(temp_health_id)
    print(type(datetime.date.today().strftime('%Y-%m-%d')))
    doc_ref2.set({
        'Date': datetime.date.today().strftime('%Y-%m-%d'),
        'Steps': steps,
        'Weight': weight
    })

def update_data(name, username, steps, weight, date):
    temp_user_id = username
    doc_ref2 = db.collection('Users').document(temp_user_id).collection('Health_Data').document(date)
    doc_ref2.update({
        'Date': datetime.date.today().strftime('%Y-%m-%d'),
        'Steps': steps,
        'Weight': weight
    })
#add_data("Hector Yep", "hyep", 3000, 80)

# Call the functions
""" try:
    list_of_users = fetch_users()
    for user in list_of_users:
        get_user_health_data(user)
    add_data("test3","test_username3", 4000, 74)

except:
    print("Error") """

