"""Setup the doorkeeper application"""
import logging
import hashlib

import pylons.test

from doorkeeper.config.environment import load_environment
from doorkeeper.model.meta import Session, Base
import doorkeeper.model as model

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup doorkeeper here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    log.info("Initialize database ...")
    Base.metadata.create_all(bind=Session.bind, checkfirst=True)

    #create default privileges
    log.info("Populate default privileges ...")
    log.info("nothing here...")
    log.info("Populate default privileges done.")

    #create default roles
    log.info("Populate default roles ...")
    q = Session.query(model.DKRole)
    if not q.all():
        records = [ model.DKRole(model.meta.ROLE_SYSADMIN),
                model.DKRole(model.meta.ROLE_USER),
        ]
        Session.add_all(records)
        Session.commit()
        log.info("Populate default roles done.")
    else:
        log.info("Roles already exist.")


    log.info("Populate default roles done.")

    #create default system parameters
    log.info("Populate default system parameters ...")
    q = Session.query(model.DKSystem)
    if not q.all():
        records = [ model.DKSystem("master_key_status", model.meta.SS_SERVICE_NO_KEY),
                model.DKSystem("service_key_gen_status", model.meta.SS_SERVICE_NOT_AVAIL),
                model.DKSystem("service_key_revoke_status", model.meta.SS_SERVICE_NOT_AVAIL),
        ]
        Session.add_all(records)
        Session.commit()
        log.info("Populate default system parameters done.")
    else:
        log.info("System parameters exists.")

    #create default admin account
    log.info("Create default admin account ...")
    q = Session.query(model.DKUser)
    r = q.get("sysadmin")
    if not r:
        user = model.DKUser()
        user.username = "sysadmin"
        user.roles = ":".join(["", model.meta.ROLE_SYSADMIN, ""])
        user.passwd = hashlib.md5("sysadmin").hexdigest()
        user.master_email = "sysadmin@example.com"
        user.actived = True
        Session.add(user)
        Session.commit()
        log.info("Admin account setup complete.")
    else:
        log.info("Admin account already setup.")

