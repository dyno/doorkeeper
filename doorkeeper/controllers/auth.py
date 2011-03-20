import logging
from hashlib import md5

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from doorkeeper.lib.base import BaseController, render

import doorkeeper.model as model

log = logging.getLogger(__name__)

class AuthController(BaseController):

    def display(self):
        if not session.get("user"):
            return render('/login.mako')
        else:
            return render('/main.mako')
    
    @jsonify
    def login(self):
        username = request.POST["username"]
        passwd = md5(request.POST["passwd"]).hexdigest()
        q = model.meta.Session.query(model.DKUser)
        user = q.get(username)
        if user.passwd == passwd:
            #cache user in session
            session["user"] = user
            session.save()
            return {"status" : "ok"}
        else:
            return {"status" : "failed"}

    def logout(self):
        session.clear()
        session.save()

