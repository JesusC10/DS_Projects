# -*- coding: utf-8 -*-
"""
Created on Tue May 30 09:27:02 2023

@author: jesus
"""

# importing the requests library
import requests
from data_input import data_in
  
# api-endpoint
URL = 'http://127.0.0.1:5000/predict'
  
# defining a params dict for the parameters to be sent to the API
headers = {"Content-Type": "application/json"}
data = {"input": data_in}
  
# sending get request and saving the response as response object
r = requests.get(URL, headers = headers,json=data)
  
# extracting data in json format
r.json()