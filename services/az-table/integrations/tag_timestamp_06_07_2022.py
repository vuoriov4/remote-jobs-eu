import uuid
from azure.data.tables import TableServiceClient, UpdateMode
import datetime
from collections import Counter
from ..secret import connection_string

service = TableServiceClient.from_connection_string(conn_str=connection_string())
tags_table_client = service.get_table_client(table_name='tags')
jobs_table_client = service.get_table_client(table_name='jobs')

def create_tags(job_entity: dict) -> list[dict]:
  tag_id = str(uuid.uuid4())
  fields = ['company', 'title', 'description']
  result = []
  raw_str = ' '.join(job_entity[field] for field in fields)
  tag_list = raw_str.split(' ')
  tag_list = list(map(lambda x: ''.join(c for c in x.lower() if c.isalnum()), tag_list))
  tag_list = list(filter(lambda x: len(x) > 0, tag_list))
  counter = Counter(tag_list)
  tag_entities = []
  for key in counter:
    tag_entity = {
      'id': tag_id,
      "job_id": job_entity['id'],
      "count" : counter[key],
      "value" : key,
      'PartitionKey': job_entity['id'],
      'RowKey': key,
      'timestamp': job_entity['timestamp'] 
    }
    tag_entities.append(tag_entity)
  operations = list(map(lambda tag_entity: ("upsert", tag_entity), tag_entities))
  batch_size = 100
  for i in range(0, len(operations), batch_size):
    batch_ops = operations[i:i+batch_size]
    tags_table_client.submit_transaction(batch_ops)
  print("Added " + str(len(tag_entities)) + " tags.")
  return result

if __name__ == '__main__':
  #tags_table_client.delete_table()
  #tags_table_client.create_table()
  jobs = list(jobs_table_client.query_entities(""))
  for job in jobs:
    create_tags(job)
