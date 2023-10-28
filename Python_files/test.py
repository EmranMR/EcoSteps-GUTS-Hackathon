import datetime
from firestore_connection import *
from fitness_api_test import *
#print(datetime.date.today().strftime('%d-%m-%Y'))

print(get_weight_data())