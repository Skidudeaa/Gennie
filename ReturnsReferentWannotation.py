# api_config.py
'''
YOUR_ACCESS_TOKEN = 'aSlsYtH2i1gJvJSnUHeGzmEf93JrrsGJGPA4cNc78L0cFnSKvIhBKDMsDquTHE7q'
YOUR_SONG_ID = 3359190

import requests

song_id = 'YOUR_SONG_ID'  # replace with your song ID
url = "https://api.genius.com/referents"
headers = {
  'Authorization': 'Bearer YOUR_ACCESS_TOKEN'  # replace with your access token
}
querystring = {"YOUR_SONG_ID": song_id}

response = requests.request("GET", url, headers=headers, params=querystring)

# Parse the JSON response into a Python dictionary
data = response.json()

for referent in data['response']['referents']:
  print(referent['id'])
  '''
  
  
  # api_config.py

YOUR_ACCESS_TOKEN = 'aSlsYtH2i1gJvJSnUHeGzmEf93JrrsGJGPA4cNc78L0cFnSKvIhBKDMsDquTHE7q'
YOUR_SONG_ID = 3359190

import requests

song_id = YOUR_SONG_ID  # use the variable, not the string
url = "https://api.genius.com/referents"
headers = {
  'Authorization': 'Bearer ' + YOUR_ACCESS_TOKEN  # use the variable, not the string
}
querystring = {"song_id": song_id}  # the key should be "song_id"

response = requests.request("GET", url, headers=headers, params=querystring)

# Parse the JSON response into a Python dictionary
data = response.json()

#for referent in data['response']['referents']:
#  print(referent['id'])


'''for referent in data['response']['referents']:
    print("Lyrics: ", referent['fragment'])
    for annotation in referent['annotations']:
        print("Annotation: ", annotation['body']['plain'])
'''        
        
'''for referent in data['response']['referents']:
    print("Lyrics: ", referent['fragment'])
    for annotation in referent['annotations']:
        print("Annotation: ", annotation['body'])
        '''

for referent in data['response']['referents']:
    print("Lyrics: ", referent['fragment'])
    for annotation in referent['annotations']:
        annotation_text = annotation['body']['dom']['children'][0]['children'][0]
        print("Annotation: ", annotation_text)
