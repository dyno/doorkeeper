import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from doorkeeper.lib.base import BaseController, render

log = logging.getLogger(__name__)

class MainController(BaseController):

    def index(self):
        if not session.get("user"):
            return render("/login.mako")
        else:
            return render("/main.mako")
