import uuid
from azure.data.tables import TableServiceClient
from azure.core.paging import ItemPaged
from .tags import get_tag_counts
from .secret import connection_string

service = TableServiceClient.from_connection_string(conn_str=connection_string)
table = service.get_table_client(table_name='jobs')

def query_jobs(search_term: str, order_by: str, num_results: int, created_since: int) -> list[ItemPaged]:
  if (len(search_term) > 0):
    tag_count = get_tag_counts(search_term, created_since)
    sorted_job_ids = list(dict(sorted(tag_count.items(), key=lambda item: item[1])).keys())
    jobs = get_jobs_by_ids(sorted_job_ids, created_since)
  else:
    jobs = all_jobs(created_since)
  sorted_jobs = sort_jobs(order_by, jobs)
  return sorted_jobs[0:int(num_results)]

def get_jobs_by_ids(ids: str, created_since: int) -> list[dict]:
  jobs = []
  for job_id in ids:
    job = list(table.query_entities("id eq '%s' and timestamp ge %d" % (job_id, int(created_since))))
    if (len(job) > 0):
      jobs = jobs + job
  return jobs 

def gd_revenue_to_int(x):
  try:
    revenue = x.split(' ')[0][1:];
    revenue = ''.join(c for c in revenue if c.isdigit())
    revenue = int(revenue)
  except:
    revenue = 0
  if ('million' in x): revenue *= 10e6
  elif ('billion' in x): revenue *= 10e9
  elif ('trillion' in x): revenue *= 10e12
  return revenue; 

def gd_rating_to_float(x):
  try:
    result = float(x)
    return result
  except:
    return 0.0

def sort_jobs(order_by: str, jobs: list) -> list:
  if (order_by == 'relevance'):
    return jobs # Sorted by relevance by default
  elif (order_by == 'timestamp'):
    return sorted(jobs, key=lambda item: -item['timestamp'])
  elif (order_by == 'gd_overall_rating'):
    return sorted(jobs, key=lambda item: -gd_rating_to_float(item['gd_overall_rating']))
  elif (order_by == 'gd_benefits_rating'):
    return sorted(jobs, key=lambda item: -gd_rating_to_float(item['gd_benefits_rating']))
  elif (order_by == 'gd_revenue'):
    return sorted(jobs, key=lambda item: -gd_revenue_to_int(item['gd_revenue']))
  return jobs

def all_jobs(created_since: int) -> list[ItemPaged]:
  return list(table.query_entities("timestamp ge %d" % int(created_since)))