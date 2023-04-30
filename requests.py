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

# Here will be various usages of Python Lib "requests"
# https://docs.python-requests.org/en/v2.0.0/ - LIBRARY DOCUMENTATION / MANUAL
# For basic authentication, script below.. :)

import requests

req = requests.get('http://httpbin.org/basic-auth/user1/passwd', auth =('user1', 'passwd'))
print(req.text) # U can use req.json - this will give resp.code etc.



