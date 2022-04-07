import schedule
import datetime
import time 

def task():
    curr = datetime.datetime.now().strftime("%H:%M:%S")
    print("Hello world "+str(curr))

schedule.every(1).minutes.at(":00").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)