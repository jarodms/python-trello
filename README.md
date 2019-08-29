
### 08/29/2019: Tested with Python 3.6.6


# Get Started
pip install py-trello


* If you have problems with this command, you may want to use the latest source from: 
https://github.com/sarumont/py-trello/tree/master/trello*



# Trello API Setup

* Go to: https://trello.com/1/appKey/generate
  * Get your APPKEY
  * Get your TOKEN
* Find your Board ID (it's in the URL when you are viewing the Board)
* Rename `myconfig.py.sample` to `myconfig.py`
* Place thes APPKEY, TOKEN, and BOARD_ID in `myconfig.py`


# Example scripts
1. `python get_board_details.py`
    * This will get the List names and the list ID's in your Board
      * To Do: 5a-blah-blah-blah-3
      * Doing: 5a-blah-blah-blah-4
      * Done: 5a-blah-blah-blah-5
      * Rejected: 5a-blah-blah-blah-6
    * Use a specific ListID from the output if you want to always add your new cards to a specific list: copy the list id into __myconfig.py__ to setting __LIST_ID__
2. `python add_card.py`
    * Prompts you for `Card Label` and a `Description`
    * A new card is added to the first list in your Board, or if __LIST_ID__ is specified in __myconfig.py__, then the new card is added to that list



# More 
Look here to figure out API
https://github.com/sarumont/py-trello/tree/master/trello

