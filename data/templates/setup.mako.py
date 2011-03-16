# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1300290074.7229991
_template_filename='/home/hfu/pylons/doorkeeper/doorkeeper/templates/setup.mako'
_template_uri='/setup.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['body']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 87
        __M_writer(u'\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<div class="yui3-g" style="height:40em;">\n    <div class="yui3-u-1-5" >\n\t<div id="side" class="yui3-menu" role="menu">\n\t    <div class="yui3-menu-content">\n\t\t<ul class="first-of-type">\n\t\t    <li class="yui3-menuitem"><a class="yui3-menuitem-content">')
        # SOURCE LINE 9
        __M_writer(escape(_("System")))
        __M_writer(u'</a></li>\n\t\t    <li class="yui3-menuitem"><a class="yui3-menuitem-content">')
        # SOURCE LINE 10
        __M_writer(escape(_("User")))
        __M_writer(u'</a></li>\n\t\t    <li class="yui3-menuitem"><a class="yui3-menuitem-content">')
        # SOURCE LINE 11
        __M_writer(escape(_("Key")))
        __M_writer(u'</a></li>\n\t\t</ul>\n\t   </div>\n\t</div>\n    </div>\n\n    <div class="yui3-u-4-5">\n\t<div  id="content">\n\t    <ul>\n\t\t<li><a href="#tab_setup" class="tablabel"> ')
        # SOURCE LINE 20
        __M_writer(escape(_('System Initialization')))
        __M_writer(u' </a></li>\n\t    </ul>\n\n\t    <div>\n\t\t<div id="tab_setup">\n\t\t    <form id="initform" action="/setup/init" method="post">\n\t\t\t<div>\n\t\t\t    <label for="admin_passwd">')
        # SOURCE LINE 27
        __M_writer(escape(_("Administrator Password")))
        __M_writer(u' : &nbsp;</label>\n\t\t\t    <input id="admin_passwd" name="admin_passwd" type="text"/>\n\t\t\t</div>\n\t\t\t<div>\n\t\t\t    <label for="admin_passwd2">')
        # SOURCE LINE 31
        __M_writer(escape(_("Repeat Password")))
        __M_writer(u' : &nbsp;</label>\n\t\t\t    <input id="admin_passwd2" name="admin_passwd" type="text"/>\n\t\t\t</div>\n\t\t\t<div class="submit">\n\t\t\t    <label for="submit">&nbsp;</label>\n\t\t\t    <button type="button" id="submit">')
        # SOURCE LINE 36
        __M_writer(escape(_("Submit")))
        __M_writer(u'</button>\n\t\t\t</div>\n\t\t    </form>\n\t\t</div>\n\t    </div>\n        </div>\n    </div>\n</div>\n\n<script src="/yui/3.3.0/yui/yui-min.js"> </script>\n<script type="text/javascript">\n//left menu\nYUI({ filter: \'raw\' }).use("node-menunav", function(Y) {\n    var menu = Y.one("#side");\n    menu.plug(Y.Plugin.NodeMenuNav);\n    menu.get("ownerDocument").get("documentElement").removeClass("yui3-loading");\n});\n\n//right tab panel\nYUI({ filter: \'raw\' }).use("yui", "tabview", function(Y) {\n    var tabview = new Y.TabView({srcNode:\'#content\'});\n    tabview.render();\n});   \n\n//ajax\nYUI({filter: "raw"}).use("io-form", function(Y) {\n    var onSuccess = function(id, response, args) {\n\talert(response.responseText);\n    };\n\n    var onFailure = function(id, response, args) {\n\talert("sorry!");\n    };\n\n    var onClick = function(e) {\n\tvar cfg = {\n\t    method: "POST",\n\t    form: {\n\t\tid: "initform",\n\t    },\n\t};\n\n        Y.io(\'/setup/init\', cfg);\n        Y.on(\'io:success\', onSuccess, this);\n        Y.on(\'io:failure\', onFailure, this);\n    };\n\n    Y.on("click", onClick, "#submit", this, true);\n}); \n</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


