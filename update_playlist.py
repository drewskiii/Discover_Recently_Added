import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import json
import time
from datetime import date
from datetime import timedelta
'''
Note:
    - set env vars
    - set redirect_uri to be same as in app in settings (online)
'''
# playlist-read-collaborative
scope = 'playlist-modify-public playlist-modify-private playlist-read-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))



UPDATING_PLAYLIST_ID = "7GiHp1v1WFgqhQrkTh9L6M" # ones u may like 😊
DAYS_IN_WEEK = 7

def parse_date(track_date):
    if track_date:
        year = int(track_date[:4])
        mth = int(track_date[5:7])
        day = int(track_date[8:10])
        # print(year, mth, day)
        date_obj = date(year, mth, day)
        return date_obj
    else:
        return None


def get_my_playlists():
    all_playlists = sp.current_user_playlists(limit=50)
    my_playlists = []
    for playlist in all_playlists['items']:
        # print(playlist['name']+ " CREATED BY " + playlist['owner']['display_name'])
        if playlist['owner']['display_name'] == 'drewskiii' and not playlist['collaborative'] and playlist['id'] != UPDATING_PLAYLIST_ID:
            my_playlists.append(playlist['id'])
            # print(playlist['name'], playlist['uri'], playlist['collaborative'])
    return my_playlists



def get_songs(p_id):
    offset = 0
    tracks = sp.playlist_items(playlist_id=p_id,
                               fields="items.track.id, items.added_at, items.track.name",
                               offset=offset
                               )['items']
    # print(tracks[-1])
    if tracks:
        last_track = tracks[-1]
        days = timedelta(DAYS_IN_WEEK)
        #  parse_date(last_track['added_at'])
        last_week = date.today() - days
        print(last_week)
        if parse_date(last_track['added_at']) >= last_week and parse_date(last_track['added_at']) <= date.today():
            print("HI")
        print('hello')
        


def selected_songs(playlist_ids):
    song_ids = []
    offset = 0
    for p_id in playlist_ids:
        get_songs(p_id)
        
        
        # print(tracks)
        break

selected_songs(get_my_playlists())

'''
playlist_upload_cover_image(playlist_id, image_b64) => Replace the image used to represent a specific playlist
playlist_add_items(playlist_id, items, position=None) => 
        Parameters:
        playlist_id - the id of the playlist
        items - a list of track/episode URIs, URLs or IDs
        position - the position to add the tracks

playlist_change_details(playlist_id, name=None, public=None, collaborative=None, description=None)
playlist_remove_all_occurrences_of_items(playlist_id, items, snapshot_id=None)
playlist_replace_items(playlist_id, items)

'''

# https://developer.spotify.com/documentation/web-api/reference/playlists/get-playlists-tracks/

# offset = 0

#   fields="items.track.added_at.id,total"
# response = sp.playlist_items(playlist_id=updating_playlist_id,
#                              offset=offset,
#                              fields="items.track.id, items.added_at, items.track.name")

#Create a list of song ids to pass to function below
# sp.playlist_replace_items(playlist_id,["1TPgw76OuRx2VA390Kjari"])
# sp.playlist_add_items(playlist_id, ["1TPgw76OuRx2VA390Kjari"], position=None)

# with open('s', "w+") as f:
#     f.write(json.dumps(response, indent=4))