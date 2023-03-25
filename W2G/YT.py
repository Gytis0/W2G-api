import Utilities
import YoutubeApi
import Video
import youtube_dl

def GetAllVideosFromYT(ytPlaylist, fileName):
    i = 1
    pageToken = None
    videoList = []
    print("Getting 0-50 vidoes...")
    resp = YoutubeApi.Get50Videos(None, ytPlaylist)
    
    for video in resp["items"]:
        videoList.append(Video.YTVideo(video["snippet"]["title"], video["contentDetails"]["videoId"]))

    # If more than 50 videos exist in the playlist, nextPageToken will be given for the next 50 videos
    # Here I'm trying to replicate a do-while loop.
    if "nextPageToken" in resp:
        pageToken = resp["nextPageToken"]

        while pageToken:
            print("Getting " + str(50*i) + "-" + str(50*i+50) + " videos...")
            resp = YoutubeApi.Get50Videos(pageToken, ytPlaylist)
            
            for video in resp["items"]:
                videoList.append(Video.YTVideo(video["snippet"]["title"], video["contentDetails"]["videoId"]))

            if "nextPageToken" in resp:
                pageToken = resp["nextPageToken"]
            else:
                break
            i = i + 1

    Utilities.WriteYT(videoList, fileName)
    
    Utilities.WritePageCount(i)

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
def DownloadVids(address):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([address])