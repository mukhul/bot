import time
from time import sleep
from time import ctime
import main


def trail_buy():
    t_end = time.time() + 100

    while True:

        number = 0

        if (time.time() == t_end) or (time.time() > t_end):
            print("time over!! == t_end == {}".format(time.ctime()))
            break
        
        while time.time() < t_end:

            print(time.ctime())
                 
            if number == 0:
                break

            else:
                print("its some other number bro!!")    
                break
            
        time.sleep(1)

trail_buy()      
# main.create_order("TSLA", 100, "buy", "market", "gtc")  


    