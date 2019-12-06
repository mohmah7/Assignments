from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])

    fh = open("text.txt")
    lines = [fh.readline().encode("utf-8") for i in range(30)]

    return lines


server = make_server('192.168.1.39', 5061, application)
server.serve_forever()
