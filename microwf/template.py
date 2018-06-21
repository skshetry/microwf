import re
from .response import Response
from .log import logger
from http import HTTPStatus

temp_context = {}


def replace_with_context(matches):
    logger.debug(matches)
    groups = matches.groups()
    logger.debug(groups)
    return str(temp_context[groups[0]])


def render(path_to_render, context=None):
    global temp_context
    temp_context = context
    template_file = open(path_to_render)
    template = template_file.read()
    template_file.close()
    return Response(
        re.sub(r"{{(?P<var>(\w)+)}}", replace_with_context, template),
        status_code=HTTPStatus.OK,
    )
