import shlex, subprocess, os.path, sys, logging

# constants
# RS => Return Status
RS_SUCCESS = "SUCCESS"
RS_FAILED = "FAILED"

log = logging.getLogger(__name__)

#----------------------------------------------------------------------
def _FUNC_NAME(back=0):
    return sys._getframe(back + 1).f_code.co_name

def _result(status, msg):
    return { "status": status, "msg": msg }

def run(cmd):
    try:
        args = shlex.split(cmd)
        p = subprocess.Popen(args)
        returncode = p.wait()
        if returncode == 0:
            r = _result(RS_SUCCESS, "")
    except Exception, e:
        r = _result(RS_FAILED, repr(e))

    log.info("%s(): %s => %s" % (_FUNC_NAME(1), cmd, repr(r)))
    return r

#----------------------------------------------------------------------
#http://code.google.com/p/cpkcrypto/
def gen_master_key():
    if os.path.exists(os.path.expanduser("~/.cpk/public_params")):
        r = _result(RS_FAILED, "public_params.der already imported!")
        log.info("%s(): => %s" % (_FUNC_NAME(), repr(r)))
        return r

    cmd = "%(cpkdir)s/cpk -import-param -in %(cpkdir)s/public_params.der" % config["pylons.paths"]
    return run(cmd)


