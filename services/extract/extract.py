import logging
import random
from linkedin.linkedin import extract_linkedin_jobs
from glassdoor.glassdoor import extract_glassdoor_data
import api
from countries import get_countries
from job_titles import get_job_titles
import countries

def callback(linkedin_data: dict):
  #print('[ON_DATA]', data['title'], data['company'], data['company_link'], data['date'], data['link'], data['insights'], len(data['description']))
  del linkedin_data['insights']
  try:
    glassdoor_data = extract_glassdoor_data(linkedin_data['company'])
  except:
    logging.warn('extract_glassdoor_data failed. Skipping.')
  try:
    api.upload({ **linkedin_data, **glassdoor_data })
  except:
    logging.warn('api.upload failed. Skipping.')


if (__name__ == '__main__'): 
  countries = get_countries()
  job_titles = get_job_titles()
  while (True):
    country_idx = random.randint(0, len(countries) - 1)
    country = countries[country_idx]
    job_title_idx = random.randint(0, len(job_titles) - 1)
    job_title = job_titles[job_title_idx]
    extract_linkedin_jobs(callback, 'Remote %s' % job_title, [country], 10)
