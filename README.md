# Data Science Projects Repo (All my public data science projects)
## Data Science Salary Estimator (DS_SALARY_PROJ)
* Created a tool the helps you estimate jobs salaries (MAE ~ $ 1K) in orther to help negotiate you income based on your job description.
* Scrapped ~1000 jobs found on glass door by using python and sellenium.
* Optimized Linear, Lasso and Random Forest Regressors using GridSearchCV  
* Built a endpoint API using flask

### Code & Resources used
**Python Version:** 3.9.13  
**Packages:** pandas, numpy, sklearn, seaborn, selenium, flask, json, pickle  
**Web Framework Requirements:** ```pip install -r requierements.text```  
**Scrapper Article:** https://mersakarya.medium.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  
**Scrapper Article:** https://medium.com/@benjaminrohan010/scraping-glassdoor-using-selenium-and-python-2022-bd0065775aec  
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2  
**API Request:** https://www.geeksforgeeks.org/get-post-requests-using-python/  

### Youtube Walkthrough Playlist
https://youtu.be/MpF9HENQjDo

### Web Scrapping
Tweaked the web scrapper (two articles above) to scrape 1000 job postings from glassdoor. With each job we got the following attributes:
* Job Title
* Salary Estimate
* Job Description
* rating
* Company
* Location
* Company Headquarters
* Company Size
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

### Data Cleaning



