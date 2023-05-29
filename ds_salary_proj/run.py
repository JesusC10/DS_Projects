# -*- coding: utf-8 -*-
"""
Created on Sat May 13 19:45:07 2023

@author: jesus
"""

import glassdoor_scrapper as gs

path = "chromedriver"
keyword = "data science"

#This line will open a new chrome window and start the scraping.
df = gs.get_jobs("data scientist", 30, True, path, 15)
df.to_csv(keyword+"_jobs.csv")
df