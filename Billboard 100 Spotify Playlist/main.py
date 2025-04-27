from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import pprint

scope = "playlist-modify-private"

sp = SpotifyOAuth(client_id="", client_secret="",
                  redirect_uri="http://example.com", scope=scope, username="")

Spotify_Api = Spotify(auth_manager=sp)

username = Spotify_Api.current_user()["id"]


user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

url = "https://www.billboard.com/charts/hot-100/" + user_input

response = requests.get(url=url, headers=header)
raw_html = response.text

soup = BeautifulSoup(raw_html, "html.parser")

song_names_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_spans]

year = user_input.split("-")[0]

print(song_names[0])

spotify_list = []

for song in song_names:
    try:
        spotify_url = Spotify_Api.search(q=f"track:{song} year:{year}")["tracks"]["items"][0]["uri"]
        spotify_list.append(spotify_url)
    except IndexError:
        print(f"{song} not found")

playlist_id = Spotify_Api.user_playlist_create(user="",name=f"{user_input} Billboard 100", public=False)


Spotify_Api.user_playlist_add_tracks(user="", playlist_id=playlist_id["uri"], tracks=spotify_list)

# print(song_names)