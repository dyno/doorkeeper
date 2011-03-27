import sys
from os.path import join, abspath, dirname, normpath
#sys.path.append(normalpath(join(dirname(__file__), "../")))

import logging
import hashlib
import random
import ConfigParser

from doorkeeper.model.meta import Session, Base
from doorkeeper.model import meta
from doorkeeper import model
from sqlalchemy import engine_from_config

log = logging.getLogger()
sur_names = []
given_names = []

def load_names():
    with open("surname_cn.txt") as f:
        for line in f:
            if not line.startswith("#") and line.strip():
                sur_names.append(line.split()[1].lower().replace("'", ""))

    with open("givenname_cn.txt") as f:
        for line in f:
            if not line.startswith("#") and line.strip():
                given_names.append(line.split()[1].lower().replace("'",""))

def setup_testing_db():
    cp = ConfigParser.ConfigParser()
    cp.read("../development.ini")
    config = {  "sqlalchemy.url":
                cp.get("app:main", "sqlalchemy.url", 0, {"here": normpath("%s/.." % dirname(abspath(__file__)))})
             }

    # Setup the SQLAlchemy database engine
    engine = engine_from_config(config, 'sqlalchemy.')
    model.init_model(engine)

    log.info("Create testing user accounts ...")
    random.seed("whatever")
    for i in range(0,100):
        sur_name = sur_names[random.randint(0, len(sur_names)-1)]
        given_name = given_names[random.randint(0, len(given_names)-1)]
        username = "%s.%s" % (sur_name, given_name)
        try:
            q = Session.query(model.DKUser)
            r = q.get(username)
            if not r:
                user = model.DKUser()
                user.username = username
                user.roles = ":".join(["", meta.ROLE_USER, ""])
                user.passwd = hashlib.md5("cpksecurity").hexdigest()
                user.master_email = "%s@cpksecurity.com" % username
                user.actived = True
                Session.add(user)
                Session.commit()
                log.info(" Account '%s' setup complete." % username)
            else:
                log.info("Account '%s' already setup." % username)
        except Exception, e:
            print e

if __name__ == "__main__":
    load_names()
    setup_testing_db()

