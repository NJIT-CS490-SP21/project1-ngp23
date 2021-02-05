#imports all the needed packages to the environment 
import os,random,requests,json
from flask import Flask,render_template
from dotenv import load_dotenv, find_dotenv

# This file executues the script.
app=Flask(__name__)
# sets the cache control max age to this number of seconds.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#token function which gets the token.
def token():
    #URL for token API
    AUTH_URL= 'https://accounts.spotify.com/api/token'
    #Loading the .env file
    load_dotenv(find_dotenv())
    #Post request with client credentials to recieve respone and storre.
    auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('CLIENT_SECRET'),
    })
    #converts the respone in the JSON format.
    auth_response_data = auth_response.json()
    #gets the access token from JSON file.
    access_token = auth_response_data['access_token']
    #returns the access token
    return access_token
    
#python decorator to assigns URL in out app to function easily
@app.route('/')

def myApp():
    #Artists Spotify IDs
    artist=["4xRYI6VqpkE3UwrDrAZL8L",
    "6eUKZXaKkcviH0Ku9w2n3V",
    "66CXWjxzNUsdJxJ2JdwvnR",
    "1tqysapcCh1lWEAc9dIFpa",
    "2GoeZ0qOTt6kjsWW4eA6LS"]
    
    #generates random value between 0 to number of Artists
    rand = random.randint(0,len(artist)-1)
    #gets the token value from the token function.
    access_token=token()
    
    #BASE URL to get the top tracks of random artist we pick from the list.
    BASE_URL=	'https://api.spotify.com/v1/artists/'+artist[rand]+'/top-tracks?market=US'
    # We assign header to access the data from the spotify using API
    headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    #makes a get request  using the base url and header infromation
    data = requests.get(BASE_URL, headers=headers)
    #converts data to JSON file.
    data = data.json()
   
    #json_formatted_str = json.dumps(data, indent=2)
    #get the number of top tracks for the artist.
    length = len(data['tracks'])
    #generates an random number between 0 to total track-1 to pick the 1 random song from the top tracks
    randArtist= random.randint(0,length-1)
    
    #gets the name of the song
    name = data['tracks'][randArtist]['name']
    #ceating the list for the artistname.
    aName=[]
    #go through the artists and gets all the artists name
    for i in range(0,len(data['tracks'][randArtist]['album']['artists'])):
        aName.append(data['tracks'][randArtist]['album']['artists'][i]['name'])
    #gets the image url
    imageUrl = data['tracks'][randArtist]['album']['images'][0]['url']
    #gets preview url
    preview_url= data['tracks'][randArtist]['preview_url']
    
    #sends the data to the HTML file.
    return render_template(
        "index.html",
        dataName = name,
        artistName = aName,
        imageUrl = imageUrl,
        preview_url=preview_url
        )

 #runs the application with a serverwith the debugger and reload which occurs when
 #we make changes
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0'),
    use_reloader = True,
    debug = True, #Autorun
    )
