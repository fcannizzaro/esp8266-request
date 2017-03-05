# esp8266-request
Make simple http requests on esp8266 Micropython

# Usage
```python
from request import Request

heads = { 'Authorization': 'Basic QWxhZGRpbjpPcGVuU2VzYW1l' }

# Get Request

err, response, body = Request.get('httpbin.org/get', heads)

# Post Request (JSON Data)

data = {
  'arg' : [1,2,3],
  'nested' : {
    'inside' : 7
  }
}

err, response, body = Request.post('httpbin.org/post', data)

# access json response

if not err and response.statusCode is 200:
  print(body['data'])

```

# Valid URL
- http://example.com
- www.example.com
- example.com
- example.com:8080
- example.com/path/to

# Request
Use python dictionaries for headers and post data.

# Response
```python
status = response.statusCode  # 200, 404 ..
headers = response.headers    
```

# JSON
If response body is a **json**, body is a python **dictionary**.
