import os
import YT
import YoutubeApi
import W2G
import json

dash = "\n------------------\n"
infoMessage = ""
infoBox = False

menuId = 0
ytPlaylistId = 1

# Make a pair instead of two variables here (name, address)
selectedYtPlaylist = ""
selectedYtPlaylistName = ""
selectedW2Groom = ""

def MainMenu():
    os.system('cls')
    global infoBox, infoMessage, selectedYtPlaylist, selectedYtPlaylistName
    mainMenuText = "SELECTED YOUTUBE PLAYLIST: {}\nSELECTED W2G ROOM: {}{}Choose an action: \nL: Login. \n1: Get all videos from YT playlist. \n2: Add all videos to W2G. \n3: Open youtube playlist selection. \n0: Exit.\n".format(selectedYtPlaylistName, selectedW2Groom, dash)
    
    if infoBox:
        print(infoMessage + "\n------------------\n")
        infoBox = False

    actionKey = input(mainMenuText)

    if actionKey == "1":
        YT.GetAllVideosFromYT(selectedYtPlaylist, "my music.json")
        return menuId
    elif actionKey == "2":
        os.system('cls')
        decision = input("Are you sure? Y/N: ")
        if decision == "Y":
            W2G.AddAllVideosToW2G
        else:
            return menuId
        input("Press enter to continue...")
        return menuId
    elif actionKey == "3":
        return ytPlaylistId
    elif actionKey == "4":
        YT.DownloadVids("https://www.youtube.com/watch?v=ETEg-SB01QY")
        return menuId
    elif actionKey == "l":
        YoutubeApi.Setup()
        return menuId
    elif actionKey == "0":
        return -1
    else:
        infoMessage = "Wrong input!"
        infoBox = True

def YtPlaylistMenu():
    os.system('cls')
    i = 1
    global infoBox, infoMessage, selectedYtPlaylist, selectedYtPlaylistName
    ytMenuText = "Choose an action: \n0: Back. \nAny number: Select the preffered playlist.\n"

    if infoBox:
        print(infoMessage + "\n------------------\n")
        infoBox = False

    print(ytMenuText)
    f = open("ytPlaylists.json")
    data = json.load(f)
    for obj in data:
        print("{}. {}".format(i, obj["name"]))
        i = i + 1

    actionKey = input()
    

    if actionKey == "0":
        return menuId
    elif int(actionKey) > len(data):
        infoMessage = "Wrong input!"
        infoBox = True
        return ytPlaylistId
    else:
        selectedYtPlaylist = data[int(actionKey)-1]["address"]
        selectedYtPlaylistName = data[int(actionKey)-1]["name"]
        infoMessage = "You selected " + selectedYtPlaylistName
        infoBox = True
        return ytPlaylistId