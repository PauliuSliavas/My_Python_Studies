###############################################################################
###############################################################################
####       Made By - Slyvoncas, for all Hackers and Makers :)              ####
####    This is my Python Learning exercises, if you can make it better,   ####
####    please do so and share it with me..!                               ####
####                                              @ baphomet               ####
####                                                                       ####
###############################################################################
###############################################################################

import requests

req = requests.get('http://httpbin.org/basic-auth/user1/passwd', auth =('user1', 'passwd'))
print(req.text) # U can use req.json - this will give resp.code etc.



