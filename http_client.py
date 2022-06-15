import json
import http.client

host = '127.0.0.1'
port = 9000

# Open
conn = http.client.HTTPConnection(host, port)

# Request
print('\nRequest')
headers = { 'Content-type': 'application/json' }
message = { 'message': 'hello world from client'}
body = json.dumps(message)
print(body)
conn.request('POST', '/', body, headers)

# Response
print('Response')
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
body = json.loads(data)
print(body)

# Close
conn.close()