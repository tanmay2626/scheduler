import schedule
import datetime
import os
import time 
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()

channel_ID = os.getenv("CHANNEL_ID")
token_ID = os.getenv("TOKEN")

#def task():
#    curr = datetime.datetime.now().strftime("%H:%M:%S")
#    print("Hello world "+str(curr))

#schedule.every(1).minutes.at(":00").do(task)

#while True:
#    schedule.run_pending()
#    time.sleep(1)

client = WebClient(token=token_ID)
logger = logging.getLogger(__name__)
channel_id = channel_ID

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
