import requests
import json
import pprint

# replace 'your_api_key' with your actual Genius API key
headers = {'Authorization': 'Bearer aSlsYtH2i1gJvJSnUHeGzmEf93JrrsGJGPA4cNc78L0cFnSKvIhBKDMsDquTHE7q'}

# replace 'song_id' with the ID of the song you want to retrieve lyrics and annotations for
response = requests.get('https://api.genius.com/songs/3359190', headers=headers)

song_data = json.loads(response.text)

#print(song_data)

#data = json.loads(song_data)

#pprint.pprint(song_data)

artist_name = song_data['response']['song']['album']['artist']['name']
print(artist_name)

print(song_data.keys())

#print(song_data['response'])
#print(song_data['response']['song'])
#print(song_data['response']['song']['album'])


#with open('song_data.json', 'w') as f:
#    json.dump(song_data, f, indent=4)
    
#    import json

#print(json.dumps(song_data, indent=4))
