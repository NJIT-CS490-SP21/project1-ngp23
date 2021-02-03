import os,random
from flask import Flask,render_template

app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
def homepage():
   
    artist={'Arijit Singh':"https://open.spotify.com/artist/4YRxDV8wJFPHPTeXepOstw",
        'Ed Sheeran':"https://open.spotify.com/artist/6eUKZXaKkcviH0Ku9w2n3V",
        'Ariana Grande':"https://open.spotify.com/artist/66CXWjxzNUsdJxJ2JdwvnR",
        'Jubin Nautiyal':"https://open.spotify.com/artist/1tqysapcCh1lWEAc9dIFpa",
        'Darshan Raval':"https://open.spotify.com/artist/2GoeZ0qOTt6kjsWW4eA6LS"
        }
    rand = random.randint(0,len(artist))
    randk=random.choice(list(artist.keys()))
    return render_template(
        "index.html",
         length = len(artist),
         artists = artist,
         randNum=rand,
         randkey=randk,
         randValue=artist.get(randk)
        )
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0'),
    use_reloader = True,
    debug = True, #Autorun
    )
