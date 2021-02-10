from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
<style>
h1 {text-align: center;}
.hello {text-align: center;}
h1 {color:blue;}
.hello {color:green;}
h1 {font-family:'Arial Narrow';}
.hello {font-family:verdana;}
</style>
<title>MY WEBSERVER</title>
</head>
<body>
<h1><u>Multiplication table of 11</u></h1>
<p class = "hello">4 x 0 = 0</p>
<p class = "hello">4 x 1 = 4</p>
<p class = "hello">4 x 2 = 8</p>
<p class = "hello">4 x 3 = 12</p>
<p class = "hello">4 x 4 = 16</p>
<p class = "hello">4 x 5 = 20</p>
<p class = "hello">4 x 6 = 24</p>
<p class = "hello">4 x 7 = 28</p>
<p class = "hello">4 x 8 = 32</p>
<p class = "hello">4 x 9 = 36</p>
<p class = "hello">4 x 10 = 40</p>
<p class = "hello">4 x 11 = 44</p>
<p class = "hello">4 x 12 = 48</p>
</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")

        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()

        self.wfile.write(content.encode())

server_address = ('',80)

httpd = HTTPServer(server_address,myhandler)

print("my webserver is running...")
httpd.serve_forever()