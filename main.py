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

if not err and response['statusCode'] is 200:
  print(body['data'])
