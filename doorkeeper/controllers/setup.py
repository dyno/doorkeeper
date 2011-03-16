import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from doorkeeper.lib.base import BaseController, render

log = logging.getLogger(__name__)

class SetupController(BaseController):

    def index(self):
        return render('/setup.mako')

    def init(self):
        print request.params["admin_passwd"]
        return "your master secret: %s" % request.params["admin_passwd"]
