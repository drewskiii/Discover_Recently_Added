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

SCOPE = 'playlist-modify-public playlist-modify-private playlist-read-private'
UPDATING_PLAYLIST_ID = "enter_playlist_id_here"
DAYS_IN_WEEK = 7


class DiscoverRecentlyAdded:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))
        self.song_collection = {}
    
    def parse_date(self, track_date):
        if track_date:
            year = int(track_date[:4])
            mth = int(track_date[5:7])
            day = int(track_date[8:10])
            date_obj = date(year, mth, day)
            return date_obj
        else:
            return None

    def get_my_playlists(self):
        all_playlists = self.sp.current_user_playlists(limit=50)
        my_playlists = []
        for playlist in all_playlists['items']:
            if playlist['owner']['display_name'] == 'drewskiii' and not playlist['collaborative'] and playlist['id'] != UPDATING_PLAYLIST_ID:
                my_playlists.append(playlist['id'])
                

        return my_playlists

    def get_all_tracks(self, p_id):
        offset = 0
        all_playlist_tracks = []
        tracks = self.sp.playlist_items(playlist_id=p_id,
                                fields="items.track.id, items.added_at, items.track.name",
                                offset=offset
                                )['items']  # limit default 100
        while tracks:
            all_playlist_tracks += tracks
            offset += len(tracks)
            tracks = self.sp.playlist_items(playlist_id=p_id,
                                fields="items.track.id, items.added_at, items.track.name",
                                offset=offset
                                )['items']  # limit default 100

        all_playlist_tracks = sorted(all_playlist_tracks, key=lambda x: x['added_at'], reverse=True)
        return all_playlist_tracks

    def get_last_week_added_songs(self, p_id):
        all_playlist_tracks = self.get_all_tracks(p_id)
        last_week = date.today() - timedelta(DAYS_IN_WEEK)
        

        for track in all_playlist_tracks:
            if self.parse_date(track['added_at']) >= last_week and self.song_collection.get(track['track']['id']) is None:
                self.song_collection[track['track']['id']] = True
            else: # the rest will be from more than a week ago
                break
        

    
    def update_playlist(self):
        playlist_ids = self.get_my_playlists()
        offset = 0
        for p_id in playlist_ids:
            self.get_last_week_added_songs(p_id)
            
        self.sp.playlist_replace_items(UPDATING_PLAYLIST_ID, list(self.song_collection.keys()))


def main():
    try:
        recent_added_obj = DiscoverRecentlyAdded()
        recent_added_obj.update_playlist()
    except:
        print("There was a problem")
        raise

if __name__ == "__main__": 
    main()