import spotipy

import spotipy
import spotipy.util as util

username = "gooday2die"
scope = "playlist-modify-private"

spotipy.util.prompt_for_user_token(username,scope,client_id='c853818d3ca945299bb9e6f73317ac75',client_secret='3dd7c1c628ed40e4bb3a5045755b78de',redirect_uri='https://developer.spotify.com/dashboard/applications/c853818d3ca945299bb9e6f73317ac75')
