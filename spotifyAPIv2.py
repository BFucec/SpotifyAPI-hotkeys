import spotipy
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, make_response

app = Flask(__name__)

def create_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id = "055f3f1bc8d247e9ba37beb0b7b0ff5f",
        client_secret = "7b444187bd5f4c5ab0dadcd9bd8b849f",
        redirect_uri="http://localhost:8080",
        scope="user-modify-playback-state user-read-playback-state",
    ))

spotify = create_spotify_client()

def play_pause():
    playback = spotify.current_playback()
    if playback and playback["is_playing"]:
        spotify.pause_playback()
        return "Playback paused"
    else:
        spotify.start_playback()
        return "Playback started"

def next_song():
    spotify.next_track()
    return "Playing next song"

def previous_song():
    spotify.previous_track()
    return "Playing previous song"

@app.route('/playback/play', methods=['POST'])
def control_playback_play():
    result = play_pause()    
    return result, 200

@app.route('/playback/next', methods=['POST'])
def control_playback_next():
    result = next_song()
    return result, 200

@app.route('/playback/previous', methods=['POST'])
def control_playback_previous():
    result = previous_song()
    return result, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
