import uuid
import json
from azure.data.tables import TableServiceClient
import datetime
from .secret import connection_string

service = TableServiceClient.from_connection_string(conn_str=connection_string)
table = service.get_table_client(table_name='jobs')

def job_exists(job: dict) -> bool:
  query = "title eq '%s' and company eq '%s' and date eq '%s'" % (job['title'], job['company'], job['date'])
  jobs = list(table.query_entities(query))
  if (len(jobs) > 0): 
    return True 
  else: 
    return False

def create_job(data: dict) -> dict:
  print(data)
  job_id = str(uuid.uuid4())
  timestamp = int(datetime.datetime.strptime(data['date'], "%Y-%m-%d").timestamp())
  job_entity = {
    **data,
    'id': job_id,
    'timestamp': timestamp,
    'PartitionKey': data['company'],
    'RowKey': job_id,
  }
  table.create_entity(job_entity)
  return job_entity