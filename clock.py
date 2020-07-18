import requests
import main
import config

def clock():

    r = requests.get(main.CLOCK_URL, headers=config.HEADERS)
    print(r.content)


clock()    
##MBNL1BQ24S