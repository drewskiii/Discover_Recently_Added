# Discover Recently Added
> Updates playlist for followers to view user's recently added tracks from the past week

This application compiles tracks the user added to their playlists from the past week and 
replaces the tracks from the selected playlist with the compiled tracks
for followers to listen in to what the user has newly added to their playlists. This is 
a fun way to connect with your followers and to seek songs they've interacted with, recently discovered, and even find new gems they found!

![](header.png)

## Installation & Usage Example
1) Clone this repo and cd into it:
```
    git clone https://github.com/drewskiii/Discover_Recently_Added.git
    cd Discover_Recently_Added
```
2) Create a virtual environment:
```
    python3 -m venv venv
```
3) Start your virtual environment:
```
    source venv/bin/activate
```
4) Follow the steps in [Spotipy Library quickstart][spotipy] to set up .env file for env vars.
5) OPTIONAL: Add to your virtual env activate script to automatically export env vars when starting up virtual environment. [Reference this to do it][reference]
6) pip install dependencies:
```
    pip install -r requirements.txt
```
7) Change UPDATING_PLAYLIST_ID in python script to match the target playlist id/URI you desire to update
8) Finally run the bash script! 
```
    ./run.sh
```
9) Deactivate virtual environment:
```
    deactivate
```
_Note, for first time run, spotify browser will pop up asking for permission to make changes to your account_


## Release History


## Meta

Created by Andrew Lor

[Buy me a coffee][coffee]

Lorandrewed@gmail.com

[drewskiii](https://github.com/drewskiii/)


<!-- Markdown link & img dfn's -->
[spotipy]: https://github.com/drewskiii/Discover_Recently_Added.git
[reference]: https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/
[coffee]: https://www.buymeacoffee.com/andrewlor
