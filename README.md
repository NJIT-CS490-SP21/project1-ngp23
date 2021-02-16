# project1-ngp23
## Technology Used in this Milestone
  - We use the cloud 9 services on aws to priview and make updates on the file.
## Framework 
  - Frame work we used was flask
## languages we used for coding M1 and M2 Python, HTML and CSS
## User will need to install all the require libraries in order for project to work using the code bellow
  - pip install Flask
  - pip install python-dotenv
  - pip install requests
  - npm install -g heroku
## Libraries needed to import for Milestone1 and Milestone2
  - Request
  - Flask
  - load_dotenv
  - find_dotenv
  - OS
  - random
  - Json
  - render_template
## API used for M1
 - Spotify API
 - you can get the Spotify key from https://developer.spotify.com/dashboard/login
## API used for M2
 - Spotify API used for M1.
 - Genius API
 - you can get the Genius key from https://genius.com/api-clients
## Secrect File
 - User will have to create an .env file in their project directory in which they will add the two line of code listed bellow
      - `export CLIENT_ID='{your API key}'`
      - `export CLIENT_SECRET='{your API key}'`
      - `export GENIUS_CLIENT_ACCESSTOKEN='{your Genius AccessToken}'`
## How to run the APP on the computer
 - cd into the directory
 - run `python app.py`
 - then preview the page
## Deploy to Heroku
 - Create a free account on heroku https://singup.heroku.com/login
 - Create an text file in directory called requirements.txt
 - Run the line of code in terminal in directory  `pip freeze > requirements.txt`  This will add all the needed libraries in the requirements.txt file.
 - If for some reason the code above doesnt work then you can always run the command `[pip freeze]` in terminal it will list out all the libraries used for the directory. Just copy those libraies in `requirements.txt` file.
 - Now create another file call Procfile in the same directory. Add `web: python app.py` in the `Procfile`.
 - Once done with previous steps makes sure to do `git add -A` and `git commit -m "text"` to commit all the changes to git repo.
 - Now login to heroku account from terminal using the `heroku login -i`
 - Now create an new app to deploy `heroku create`
 - once the app is created it will give print out url in the terminal where heroku will deploy the appications.
 - do `git push heroku (main or master)` what is does is that it will push you repo to the heroku's repo.
 - once its push you can do `heroku open` which will give you link to open the application.
 - Since we using the .env to hide the API keys we will need to add the keys into heroku so that It can access the keys. So the way we will add is login to the heroku from browser. Once the dashboard pops up click on the app which needs secret key. Click on the setting then scroll down you see will see "Reveal Config Vars". In that add your keys from .env file.
 - Now app should open without any problem.
## what are at least 3 technical issues encountered with your prject? how did you fix them?
 - The problem I encounter during the process was the CSS cache issue. I used the app.config`['SEND_FILE_MAX_AGE_DEFAULT'] = 0` to fix the cache. Apart from that I have figure out other solution if the existing doesnt work it would be to got browser setting =>  go to clearing browsing data => Clear the cache image and file.
 - Other problem I encounter during the process was JSON file format. To fix this issue I created a text file and add the JSON data in that text file which beautify the file.
 - Genius Link not working beacuse of the token issue. I fixed it by getting a new token.
 - I also faced problem while deploying on herkou because I was not adding all the requirements in the requirements.txt file 
## what are known problem (Still existing), if any, with your project?
  - The know problem is genius not returning the excet data while using the API sometimes it returns the wrong lyrics because of the song name.
  - Sometimes Genius API gets corrupted so have to replace with the new key.
 ## What would you do to improve you project in the future?
 - Make more user friendly by adding more features such as give user ability to add the artist to their favourite list or add the song to their spotify library.
 - Make more user interactive by adding an search bar where user can search for their favourtie song and artist.
 
 
