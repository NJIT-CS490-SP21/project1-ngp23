import os,random,requests,json
from flask import Flask,render_template
from dotenv import load_dotenv, find_dotenv

app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
def homepage():

    artist=["4xRYI6VqpkE3UwrDrAZL8L",
    "6eUKZXaKkcviH0Ku9w2n3V",
    "66CXWjxzNUsdJxJ2JdwvnR",
    "1tqysapcCh1lWEAc9dIFpa",
    "2GoeZ0qOTt6kjsWW4eA6LS"]
    
    rand = random.randint(0,len(artist)-1)
    
    AUTH_URL= 'https://accounts.spotify.com/api/token'
    load_dotenv(find_dotenv())
    auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('CLIENT_SECRET'),
    })

    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    BASE_URL=	'https://api.spotify.com/v1/artists/'+artist[rand]+'/top-tracks?market=US'
    headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    data = requests.get(BASE_URL , headers=headers)
    data = data.json()
    json_formatted_str = json.dumps(data, indent=2)
    
    length = len(data['tracks'])
    randArtist= random.randint(0,length-1)
    name = data['tracks'][randArtist]['name']
    aName=[]
    for i in range(0,len(data['tracks'][randArtist]['album']['artists'])):
        aName.append(data['tracks'][randArtist]['album']['artists'][i]['name'])
         
    imageUrl = data['tracks'][randArtist]['album']['images'][0]['url']
    
    preview_url= data['tracks'][randArtist]['preview_url']
    
    return render_template(
        "index.html",
        dataName = name,
        artistName = aName,
        imageUrl = imageUrl,
        preview_url=preview_url
        )
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0'),
    use_reloader = True,
    debug = True, #Autorun
    )
