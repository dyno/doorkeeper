import logging
from hashlib import md5

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from doorkeeper.lib.base import BaseController, render
from doorkeeper.lib.util import FUNC_NAME, pack_result, RS_SUCCESS, RS_FAILURE

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
            return pack_result(RS_SUCCESS)
        else:
            return pack_result(RS_FAILURE)

    @jsonify
    def register(self):
        user = model.DKUser()

        user.username = request.POST["username"]
        user.passwd = md5(request.POST["passwd"]).hexdigest()
        user.master_email = request.POST["email"]
        user.phone_mobile = request.POST["phone_mobile"]
        user.phone_office = request.POST["phone_office"]
        user.phone_home = request.POST["phone_home"]
        user.org = request.POST["org"]
        user.title = request.POST["title"]
        user.addr = request.POST["addr"]

        session = model.meta.Session
        session.add(user)
        session.commit()
        return pack_result(RS_SUCCESS)

    def logout(self):
        session.clear()
        session.save()

