import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Initialize the spotipy client with your credentials
client_id = "1d769f1a37ef41fd87b485116c646c13"
client_secret = "c31b2e31573b494b8f47da691a9b7deb"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri='http://google.com/callback/',
                                               scope='user-library-read user-modify-playback-state'))


# Function to search for a song on Spotify and play it
def play_song(song_name):
    results = sp.search(q=song_name, type='track', limit=1)

    if results and results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        sp.start_playback(uris=[track_uri])
        print(f"Playing: {results['tracks']['items'][0]['name']}")
    else:
        print(f"Song '{song_name}' not found on Spotify.")


# Get the user input for the song name
while True:
    song_name = input("Enter the name of the song you want to play on Spotify (or 'quit' to exit): ").strip()

    if song_name.lower() == 'quit':
        break

    play_song(song_name)