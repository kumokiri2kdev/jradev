import os.path
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = 'localhost'
PORT = 8080

class CallbackServer(BaseHTTPRequestHandler):
    def construct_path_dict(self):
        print("construct_path_dict")
        self.path_dict = {}
        
    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)
        self.construct_path_dict()

    def do_GET(self):
        if self.path == '/':
            path = 'index.html'
        else :
            path = self.path

        response = self.handle_http(path)
        self.wfile.write(response)

    def do_POST(self):
        content_len = int(self.headers['content-length'])
        post_body = self.rfile.read(content_len).decode("'utf-8'")
        splited = post_body.split('=')
        file_name = splited[1].replace('/','-')
        response = self.handle_http(file_name)
        self.wfile.write(response)

    def handle_http(self,  path):
        print(path)
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=shift_jis')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        if path.startswith('/') :
            path = path.lstrip('/')
        
        path = DATA_DIR + path
        
        if os.path.isfile(path):
        	with open(path, 'rb') as rfp:
        		content = rfp.read()
        else:
        	content = ""
        	
        return bytes(content)

           
            
if __name__ == '__main__':
    if ('JRA_DIR' in os.environ) == False:
        print("Directory Not Found")
        exit

    DATA_DIR = os.environ['JRA_DIR'] 
    server_class = HTTPServer
    httpd = server_class((HOST, PORT), CallbackServer)
    httpd.serve_forever()
