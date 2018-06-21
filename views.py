from microwf import App
from microwf.template import render
from microwf.response import Response
from microwf.view import View

from app import app


@app.route(r"/view/(?P<name>(\w)+)")
class HelloView(View):

    def get(self, name):
        return Response(f"Hello {name}")


@app.route(r"/hello/(?P<name>(\w)+)")
class HelloWorldView(View):

    def get(self, name, age=20):
        return render("templates/hello_world.html", context={"name": name, "age": age})
