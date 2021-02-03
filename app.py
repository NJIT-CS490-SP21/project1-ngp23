import os,random
from flask import Flask,render_template

app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
def homepage():
   
   # artist={'Arijit Singh':"4YRxDV8wJFPHPTeXepOstw",
#        'Ed Sheeran':"6eUKZXaKkcviH0Ku9w2n3V",
 #       'Ariana Grande':"66CXWjxzNUsdJxJ2JdwvnR",
  #      'Jubin Nautiyal':"1tqysapcCh1lWEAc9dIFpa",
   #     'Darshan Raval':"2GoeZ0qOTt6kjsWW4eA6LS"
    #    }
    artist=["4YRxDV8wJFPHPTeXepOstw",
    "6eUKZXaKkcviH0Ku9w2n3V",
    "66CXWjxzNUsdJxJ2JdwvnR",
    "1tqysapcCh1lWEAc9dIFpa",
    "2GoeZ0qOTt6kjsWW4eA6LS"]
    rand = random.randint(0,len(artist))
    #randk=random.choice(list(artist.keys()))
    return render_template(
        "index.html",
         length = len(artist),
         artists = artist,
         randNum=rand,
        # randkey=randk,
        # randValue=artist.get(randk)
        )
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0'),
    use_reloader = True,
    debug = True, #Autorun
    )
