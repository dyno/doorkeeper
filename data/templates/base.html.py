# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1300283371.978842
_template_filename=u'/home/hfu/pylons/doorkeeper/doorkeeper/templates/base.html'
_template_uri=u'/base.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\n<html>\n<head>\n<meta http-equiv="content-type" content="text/html; charset=utf-8">\n\n<style>\n</style>\n\n<link rel="stylesheet" type="text/css" href="/yui/3.3.0/cssbase/base-min.css">\n<link rel="stylesheet" type="text/css" href="/yui/3.3.0/cssreset/reset-min.css">\n<link rel="stylesheet" type="text/css" href="/yui/3.3.0/cssfonts/fonts-min.css">\n<link rel="stylesheet" type="text/css" href="/yui/3.3.0/cssgrids/grids-min.css">\n<link rel="stylesheet" type="text/css" href="/doorkeeper.css">\n</head>\n\n<body class="yui3-skin-sam">\n    <div class="yui3-u-1">\n\t<h1> ')
        # SOURCE LINE 19
        __M_writer(escape(_("whatever")))
        __M_writer(u' </h1>\n    </div>\n\n    ')
        # SOURCE LINE 22
        __M_writer(escape(self.body()))
        __M_writer(u'\n\n    <div class="yui3-u-1" id="footer">\n\t')
        # SOURCE LINE 25
        __M_writer(escape(_("foot copywhatever ")))
        __M_writer(u'\n    </div>\n</body>\n</html>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


