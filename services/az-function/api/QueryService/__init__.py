import azure.functions as func
import logging
import json
from .jobs import query_jobs

def main(req: func.HttpRequest) -> func.HttpResponse:
  logging.info('Python HTTP trigger function processed a request.')
  search_term = ''
  if ('search_term' in req.params):
    search_term = req.params['search_term']
  order_by = req.params['order_by']
  num_results = req.params['num_results']
  created_since = req.params['created_since']
  jobs = query_jobs(search_term, order_by, num_results, created_since)
  response = {
    'jobs': jobs,
  }
  return func.HttpResponse(json.dumps(response), mimetype="application/json")

