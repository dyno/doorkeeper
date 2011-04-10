import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from doorkeeper.lib.base import BaseController, render
from doorkeeper.lib.util import pack_result, RS_SUCCESS, RS_FAILURE
import doorkeeper.model as model
from doorkeeper.model import meta

log = logging.getLogger(__name__)

class UmController(BaseController):
    def __before__(self):
        # Restrict access to SYSADMIN
        login_user = session.get("user")
        if not login_user:
            abort()
        if meta.ROLE_SYSADMIN not in login_user.roles:
            redirect("/")

    @jsonify
    def get_users(self, id):
        offset, size = map(int, id.split("&", 1)[0].split("-"))
        q = meta.Session.query(model.DKUser).offset(offset).limit(size)
        l = [(u.username, u.master_email) for u in q.all()]

        return pack_result(RS_SUCCESS, data=l)

    @jsonify
    def get_user_count(self):
        count = meta.Session.query(model.DKUser).count()
        return pack_result(RS_SUCCESS, data=count)

