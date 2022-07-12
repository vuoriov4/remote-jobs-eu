import azure.functions as func
import logging
import time
import json
from .jobs import query_jobs

def main(req: func.HttpRequest) -> func.HttpResponse:
  logging.info('Python HTTP trigger function processed a request.')
  search_term = ''
  if ('search_term' in req.params):
    search_term = req.params['search_term']
  order_by = 'relevance'
  if ('order_by' in req.params):
    order_by = req.params['order_by']
  num_results = 50
  if ('num_results' in req.params):
    num_results = req.params['num_results']
  created_since = int(time.time() - 60*60*24*7)
  if ('created_since' in req.params):
    created_since = req.params['created_since']
  jobs = query_jobs(search_term, order_by, num_results, created_since)
  response = {
    'jobs': jobs,
  }
  return func.HttpResponse(json.dumps(response), mimetype="application/json")

