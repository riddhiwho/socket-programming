import http.server

class RequestHandler(http.server.BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed page.'''
    
    # Page to send back
    Page = '''\
<html>
<body>
<p>Hello, there!</p>
</body>
</html>
'''

    # Handle a GET Request
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page.encode('utf-8'))))
        self.end_headers()
        self.wfile.write(self.Page.encode('utf-8'))

if __name__ == '__main__':
    serverAddress = ('', 8080)
    httpd = http.server.HTTPServer(serverAddress, RequestHandler)
    print('Server started...')
    httpd.serve_forever()