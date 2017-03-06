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
