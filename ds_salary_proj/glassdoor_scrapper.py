# -*- coding: utf-8 -*-
"""
Created on Wed May 17 09:28:10 2023

@author: jesus
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pandas as pd

def get_jobs(keyword, num_pages, verbose, path, sleep_time):
     
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)
    
    url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=Remote&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    driver.get(url)
    #Set current page to 1
    current_page = 1   
    jobs = []
    
    

    time.sleep(sleep_time)
    while current_page <= num_pages:
        try:
            driver.find_element(By.CLASS_NAME,"selected").click()
        except ElementClickInterceptedException:
            pass

        time.sleep(.1)

        try:
            driver.find_element(By.CSS_SELECTOR,'[alt="Close"]').click()  #clicking to the X.
        except NoSuchElementException:
            pass
        done = False
        while not done:
        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
    
            #Going through each job in this page
            job_buttons = driver.find_elements(By.XPATH,"//article[@id='MainCol']//ul/li[@data-adv-type='GENERAL']")  #jl for Job Listing. These are the buttons we're going to click.
            for job_button in job_buttons:  
# =============================================================================
#                 
#                 #Expands the Description section by clicking on Show More
#                 try:
#                     driver.find_element(By.XPATH, "//div[@class='css-t3xrds e856ufb2']").click()
#                     time.sleep(1)
#                 except NoSuchElementException:
#                     job_button.click()
#                     print(str(current_page) + '#ERROR: no such element')
#                     time.sleep(3)
#                     #driver.find_element(By.XPATH"//div[@class='css-t3xrds e856ufb2']").click()
#                 except ElementNotInteractableException:
#                     job_button.click()
#                     driver.implicitly_wait(3)
#                     print(str(current_page) + '#ERROR: not interactable')
#                     #driver.find_element(By.XPATH"//div[@class='css-t3xrds e856ufb2']").click()
#                 
# =============================================================================
                job_button.click()  #You might 
                time.sleep(1)
                
                try:
                    company_name = driver.find_element(By.XPATH,'.//div[@data-test="employerName"]').text
                    location = driver.find_element(By.XPATH,'.//div[@data-test="location"]').text
                    job_title = driver.find_element(By.XPATH,'.//div[@data-test="jobTitle"]').text
                    job_description = driver.find_element(By.XPATH,'.//div[@class="jobDescriptionContent desc"]').text
                except:
                    time.sleep(5)
                
                try:
                    salary_estimate = driver.find_element(By.XPATH,'.//span[@data-test="detailSalary"]').text
                except NoSuchElementException:
                    salary_estimate = -1 #You need to set a "not found value. It's important."
                
                try:
                    rating = driver.find_element(By.XPATH,'.//span[@data-test="detailRating"]').text
                except NoSuchElementException:
                    rating = -1 #You need to set a "not found value. It's important."
                
                #Printing for debugging
                if verbose:
                    print("Job Title: {}".format(job_title))
                    print("Salary Estimate: {}".format(salary_estimate))
                    print("Job Description: {}".format(job_description[:500]))
                    print("Rating: {}".format(rating))
                    print("Company Name: {}".format(company_name))
                    print("Location: {}".format(location))
                
                #Going to the Company tab...
                #clicking on this:
                #<div class="tab" data-tab-type="overview"><span>Company</span></div>
                try:
                    headquarters = driver.find_element(By.XPATH,'.//div[@id="CompanyContainer"]//span[text()="Headquarters"]//following-sibling::*').text
                except NoSuchElementException:
                    headquarters = -1
                
                try:
                    size = driver.find_element(By.XPATH,'.//div[@id="CompanyContainer"]//span[text()="Size"]//following-sibling::*').text
                except NoSuchElementException:
                    size = -1
                
                try:
                    founded = driver.find_element(By.XPATH,'.//div[@id="CompanyContainer"]//span[text()="Founded"]//following-sibling::*').text
                except NoSuchElementException:
                    founded = -1
                
                try:
                    type_of_ownership = driver.find_element(By.XPATH,'.//div[@id="CompanyContainer"]//span[text()="Type"]//following-sibling::*').text
                except NoSuchElementException:
                    type_of_ownership = -1
                
                try:
                    industry = driver.find_element(By.XPATH,'.//div[@id="CompanyContainer"]//span[text()="Industry"]//following-sibling::*').text
                except NoSuchElementException:
                    industry = -1
                
                try:
                    sector = driver.find_element(By.XPATH,'.//div[@id="CompanyContainer"]//span[text()="Sector"]//following-sibling::*').text
                except NoSuchElementException:
                    sector = -1
                
                try:
                    revenue = driver.find_element(By.XPATH,'.//div[@id="CompanyContainer"]//span[text()="Revenue"]//following-sibling::*').text
                except NoSuchElementException:
                    revenue = -1
                
                try:
                    competitors = driver.find_element(By.XPATH,'.//div[@id="CompanyContainer"]//span[text()="Competitors"]//following-sibling::*').text
                except NoSuchElementException:
                    competitors = -1
                
                
                if verbose:
                    print("Headquarters: {}".format(headquarters))
                    print("Size: {}".format(size))
                    print("Founded: {}".format(founded))
                    print("Type of Ownership: {}".format(type_of_ownership))
                    print("Industry: {}".format(industry))
                    print("Sector: {}".format(sector))
                    print("Revenue: {}".format(revenue))
                    print("Competitors: {}".format(competitors))
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                
                jobs.append({"Job Title" : job_title,
                    "Salary Estimate" : salary_estimate,
                    "Job Description" : job_description,
                    "Rating" : rating,
                    "Company Name" : company_name,
                    "Location" : location,
                    "Headquarters" : headquarters,
                    "Size" : size,
                    "Founded" : founded,
                    "Type of ownership" : type_of_ownership,
                    "Industry" : industry,
                    "Sector" : sector,
                    "Revenue" : revenue,
                    "Competitors" : competitors})
                #add job to jobs
                
                done = True
                
            
        if done: 
            #Clicking on the "next page" button
            try:
                driver.find_element(By.XPATH,'.//span[@alt="next-icon"]').click()
                current_page += 1
                time.sleep(3)
            except NoSuchElementException:
                print("Scraping terminated before reaching target number of pages. Needed {}, got {}.".format(num_pages, len(jobs)))
                
            
    
    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.
