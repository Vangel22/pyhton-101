from http.server import BaseHTTPRequestHandler, HTTPServer


class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'This is a GET request response.')


def run_server():
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, GetHandler)
    print('Server is running on port 3000')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()

# if __name__ == "__main__": block ensures that the run_server() function is only called
# when the script is run directly (not when it's imported as a module).
