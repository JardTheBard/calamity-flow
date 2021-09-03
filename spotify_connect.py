import spotipy
#import json
from spotipy.oauth2 import SpotifyOAuth

class Connect:
    def __init__(self, request):
        self.request = request
        self.scope = ["user-library-read", "user-read-playback-state"]
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))
    
    def display_user_info(self):
        return self.sp.current_user()