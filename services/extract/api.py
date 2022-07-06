import requests
import json 

UPLOAD_SERVICE_URL = 'http://localhost:7071/api/UploadService'; #'https://remote-jobs-eu-fnapp.azurewebsites.net/api/uploadservice'; #

def upload(data):
  headers = {
    'x-functions-key':"hZGChREtTUK7A0kuUESU-OS8gvFHjxp09zh2h69itkxfAzFuvM5glg==",
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }
  json_data = json.dumps(data)
  response = requests.post(UPLOAD_SERVICE_URL, data=json_data, headers=headers)
  return response.json()
