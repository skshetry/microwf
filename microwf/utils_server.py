from http.server import HTTPServer
from .handler import RequestHandler
from .log import logger


def run_server(hostname="", port=9191):
    try:
        httpd = HTTPServer((hostname, port), RequestHandler)
        httpd.serve_forever()
        logger.debug(f"Running on {hostname}:{port}")
    except KeyboardInterrupt:
        logger.debug("\nCleaning Up. Exiting.")
