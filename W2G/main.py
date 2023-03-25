# Make a function to detect new songs
# Make a function to add only the new songs
# After scanning the playlist, the program should ask the user if they want to add the new founds songs

from wsgiref import util
import W2Gapi
import YoutubeApi
import Utilities
import Menus
import Video

import json
from collections import namedtuple
from json import JSONEncoder


api_key = "gcv2qy76i2qafc31xcyrlfdg7c9k5aj70b87wl4nl0cpvs5m59pdtrp7hj7ueld2"

# 0 - Main menu
# 1 - YtPlaylist selection
# 2 - W2G room   selection
screen = 0

videoList = []

def customDecoder(myClass):
    return namedtuple("X", myClass.keys())(*myClass.values())

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

while True:
    if screen == 0:
        screen = Menus.MainMenu()
    elif screen == 1:
        screen = Menus.YtPlaylistMenu()
    elif screen == -1:
        break