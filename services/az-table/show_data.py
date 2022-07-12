from azure.data.tables import TableServiceClient
from secret import connection_string
service = TableServiceClient.from_connection_string(conn_str=connection_string())

def show_data():
  for table in ['jobs', 'tags']:
    table_client = service.get_table_client(table_name=table)
    data = list(table_client.query_entities(""))
    print(data)

if __name__ == '__main__':
  show_data()