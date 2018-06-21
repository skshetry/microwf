from .router import Router
from .response import Response
from .utils import applications, GET, POST
from .log import logger

from http import HTTPStatus


class App:

    def __init__(self, name):
        self.name = name
        self.router = Router()
        logger.debug(f"{self.name}, {self.router}")

        applications.append(self)

    def route(self, endpoint):

        def wrapper(view):
            self.router.add(endpoint, view)
            logger.debug(f"Route added to {view}")
            return view

        return wrapper

    def return_view(self, path, method):
        logger.debug(f"routerroutes: {self.router.routes}")
        matches = self.router.match(path)
        logger.debug(matches)
        if matches:
            view = matches[0]
            kargs = matches[1]
            if method == GET:
                return view().get(**kargs)

            elif method == POST:
                return view().post(**kargs)

        else:
            return Response(
                "No view matches the path.", status_code=HTTPStatus.NOT_FOUND
            )
