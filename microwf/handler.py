from http.server import HTTPServer, BaseHTTPRequestHandler

from .log import logger
from .utils import get_application, GET, POST


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        app = get_application()
        response = app.return_view(path=self.path, method=GET)
        logger.debug(app)
        logger.debug(response)
        self.send_response(response.response)
        self.send_header("Content-Type", "text/html;charset=utf-8")
        self.end_headers()
        self.wfile.write(str.encode(response.message))


# def routes(endpoint):
#     def wrapper(view):
#         router_add(endpoint, view)
#         return view
#     return wrapper


# def router_add(route_url, view):
#     routers.append((route_url, view))
#     logger.debug(routers)

# def route(url):
#     for route in routers:
#         re_url = route[0]
#         logger.debug(f'{re_url} {url}')
#         matches = re.match(re_url, url)
#         if matches:
#             logger.debug(matches)
#             logger.debug(matches.groupdict())
#             return route[1](**matches.groupdict())
#         else:
#             logger.debug("It didnt match")

# @routes(r'/view/(?P<name>(\w)+)')
# def view(name):
#     return Response(f'<h1>hello {name}')

# router_add(r'/view/(?P<name>(\w)+)', view)
