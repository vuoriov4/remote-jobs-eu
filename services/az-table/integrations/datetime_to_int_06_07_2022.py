import uuid
from azure.data.tables import TableServiceClient, UpdateMode
import datetime 

connection_string = "DefaultEndpointsProtocol=https;AccountName=remotejobseustorage;AccountKey=R62QYH6DVeQYp/QSZufRI91qzg6nU0cQU+F2J+8WxBObJTknZxzyc82w95Mfu03S31JTUUPWi55B+AStEhc+ug==;EndpointSuffix=core.windows.net"
service = TableServiceClient.from_connection_string(conn_str=connection_string)

if __name__ == '__main__':
  for table in ['jobs']:
    table_client = service.get_table_client(table_name=table)
    data = list(table_client.query_entities(""))
    for job in data:
      date = job['date']
      timestamp = int(datetime.datetime.strptime(date, "%Y-%m-%d").timestamp())
      table_client.update_entity(
        mode=UpdateMode.REPLACE, 
        entity={ **job, 'timestamp': timestamp }
      )
