import uuid
from azure.data.tables import TableServiceClient
from .secret import connection_string

service = TableServiceClient.from_connection_string(conn_str=connection_string())

def create_tables():
  for table in ['jobs', 'tags']:
    table_client = service.get_table_client(table_name=table)
    table_client.create_table()

if __name__ == '__main__':
  create_tables()