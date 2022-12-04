
## 1. SET UP

# Import modules
import spotipy
import os

# Spotify Authentication
from spotipy.oauth2 import SpotifyClientCredentials
os.environ['SPOTIPY_CLIENT_ID'] = '13039085c25042118376c79a2b0640ff'
os.environ['SPOTIPY_CLIENT_SECRET'] = '0f580e442b2c4d1bb3177c8578eb74b4'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://localhost:8888/callback'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

## 2. SEARCH EXERCISE

print('Welcome to the Spotify Search tool')

# User input
type = input('What do you want to search for? (track, artist, album) - ')
query = input('Input search parameters: name, year and genre - ')
number = input('How many search results do you want to see? - ')

#  Search and print results
results = sp.search(q=query, limit=number, type=type)
if type=='track':
    for result in results['tracks']['items']:
        print(result['name'])
elif type=='artist':
    for result2 in results['artists']['items']:
        print(result2['name'])
else:
    for result3 in results['albums']['items']:
        print(result3['name'])
