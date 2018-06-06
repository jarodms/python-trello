from myconfig import *
import requests

url = "https://api.trello.com/1/boards/" + BOARD_ID + "/lists"

querystring = {"key":APPKEY,"token":TOKEN}

response = requests.request("GET", url, params=querystring)

print(response.text)
