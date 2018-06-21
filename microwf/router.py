import re

from .log import logger


class Router:

    def __init__(self):
        self.routes = []

    def add(self, endpoint, view):
        logger.debug(f"{self.routes}")
        self.routes.append((endpoint, view))
        logger.debug(f"{self.routes}")

    def match(self, path):
        logger.debug(f"routes: {self.routes}")
        for route in self.routes:
            re_path = route[0]
            logger.debug(f"{re_path}, {path}")
            matches = re.match(re_path, path)
            if matches:
                logger.debug(matches)
                logger.debug(matches.groupdict())
                return route[1], matches.groupdict()

            else:
                logger.debug("It didnt match")
