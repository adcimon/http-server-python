import json
import http.server

host = '127.0.0.1'
port = 9000

class MyServer(http.server.BaseHTTPRequestHandler):

    def read(self):
        n = int(self.headers['Content-Length'])
        data = self.rfile.read(n)
        return data

    def write(self, str):
        data = bytes(str, 'utf-8')
        self.wfile.write(data)

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.write('<html>')
        self.write('<head>')
        self.write('<title>HTTP Server</title>')
        self.write('</head>')
        self.write('<body>')
        self.write('<h1>HTTP server</h1>')
        self.write('<p>This is a simple HTTP server.</p>')
        self.write('</body>')
        self.write('</html>')

    def do_POST(self):

        # Request
        print('\nRequest')
        data = self.read()
        body = json.loads(data)
        print(body)

        # Response
        print('Response')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        message = { 'message': 'hello world from server' }
        body = json.dumps(message)
        print(body)
        self.write(body)

def main():
    server = http.server.HTTPServer((host, port), MyServer)
    print('🚀 Server running on: http://%s:%s' % (host, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()  

if __name__ == '__main__':
    main()