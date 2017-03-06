import usocket as socket
import ujson as json
import ure as re

print('\n >> using esp8266-Request v1.0.0\n')

class Response:

  def __init__(self, statusCode, body, headers):
    self.body = body
    self.headers = headers
    self.statusCode = statusCode

class Request:

  @staticmethod
  def parse(url):

    regex = r"(?:https?://)?(?:www\.)?([^:/]*)((?::\d+)?)(\/?.*)"

    if re.match(regex,url):
      m = re.search(regex,url)
      port = m.group(2) or ':80'
      addr = socket.getaddrinfo(m.group(1), int(port[1:]))[0][-1]
      return (None, m.group(3) or '/',addr[0],addr[1])
    
    else:
      return ('Invalid URL String',None,None)
    

  @staticmethod
  def response(req,send,file):

    req.send(str.encode(send))

    data = req.recv(512)
 
    if file:

      f = open(file, 'a')

      while data:
        f.seek(0, 2)
        f.write(str(data,'utf-8'))
        data = req.recv(512)

      f.close()

    else:

      res = ''

      while data:
        res += str(data,'utf-8')
        data = req.recv(512)

      headers = {}
      split = res.split('\r\n')

      for idx, value in enumerate(split):
        if not value:
          body = '\r\n'.join(split[idx+1:])
          break
        elif ":" in value:
          line = value.split(':', 1)
          key = line[0]
          headers[key] = line[1][1:]

      if "application/json" in (headers['Content-Type'] or headers['content-type'] or ''):
        body = json.loads(body)

      # Extract status code
      _, statusCode, _ = split[0].split(' ', 2)
    
      return (None, Response(int(statusCode), headers, body))

    req.close()
    
    return (None,None)

  @staticmethod
  def send(method, url, headers, file, content=None):
    
    err, path, ip, port = Request.parse(url)

    if err:
      return (err, None)

    else:
      try:

        req = socket.socket()
        req.connect((ip,port))

        send = "%s %s HTTP/1.0\r\n" % (method,path)
        send += "Host: %s\r\n" % (ip)
      
        for key, value in headers.items():
          send += "%s: %s\r\n" % (key,value)
        
        send += '\r\n'

        if content is not None:
          send += content
          
        return Request.response(req,send,file)

      except Exception as e:
        return (e, None, None)

  @staticmethod
  def get(url,headers={},file=None):
    return Request.send('GET', url, headers,file)
  
  @staticmethod
  def post(url,body={},headers={},file=None):
    data = json.dumps(body)
    headers["content-length"] = len(data)
    headers["content-type"] = "application/json"
    return Request.send('POST', url, headers, file, data)
