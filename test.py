#! /usr/bin/env python

# https://pypi.python.org/pypi/trello
# See also https://pythonhosted.org/trello/trello.html
from myconfig import *
from urllib.parse import quote
from trello import TrelloApi

from requests.exceptions import HTTPError
import sys
import os
import re


# To get an app key, go here:
# https://trello.com/app-key

trello = TrelloApi(APPKEY)

trello.set_token(TOKEN)

trello_label = input('Enter the Card Label: ')
trello_description = input('Description (optional): ')

if len(trello_label) == 0:
    print("ERROR: Please provide a Label to create the card")
    sys.exit(-1)
elif len(trello_description) == 0:
	trello_description = ""


try:
    #cards = trello.boards.get_card(BOARD_ID)

    #lists = trello.boards.get_list(BOARD_ID)
    trello.lists.new_card(LIST_ID,trello_label, trello_description)

except HTTPError as e:
    message = 'Unknown HTTPError'
    if e.message.startswith('400'):
        message = 'Undefined HTTPError (bad board id?)'
    if e.message.startswith('401'):
        message = 'Unauthorized (bad token or app key?)'

    print('ERROR: %s' % message)
    sys.exit(-1)
