#!/usr/bin/env python3
import requests

URL="http://127.0.0.1:2224/data"

response= requests.get(URL).json()

for item in response:
    for key, value in item.items():
        if isinstance(value, list):
            value_str= ",".join(value)
        else:
            value_str= str(value)
        print(f"{key} : {value_str}")
    
