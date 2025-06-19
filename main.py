import time
from plyer import notification

while True:
    print("Have some water!!!!!!!!!")
    notification.notify(title='Time to have some water!', 
                        message="Stay hydrated! Drink some water now!!! ",
                        timeout=10)
    time.sleep(60*60)