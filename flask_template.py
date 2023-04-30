######################################################################
###################################################################### 
###          ____  _                                               ###
##          / ___|| |_   ___   _____  _ __   ___ __ _ ___           ##
##          \___ \| | | | \ \ / / _ \| '_ \ / __/ _` / __|          ##
##           ___) | | |_| |\ V / (_) | | | | (_| (_| \__ \          ##
##          |____/|_|\__, | \_/ \___/|_| |_|\___\__,_|___/          ##
##                   |___/                                          ##
###                                                                ###
######################################################################
######################################################################

# You should always render html file from file not direct in .py code, for that render.template will work
# You should also add .html file in the same directory as you app.py file
# As usual all info regarding this is --> https://flask.palletsprojects.com/en/2.3.x/quickstart/#logging

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def flaskProject():
    return render_template('index.html')



