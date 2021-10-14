# You Need

- Endpoint: https://locus-api.com/v1/client/:clientId/spmdbatch/:batchId/task

- Path Variables:
    - clientID - a valid string value
    - batchID - a valid string value
    - Content-Type - applications/json
    - Body - Raw (use sample in this folder with name `task-three.json`)
- Basic Auth

## Using cURL

```cURL
curl --location --request POST 'https://locus-api.com/v1/client/:clientId/spmdbatch/:batchId/task' \
--data-raw 'copy-your-raw-task-three-json-content-here'
```

## Using Python http.client

```Python
import http.client

conn = http.client.HTTPSConnection("locus-api.com")
payload = "copy-your-raw-task-three-json-content-here" # or you can use file parsing with json loads
headers = {}
conn.request("POST", "/v1/client/:clientId/spmdbatch/:batchId/task", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

## Using Python requests

```Python
import requests

url = "https://locus-api.com/v1/client/:clientId/spmdbatch/:batchId/task"

payload = "copy-your-raw-task-three-json-content-here" # or you can use file parsing with json loads
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```