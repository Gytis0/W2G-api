# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import Utilities

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
youtube = None

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

def Setup():

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_798151242560-6kph2b3cqibn4oo86kaj0rajqhr0shjl.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()

    #Utilities.OpenLink(flow.authorization_url()[0])
    global youtube
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

def Get50Videos(_pageToken, youtubePlaylist):

    if _pageToken != None:
        request = youtube.playlistItems().list(
            part="contentDetails,snippet",
            playlistId = youtubePlaylist,
            maxResults = 50,
            pageToken = _pageToken
        )
    else:
        request = youtube.playlistItems().list(
            part="contentDetails,snippet",
            playlistId = youtubePlaylist,
            maxResults = 50
        )

    response = request.execute()

    return response