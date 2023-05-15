# -*- coding: utf-8 -*-
"""
Created on Sat May 13 19:45:07 2023

@author: jesus
"""

import glassdoor_scrapper as gs
import pandas as pd


path = r"chromedriver"

#This line will open a new chrome window and start the scraping.
df = gs.fetch_jobs("data scientist","Mexico", 30, path)
df