import json
import time



def hello(event, context):
    print("Hello World")
    time.sleep(4)

    return "Another Hello World"
