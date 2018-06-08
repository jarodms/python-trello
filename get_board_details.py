from myconfig import *
import requests
import json


url = "https://api.trello.com/1/boards/" + BOARD_ID + "/lists"

querystring = {"key":APPKEY,"token":TOKEN}

response = requests.request("GET", url, params=querystring)
json_dict = json.loads(response.text)


for boardList in json_dict:    
    print(boardList['name'] + ": " + boardList['id'])
