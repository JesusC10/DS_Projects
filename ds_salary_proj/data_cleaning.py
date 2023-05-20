# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:15:58 2023

@author: jesus
"""

import pandas as pd

df = pd.read_csv('data_scientist_jobs.csv')

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
df['avg_salary'] = (df['max_salary'] + df['min_salary']) / 2

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


df_out = df.drop(['Unnamed: 0'], axis=1)
df_out.to_csv('clean_data_science_jobs.csv', index = False)