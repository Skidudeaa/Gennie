# api_config.py
#GENIUS_API_TOKEN = 'aSlsYtH2i1gJvJSnUHeGzmEf93JrrsGJGPA4cNc78L0cFnSKvIhBKDMsDquTHE7q'


import requests

# Set the API endpoint and access token
base_url = 'https://api.genius.com'
access_token = 'aSlsYtH2i1gJvJSnUHeGzmEf93JrrsGJGPA4cNc78L0cFnSKvIhBKDMsDquTHE7q'

# Set the song title and artist
song_title = 'Lucid Dreams'
artist_name = 'Juice WRLD'

# Search for the song
search_url = f'{base_url}/search?q={song_title} {artist_name}'
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(search_url, headers=headers)
data = response.json()

# Retrieve the song ID from the search results
song_id = data['response']['hits'][0]['result']['id']

# Get the lyrics and annotations for the song
song_url = f'{base_url}/songs/{song_id}'
response = requests.get(song_url, headers=headers)
data = response.json()

# Extract the lyrics and annotations
lyrics = data['response']['song']['lyrics']['dom']['children'][0]['children'][0]['children']
annotations = data['response']['song']['description']['dom']['children'][0]['children']

# Print the lyrics and annotations
print("Lyrics:")
for line in lyrics:
    if line['tag'] == 'br':
        print()
    else:
        print(line['children'][0])

print("\nAnnotations:")
for annotation in annotations:
    print(annotation['children'][0])
