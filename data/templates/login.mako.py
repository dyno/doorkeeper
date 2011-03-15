# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1300175017.263834
_template_filename='/home/hfu/pylons/doorkeeper/doorkeeper/templates/login.mako'
_template_uri='/login.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\n"http://www.w3.org/TR/html4/strict.dtd">\n<head>\n<style type="text/css">\nbody {\n  margin:0;\n  padding:0;\n}\n</style>\n\n<link type="text/css" rel="stylesheet" href="/yui/3.3.0/cssfonts/fonts-min.css">\n<script type="text/javascript" src="/yui/3.3.0/yui/yui-min.js"></script>\n\n<style id="yui3-style-overrides">\n  #main #example-canvas .yui3-tabview .yui3-tab-selected a {\n  color:white;\n}\n</style>\n</head>\n\n<body class="yui3-skin-sam  yui-skin-sam">\n<div id="panel">\n    <ul>\n        <li><a href="#login">Login</a></li>\n        <li><a href="#register">Register</a></li>\n    </ul>\n    <div>\n        <div id="login">\n            <p>login content</p>\n        </div>\n\n        <div id="register">\n            <p>register content</p>\n        </div>\n    </div>\n</div>\n\n<div id="loginDialog">\n<div class="hd">Login</div>\n  <div class="bd">\n     <form method="POST" action="/login">\n       <div class="smallTitle">Welcome to the Xxxxxx Management System.</div>\n       <br/>\n          <div class="smallText">\n          <table cellpadding="0" cellspacing="0" border="0">\n          <tr>\n   <td style="width: 80px"><label for="username">Name:</label></td>\n   <td><input type="text" name="username" class="textBox" /></td>\n          </tr>\n          <tr>\n   <td><label for="password">Password:</label></td>\n   <td><input type="password" name="password" class="textBox" /></td>\n          </tr>\n          <tr>\n   <td colspan="2"><div id="loginError">Invalid login.</div></td>\n          </tr>\n          </table>\n       </div>\n    </form>\n  </div>\n</div>\n\n</body>\n\n<script type="text/javascript">\nYUI({ filter: \'raw\' }).use("yui", "tabview", function(Y) {\n    var tabview = new Y.TabView({srcNode:\'#panel\'});\n    tabview.render();\n});\n\nvar handleLogin = function() {\n   this.submit();\n};\n            \nvar handleLoginSuccess = function(o) {\n    if (o.responseText == "success") {\n       getListings();\n    } else {\n       Initialize(true);\n    }\n};\n\nvar handleLoginFailure = function(o) {\n    alert("Submission failed: " + o.status);\n};\n\n// Instantiate the Dialog\nvar loginDialog = new YAHOO.widget.Dialog("loginDialog", \n{ \n    width : "340px",\n    fixedcenter : true,\n    visible : false, \n    constraintoviewport : true,\n    draggable : true,\n    buttons : [ { text:"Login", handler:handleLogin, isDefault:true }]\n} );\n       \nloginDialog.callback = { success: handleLoginSuccess,\n                         failure: handleLoginFailure };\n\t\t\t   \n// Validate the entries in the form to require that both first and last name are entered\nloginDialog.validate = function() {\n    var data = this.getData();\n    if (data.username == "" || data.password == "") {\n\talert("Please enter a username and password.");\n\treturn false;\n    } else {\n\treturn true;\n    }\n};\n\n</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


