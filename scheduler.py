import schedule
import datetime
import time 
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

#def task():
#    curr = datetime.datetime.now().strftime("%H:%M:%S")
#    print("Hello world "+str(curr))

#schedule.every(1).minutes.at(":00").do(task)

#while True:
#    schedule.run_pending()
#    time.sleep(1)

client = WebClient(token="xoxb-3232981397716-3257672269472-H0jF2BdBw2z0LPZoIRC2bmQZ")
logger = logging.getLogger(__name__)
channel_id = "C036L0W9R46"

def task():
    curr = datetime.datetime.now().strftime("%H:%M:%S")
    try:
        result = client.chat_postMessage(
        channel=channel_id,
        text="Hello world "+str(curr)
    )
        print(result)
    
    except SlackApiError as e:
        print(f"Error: {e}")

schedule.every(10).minutes.at(":00").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)

while True:
    schedule.run_pending()
    time.sleep(1)
