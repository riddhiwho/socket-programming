# import http.server

# class RequestHandler(http.server.BaseHTTPRequestHandler):
    
#     #page template
#     Page = '''\
# <html>
# <body>
# <table>
# <tr>  <td>Header</td>         <td>Value</td>          </tr>
# <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
# <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
# <tr>  <td>Client port</td>    <td>{client_port}s</td> </tr>
# <tr>  <td>Command</td>        <td>{command}</td>      </tr>
# <tr>  <td>Path</td>           <td>{path}</td>         </tr>
# </table>
# </body>
# </html>
# '''
    
#     def do_GET(self):
#         page = self.create_page()
#         self.send_page(page)
        
#     def create_page(self):
#         values= {
#             'date_time' : self.date_time_string(),
#             'client_host': self.client_address[0],
#             'client_port': self.client_address[1],
#             'command' : self.command,
#             'path' : self.path 
            
#         }
        
#         page = self.Page.format(**values)
#         return page
    
#     def send_page(self, page):
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.send_header("Content-Length", str(len(self.Page.encode('utf-8'))))
#         self.end_headers()
#         self.wfile.write(self.Page.encode('utf-8'))

# if __name__ == '__main__':
#     serverAddress = ('', 8080)
#     httpd = http.server.HTTPServer(serverAddress, RequestHandler)
#     print('Server started...')
#     httpd.serve_forever()\
    
    
import http.server

class RequestHandler(http.server.BaseHTTPRequestHandler):
    
    # Page template
    Page = '''\
<html>
<body>
<table>
<tr>  <td>Header</td>         <td>Value</td>          </tr>
<tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
<tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
<tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
<tr>  <td>Command</td>        <td>{command}</td>      </tr>
<tr>  <td>Path</td>           <td>{path}</td>         </tr>
</table>
</body>
</html>
'''
    
    def do_GET(self):
        page = self.create_page()
        self.send_page(page)
        
    def create_page(self):
        values = {
            'date_time': self.date_time_string(),
            'client_host': self.client_address[0],
            'client_port': self.client_address[1],
            'command': self.command,
            'path': self.path 
        }
        
        page = self.Page.format(**values)
        return page
    
    def send_page(self, page):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(page.encode('utf-8'))))
        self.end_headers()
        self.wfile.write(page.encode('utf-8'))

if __name__ == '__main__':
    serverAddress = ('', 8080)
    httpd = http.server.HTTPServer(serverAddress, RequestHandler)
    print('Server started...')
    httpd.serve_forever()
