import uuid
from azure.data.tables import TableServiceClient
from azure.core.paging import ItemPaged
from operator import itemgetter
from .secret import connection_string

service = TableServiceClient.from_connection_string(conn_str=connection_string)
table = service.get_table_client(table_name='tags')

def group_tags_by_job_id(tags) -> dict:
  tags.sort(key=itemgetter('job_id'))
  result = {}
  for tag in tags:
    if (tag['job_id'] in result):
      result[tag['job_id']].append(tag)
    else:
      result[tag['job_id']] = [tag]
  return result

def query_tags(value: str, created_since: int) -> list[ItemPaged]:
  tag_filter = "value eq '%s' and timestamp ge %d" % (value.lower(), int(created_since))
  tags = list(table.query_entities(tag_filter))
  return tags

def get_tag_counts(search_term: str, created_since: int) -> dict:
  tag_count = {}
  for x in search_term.split(' '):
    search_term = ''.join(c for c in x.lower() if c.isalnum())
    tags = query_tags(search_term, created_since)
    groups = group_tags_by_job_id(tags)
    for job_id in groups:
      tag_count[job_id] = (tag_count[job_id] if (job_id in tag_count) else 0) + len(groups[job_id])
  return tag_count