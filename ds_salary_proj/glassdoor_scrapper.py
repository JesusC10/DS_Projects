from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
import pandas as pd
import time


def fetch_jobs(keyword, location,num_pages, path):
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)

    url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=11047&locKeyword="'+ location +'"&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    driver.get(url)
      
    #Set current page to 1
    current_page = 1     
        
        
    time.sleep(3)
    
    while current_page <= num_pages:   
        
        done = False
        while not done:
            job_cards = driver.find_elements(By.XPATH,"//article[@id='MainCol']//ul/li[@data-adv-type='GENERAL']")
            for card in job_cards:
                card.click()
                time.sleep(1)

                #Closes the signup prompt
                try:
                    driver.find_element(By.XPATH,".//span[@class='SVGInline modal_closeIcon']").click()
                    time.sleep(2)
                except NoSuchElementException:
                    time.sleep(2)
                    pass

# =============================================================================
#                 #Expands the Description section by clicking on Show More
#                 try:
#                     driver.find_element(By.XPATH,"//div[@class='css-t3xrds e856ufb4']").click()
#                     time.sleep(1)
#                 except NoSuchElementException:
#                     card.click()
#                     print(str(current_page) + '#ERROR: no such element')
#                     time.sleep(3)
#                     #driver.find_element(By.XPATH,"//div[@class='css-t3xrds e856ufb4']").click()
#                 except ElementNotInteractableException:
#                     card.click()
#                     driver.implicitly_wait(3)
#                     print(str(current_page) + '#ERROR: not interactable')
#                     #driver.find_element(By.XPATH,"//div[@class='css-t3xrds e856ufb4']").click()
# 
# =============================================================================
                #Scrape 

                try:
                    company_name = (driver.find_element(By.XPATH,"//div[@data-test='employerName']").text)
                except:
                    print("Missing Employer")
                    company_name = -1
                    pass

                try:
                    job_title = (driver.find_element(By.XPATH,"//div[@data-test='jobTitle']").text)
                except:
                    print("Missisng Job Title")
                    job_title = -1
                    pass

                try:
                    location = (driver.find_element(By.XPATH,"//div[@data-test='location']").text)
                except:
                    print("Missing Location")
                    location = -1
                    pass

                try:
                    job_description = (driver.find_element(By.XPATH,"//div[@class='JobDescriptionContent desc']").text)
                except:
                    print("Missing description")
                    job_description = -1
                    pass

                try:
                    rating = (driver.find_element(By.XPATH,"//span[@data-test='detailRating']").text)
                except:
                    print("Missing Rating")
                    salary_estimate = -1
                    pass
                
                try:
                    salary_estimate = (driver.find_element(By.XPATH,"//span[@data-test='detailSalary']").text)
                except:
                    print("Missing Salary")
                    salary_estimate = -1
                    pass
                try:
                    company_size = (driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Size']//following-sibling::*").text)
                except:
                    print("Missing Size")
                    company_size = -1
                    pass
                
                try:
                    company_type = (driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Type']//following-sibling::*").text)
                except:
                    print("Missing Type")
                    company_type = -1
                    pass
                    
                try:
                    company_sector = (driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Sector']//following-sibling::*").text)
                except:
                    print("Missing Sector")
                    company_sector = -1
                    pass
                    
                try:
                    company_industry = (driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Industry']//following-sibling::*").text)
                except:
                    print("Missing Industry")
                    company_industry = -1
                    pass
                    
                try:
                    company_founded = (driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Founded']//following-sibling::*").text)
                except:
                    print("Missing Founded")
                    company_founded = -1
                    pass
                    
                try:
                    company_revenue = (driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Revenue']//following-sibling::*").text)
                except:
                    print("Missing Revenue")
                    company_revenue = -1
                    pass
                    
                    
                    
                    
                done = True
                
       # Moves to the next page         
        if done:
            print(str(current_page) + ' ' + 'out of' +' '+ str(num_pages) + ' ' + 'pages done')
            driver.find_element(By.XPATH,"//span[@alt='next-icon']").click()   
            current_page = current_page + 1
            time.sleep(4)
            




    driver.close()
    df = pd.DataFrame({'company': company_name, 
    'job title': job_title,
    'location': location,
    'job description': job_description,
    'salary estimate': salary_estimate,
    'company_size': company_size,
    'company_type': company_type,
    'company_sector': company_sector,
    'company_industry' : company_industry, 'company_founded' : company_founded, 'company_revenue': company_revenue})
    
    df.to_csv(keyword + '.csv')
                       
                       
                       
    
    