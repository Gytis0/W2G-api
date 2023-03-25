from typing import List
import urllib3
import json
import Video

def CreateRoom(api_key):
    URL = 'https://api.w2g.tv/rooms/create.json'

    HEADERS = {'Accept': 'application/json',
                        'Content-Type': 'application/json'}

    PARAMS = {"w2g_api_key": api_key}
    encoded_data = json.dumps(PARAMS).encode('utf-8')

    http = urllib3.PoolManager()
    resp = http.request("POST", URL, headers = HEADERS, body = encoded_data)

    return resp

def PlayVideo(api_key, room_key, video_url):
    URL = 'https://api.w2g.tv/rooms/' + room_key +'/sync_update'

    HEADERS = {'Accept': 'application/json',
                        'Content-Type': 'application/json'}

    PARAMS = {"w2g_api_key": api_key,
              "item_url": video_url}
    encoded_data = json.dumps(PARAMS).encode('utf-8')

    http = urllib3.PoolManager()
    resp = http.request("POST", URL, headers=HEADERS, body=encoded_data)

    return resp

def AddVideos(api_key, room_key, videos):
    videoPlaylist = []
    
    for x in videos:
        videoPlaylist.append({"url" : x.link, "title" : x.name, "thumb" : x.thumb})

    video_playlists = [{"url":"https://www.youtube.com/watch?v=m9EX0f6V11Y","thumb":"https://i.ytimg.com/vi/m9EX0f6V11Y/mqdefault.jpg"},
                   {"url":"https://www.youtube.com/watch?v=m9EX0f6V11Y","thumb":"https://i.ytimg.com/vi/m9EX0f6V11Y/mqdefault.jpg"},
                   {"url":"https://www.youtube.com/watch?v=m9EX0f6V11Y","thumb":"https://i.ytimg.com/vi/m9EX0f6V11Y/mqdefault.jpg"},
                   {"url":"https://www.youtube.com/watch?v=m9EX0f6V11Y","thumb":"https://i.ytimg.com/vi/m9EX0f6V11Y/mqdefault.jpg"},
                   {"url":"https://www.youtube.com/watch?v=m9EX0f6V11Y","thumb":"https://i.ytimg.com/vi/m9EX0f6V11Y/mqdefault.jpg"}
                    ]

    URL = 'https://api.w2g.tv/rooms/' + room_key +'/playlists/current/playlist_items/sync_update'
    
    HEADERS = {'Accept': 'application/json',
                        'Content-Type': 'application/json'}

    PARAMS = {"w2g_api_key": api_key,
              "add_items": videoPlaylist}
    encoded_data = json.dumps(PARAMS).encode('utf-8')

    http = urllib3.PoolManager()
    resp = http.request("POST", URL, headers = HEADERS, body = encoded_data)

    return resp

def GetVideos(api_key, room_key):
    URL = 'https://api.w2g.tv/rooms/' + room_key
    
    HEADERS = {'Accept': 'application/json',
                        'Content-Type': 'application/json'}

    PARAMS = {"w2g_api_key": api_key}
    encoded_data = json.dumps(PARAMS).encode('utf-8')

    http = urllib3.PoolManager()
    resp = http.request("GET", URL, headers = HEADERS, body = encoded_data)

    return resp