import logging
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

logging.basicConfig(level=logging.INFO)

def click(locator, driver):
  logging.info('Click %s' % locator[1])
  elem = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locator))
  elem.click()

def extract_glassdoor_data(company_name: str, headless: bool = True):
  result = {
    'gd_company_name': company_name,
    'gd_website': None,
    'gd_employees': None,
    'gd_industry': None,
    'gd_revenue': None,
    'gd_overall_rating': None, 
    'gd_culture_rating': None, 
    'gd_diversity_rating': None, 
    'gd_worklife_rating': None, 
    'gd_management_rating': None, 
    'gd_benefits_rating': None, 
    'gd_career_rating': None,
    'gd_source': None
  }
  chrome_options = Options()
  if (headless):
    chrome_options.add_argument("--headless")
  driver = webdriver.Chrome(options=chrome_options)
  driver.set_window_size(960, 1280)
  # Search page
  query = '%20'.join(company_name.split())
  driver.get("https://www.glassdoor.com/Search/results.htm?keyword=" + query)
  # Sign in
  click((By.CLASS_NAME, "siteHeader__HeaderStyles__signInButton"), driver)
  username = driver.find_element_by_id("modalUserEmail")
  password = driver.find_element_by_id("modalUserPassword")
  username.send_keys("vuoriov4@gmail.com")
  password.send_keys("apinapaska123")
  click((By.NAME, "submit"), driver)
  time.sleep(1.0)
  # Company overview 
  click((By.CLASS_NAME, "company-tile"), driver)
  result['gd_revenue'] = driver.find_element_by_xpath("//div[@data-test='employer-revenue']").get_attribute('innerHTML')
  result['gd_employees'] = driver.find_element_by_xpath("//div[@data-test='employer-size']").get_attribute('innerHTML')
  result['gd_industry'] = driver.find_element_by_xpath("//a[@data-test='employer-industry']").get_attribute('innerHTML')
  result['gd_website'] = driver.find_element_by_xpath("//a[@data-test='employer-website']").get_attribute('innerHTML')
  result['gd_source'] = driver.current_url
  # Reviews
  click((By.XPATH, "//a[@data-label='Reviews']"), driver)
  #v2__EIReviewsRatingsStylesV2__ratingNum #v2__EIReviewsRatingsStylesV2__large #v2__EIReviewsRatingsStylesV2__ratingInfo
  click((By.CLASS_NAME, "v2__EIReviewsRatingsStylesV2__ratingNum"), driver)
  ratings = [
    { 'field': 'gd_overall_rating', 'class': 'overall-rating' },
    { 'field': 'gd_culture_rating', 'class': 'culture-rating' },
    { 'field': 'gd_diversity_rating', 'class': 'diversity-rating' },
    { 'field': 'gd_worklife_rating', 'class': 'worklife-rating' },
    { 'field': 'gd_management_rating', 'class': 'management-rating' },
    { 'field': 'gd_benefits_rating', 'class': 'benefits-rating' },
    { 'field': 'gd_career_rating', 'class': 'career-rating' }
  ]
  for x in ratings:
    rating_elem = driver.find_element_by_xpath("//div[@data-ga-action='%s']" % x['class'])
    if (x['class'] == 'overall-rating'): 
      class_name = 'eiRatingTrends__RatingTrendsStyle__overallRatingNum' 
    else: 
      class_name = 'eiRatingTrends__RatingTrendsStyle__ratingNum'
    result[x['field']] = rating_elem.find_element_by_class_name(class_name).get_attribute('innerHTML')
  driver.close()
  logging.info('extract_glassdoor_data: %s' % result)
  return result

if (__name__ == '__main__'):
  extract_glassdoor_data('Arrow Electronics', headless=True)