import W2Gapi

def AddAllVideosToW2G():
    pages = Utilities.ReadPageCount()
    for i in range(0, pages):
        videoList = Read50VideosFromJSON(i)
        resp = W2Gapi.AddVideos(api_key, pussiesRoom, videoList)
        if resp.status == 200:
            print("Added " + str(50*i) + "-" + str(50*i+50) + " videos.")
        else:
            print("Couldn't add " + str(50*i) + "-" + str(50*i+50) + " videos.")