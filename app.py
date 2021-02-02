import os
from flask import Flask,render_template

app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
def homepage():
    artist=["Arijit Singh","Ed Sheeran","Ariana Grande","Jubin Nautiyal","Darshan Raval"]
    return render_template(
        "index.html",
         len= len(artist),
         artist = artist
        )
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0'),
    use_reloader = True,
    debug = True,
    )
