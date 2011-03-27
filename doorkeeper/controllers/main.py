import logging
import sys, os.path

from pylons import request, response, session, tmpl_context as c, url, config
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from doorkeeper.lib.base import BaseController, render
import doorkeeper.model.cpk as cpk

log = logging.getLogger(__name__)

#----------------------------------------------------------------------
class MainController(BaseController):

    def index(self):
        if not session.get("user"):
            return render("/login.mako")
        else:
            return render("/main.mako")

    @jsonify
    def do(self):
        if not session.get("user"):
            raise Exception("not logged in!")

        if request.POST["action"] == "gen_master_key":
            return cpk.gen_master_key()

