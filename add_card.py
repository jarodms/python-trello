# Add a card to the FIRST list on the Board defined by BOARD_ID, or List defined by LIST_ID

from myconfig import *
from trello import TrelloClient
from trello import ResourceUnavailable

from requests.exceptions import HTTPError
import sys
import os
import re


# To get an app key, go here:
# https://trello.com/app-key

trello = TrelloClient(
    api_key=APPKEY,
    api_secret=TOKEN
)

trello_label = input('Enter the Card Label: ')
trello_description = input('Description (optional): ')

if len(trello_label) == 0:
    print("ERROR: Please provide a Label to create the card")
    sys.exit(-1)
elif len(trello_description) == 0:
	trello_description = ""


try:
    my_board = trello.get_board(BOARD_ID)
    board_lists = my_board.all_lists()

    #print(board_lists)
    for boardList in board_lists:    
        boardList.fetch()
    #    print(boardList.name + ": " + boardList.id)

    theListID = LIST_ID
    if len(LIST_ID) == 0:
        theListID = board_lists[0].id

    trello.get_list(theListID).add_card(trello_label, trello_description)

except ResourceUnavailable as e:    
    print('ERROR: %s' % e._msg)
    sys.exit(-1)
