import requests

#Get weight data from Ian Samir Yep Manzano's google Fit API
def get_weight_data():
    url = "https://v1.nocodeapi.com/isym444/fit/PJbNKublYFhRoNGp/aggregatesDatasets?dataTypeName=weight"
    params = {}
    r = requests.get(url = url, params = params)
    return(r.json())
    #print(result)


