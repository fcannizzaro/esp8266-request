# esp8266-request
Make simple http requests on esp8266 Micropython

# Usage
```python
from request import Request

heads = { 'Authorization': 'Basic QWxhZGRpbjpPcGVuU2VzYW1l' }

# Get Request
err, response = Request.get('httpbin.org/get', heads)

# JSON response
if not err and response.statusCode is 200:
  print(response.body)

# Post Request (JSON Data)

data = {
  'arg' : [1,2,3],
  'nested' : {
    'inside' : 7
  }
}

# Response Body as file
err, _ = Request.post('httpbin.org/post', data, file='response.txt')
```

# Valid URL
- http://example.com
- www.example.com
- example.com
- example.com:8080
- example.com/path/to
- 93.184.216.34

# Request
Use python dictionaries for headers and post data.

# Response (Class)

## statusCode
request status code 200, 404, ...

## headers
python dictionary

## body
response body (text or dictionary)
