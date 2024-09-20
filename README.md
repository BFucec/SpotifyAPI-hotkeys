The main purpose of the project is to be able to specifically control Spotify volume, pause, play and execute other important functionalities since some of them cannot be used while Spotify is not in focus.

This project is meant to be used with additional macro keyboards, or keyboards with volume knobs.

The project consists of one python script which should be always running on the user's PC. This script connects to the Spotify API which allows users to control the volume, skip tracks, pause/play, ...
The python script is a lightweight local server that makes the calls to the Spotify API since it uses the spotipy library which can handle the authorization and keeping the connection active.

The project also consists of one AHK script which then binds the keyboards keys to executing specific functions on the Spotify API.

Some of the functionalities on the Spotify API are available only for premium users.
