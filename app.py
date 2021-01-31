import os
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def homepage():
    artist=["Arijit Singh","Ed Sheeran","Ariana Grande"]
    return render_template(
        "index.html",
         len= len(artist),
         artist = artist
        )
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0'),
    use_reloader = True,
    debug = True
    )