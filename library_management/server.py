import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import re

from log import logger

routers = []

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = route(self.path)
        self.send_response(response.response)
        self.send_header("Content-Type", "text/html;charset=utf-8")
        self.end_headers()
        self.wfile.write(str.encode(response.message))


class Response:
    def __init__(self, message, status_code=200):
        self.response = status_code
        self.message = message

def run_server(hostname='', port=9191):
    try:
        httpd = HTTPServer((hostname, port), RequestHandler)
        httpd.serve_forever()
        logger.debug(f'Running on {hostname}:{port}')
    except KeyboardInterrupt:
        logger.debug('\nCleaning Up. Exiting.')
        exit(123)

def router_add(route_url, view):
    routers.append((route_url, view))
    logger.debug(routers)

def route(url):
    for route in routers:
        re_url = route[0]
        logger.debug(re_url, url)
        matches = re.match(re_url, url)
        if matches:
            logger.debug(matches)
            logger.debug(matches.groupdict())
            return route[1](**matches.groupdict())
        else:
            logger.debug("It didnt match")


def view(name):
    return Response(f'<h1>hello {name}')


router_add(r'/view/(?P<name>(\w)+)', view)
