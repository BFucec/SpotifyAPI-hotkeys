import spotipy
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth
from pynput import keyboard

def create_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id = "055f3f1bc8d247e9ba37beb0b7b0ff5f",
        client_secret = "7b444187bd5f4c5ab0dadcd9bd8b849f",
        redirect_uri="http://localhost:8080",
        scope="user-modify-playback-state user-read-playback-state",
    ))

spotify = create_spotify_client()
start_time = datetime.now()
#time_change = datetime.timedelta(minutes=59)

def play_pause():
    playback = spotify.current_playback()
    if playback and playback["is_playing"]:
        spotify.pause_playback()
    else:
        spotify.start_playback()

#play_pause()

'''pressed_keys = set()
play_pause_COMBO = {keyboard.Key.home, keyboard.Key.end, keyboard.Key.page_up}

def on_press(key):
    pressed_keys.add(key)
    if all(k in pressed_keys for k in play_pause_COMBO):
        play_pause()

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)'''


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

#if datetime.now() == start_time + time_change:
    #start_time = datetime.now()
