import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from doorkeeper.lib.base import BaseController, render

log = logging.getLogger(__name__)

class LoginController(BaseController):

    def index(self):
        # Return a rendered template
        return render('/login.mako')

