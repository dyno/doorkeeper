import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from doorkeeper.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UmController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/um.mako')
        # or, return a string
        return 'Hello World'
