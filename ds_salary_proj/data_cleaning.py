# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:15:58 2023

@author: jesus
"""

import pandas as pd

df = pd.read_csv('data_scientist_jobs_2.csv')

#salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x : 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x : 1 if 'employer provided salary' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x : x.split('(')[0])
minus_kd = salary.apply(lambda x : x.replace('K', '').replace('$',''))

minus_hr = minus_kd.apply(lambda x : x.lower().replace('per hour', ''))
minus_ep = minus_hr.apply(lambda x : x.lower().replace('employer provided salary:', ''))

add_range = minus_ep.apply(lambda x : x + ' - '+ x if len(x.split('-')) == 1 else x)

df['min_salary'] = add_range.apply(lambda x : int(float(x.split('-')[0])))
df['max_salary'] = add_range.apply(lambda x : int(float(x.split('-')[1])))

#company name text only
df['company_text'] = df.apply(lambda x : x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#Location field
complete_location = df['Location'].apply(lambda x : x + ', '+ x if len(x.split(',')) == 1 else x)
df['job_state'] = complete_location.apply(lambda x : x.split(',')[1])

#Age of company
df['age'] = df['Founded'].apply(lambda x : x if x < 1 else 2023 - x)

#Parsing of job description (python, etc)
#Python
df['python_yn'] = df['Job Description'].apply(lambda x : 1 if 'python' in x.lower() else 0)
#R Studio
df['rstudio_yn'] = df['Job Description'].apply(lambda x : 1 if 'r studio' in x.lower() else 0)
#Spark
df['spark_yn'] = df['Job Description'].apply(lambda x : 1 if 'spark' in x.lower() else 0)
#AWS
df['aws_yn'] = df['Job Description'].apply(lambda x : 1 if 'aws' in x.lower() else 0)
#Excel
df['excel_yn'] = df['Job Description'].apply(lambda x : 1 if 'excel' in x.lower() else 0)

#Simplify Job title
def title_simplifier(title):
    if 'data scientist' in title.lower():
        return 'data scientist'
    elif 'data enineer' in title.lower():
        return 'data enineer'
    elif 'analyst' in title.lower():
        return 'analyst'
    elif 'machine learning' in title.lower():
        return 'mle'
    elif 'manager' in title.lower():
        return 'manager'
    if 'director' in title.lower():
        return 'director'
    else:
        return 'na'
    
def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr.' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
        return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower():
        return 'jr'
    else:
        return 'na'
    
df['job_simp'] = df['Job Title'].apply(title_simplifier)
df['seniority'] = df['Job Title'].apply(seniority)

#Job description length
df['desc_len'] = df['Job Description'].apply(lambda x : len(x))

# Hourly wage to annual
df['min_salary'] = df.apply(lambda x: x.min_salary*2 if x.hourly == 1 else x.min_salary, axis=1)
df['max_salary'] = df.apply(lambda x: x.max_salary*2 if x.hourly == 1 else x.max_salary, axis=1)
df['avg_salary'] = (df['max_salary'] + df['min_salary']) / 2

df['company_txt'] = df.company_text.apply(lambda x: x.replace('\n',''))


df_out = df.drop(['Unnamed: 0'], axis=1)
df_out.to_csv('clean_data_science_jobs_2.csv', index = False)