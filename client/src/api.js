const QUERY_SERVICE_URL = 'https://remote-jobs-eu-fnapp.azurewebsites.net/api/queryservice'; //

const query = async (searchTerm, orderBy, numResults, createdSince, signal) => {
  const options = { 
    method: 'GET', 
    mode: 'cors',
    headers: {
      'x-functions-key':"hZGChREtTUK7A0kuUESU-OS8gvFHjxp09zh2h69itkxfAzFuvM5glg==",
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    signal,
  };
  const params = '?' + new URLSearchParams({ 
    'search_term': searchTerm, 
    'order_by': orderBy, 
    'num_results': numResults, 
    'created_since': createdSince,
  });
  try {
    const response = await fetch(QUERY_SERVICE_URL + params, options);
    console.log('response', response);
    return response.json();
  } catch (error) {
    if (error.name !== 'AbortError') throw error;
  }
}

//const UPLOAD_SERVICE_URL =  'https://remote-jobs-eu-fnapp.azurewebsites.net/api/uploadservice'; //'http://localhost:7071/api/UploadService';

/*
const upload = async (data) => {
  const options = {
    method: 'POST', 
    mode: 'cors',
    headers: {
      'x-functions-key':"hZGChREtTUK7A0kuUESU-OS8gvFHjxp09zh2h69itkxfAzFuvM5glg==",
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    body: JSON.stringify(data)
  };
  const response = await fetch(UPLOAD_SERVICE_URL, options);
  console.log('response', response);
  return response.json();
};
*/

export default { query }