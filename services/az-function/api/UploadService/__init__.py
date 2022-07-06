import logging
import json
import azure.functions as func
from .jobs import create_job, job_exists
from .tags import create_tags
from .geolocate import geolocate

def main(req: func.HttpRequest) -> func.HttpResponse:
  logging.info('Python HTTP trigger function processed a request.')
  data = req.get_json()
  if (job_exists(data)):
    result = { 'message': 'Job already exists.' }
    logging.info('Job already exists')
    return func.HttpResponse(json.dumps(result), status_code=400, mimetype="application/json")
  try:
    lat, lon = geolocate(data['place'])
    data['lat'] = lat 
    data['lon'] = lon
  except:
    result = { 'message': 'Failed to geolocate.' }
    logging.info('Failed to geolocate.')
    return func.HttpResponse(json.dumps(result), status_code=400, mimetype="application/json")
  job_entity = create_job(data)
  create_tags(job_entity)
  return func.HttpResponse(json.dumps(job_entity), status_code=201, mimetype="application/json")