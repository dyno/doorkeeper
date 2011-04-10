import shlex, subprocess, os.path, sys, logging

from doorkeeper.lib.util import FUNC_NAME, pack_result, RS_SUCCESS, RS_FAILURE

log = logging.getLogger(__name__)

#----------------------------------------------------------------------
def run(cmd):
    try:
        args = shlex.split(cmd)
        p = subprocess.Popen(args)
        returncode = p.wait()
        if returncode == 0:
            r = pack_result(RS_SUCCESS)
    except Exception, e:
        r = pack_result(RS_FAILURE, message=repr(e))

    log.info("%s(): %s => %s" % (FUNC_NAME(1), cmd, repr(r)))
    return r

#----------------------------------------------------------------------
#http://code.google.com/p/cpkcrypto/
def gen_master_key():
    if os.path.exists(os.path.expanduser("~/.cpk/public_params")):
        r = pack_result(RS_FAILURE, "public_params.der already imported!")
        log.info("%s(): => %s" % (FUNC_NAME(), repr(r)))
        return r

    cmd = "%(cpkdir)s/cpk -import-param -in %(cpkdir)s/public_params.der" % config["pylons.paths"]
    return run(cmd)

