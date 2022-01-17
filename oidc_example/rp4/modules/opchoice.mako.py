# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1639932697.593876
_enable_loop = True
_template_filename = 'htdocs/opchoice.mako'
_template_uri = 'opchoice.mako'
_source_encoding = 'utf-8'
_exports = []



def op_choice(op_list):
    #Creates a dropdown list of OpenID Connect providers
    element = "<select name=\"op\">"
    for name in op_list:
        element += "<option value=\"%s\">%s</option>" % (name, name)
    element += "</select>"
    return element


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        op_list = context.get('op_list', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n\r\n<html>\r\n<head>\r\n    <title>pyoidc RP</title>\r\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n    <!-- Bootstrap -->\r\n    <link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">\r\n    <link href="static/style.css" rel="stylesheet" media="all">\r\n\r\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\r\n    <!--[if lt IE 9]>\r\n    <script src="../../assets/js/html5shiv.js"></script>\r\n    <script src="../../assets/js/respond.min.js"></script>\r\n    <![endif]-->\r\n</head>\r\n<body>\r\n\r\n<!-- Static navbar -->\r\n<div class="navbar navbar-default navbar-fixed-top">\r\n    <div class="navbar-header">\r\n        <a class="navbar-brand" href="#">pyoidc RP</a>\r\n    </div>\r\n</div>\r\n\r\n<div class="container">\r\n    <!-- Main component for a primary marketing message or call to action -->\r\n    <div class="jumbotron">\r\n        <form class="form-signin" action="rp" method="get">\r\n            <h1>OP by UID</h1>\r\n\r\n            <h3>Chose the OpenID Connect Provider: </h3>\r\n\r\n            <p>From this list</p>\r\n            ')
        __M_writer(str(op_choice(op_list)))
        __M_writer('\r\n            <p> OR by providing your unique identifier at the OP. </p>\r\n            <input type="text" id="uid" name="uid" class="form-control" placeholder="UID" autofocus>\r\n            <p> OR by providing an issuer id</p>\r\n            <input type="text" id="issuer" name="issuer" class="form-control" placeholder="ISSUER">\r\n            <button class="btn btn-lg btn-primary btn-block" type="submit">Start</button>\r\n        </form>\r\n    </div>\r\n\r\n</div>\r\n<!-- /container -->\r\n<!-- jQuery (necessary for Bootstrap\'s JavaScript plugins) -->\r\n<script src="/static/jquery.min.1.9.1.js"></script>\r\n<!-- Include all compiled plugins (below), or include individual files as needed -->\r\n<script src="/static/bootstrap/js/bootstrap.min.js"></script>\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "htdocs/opchoice.mako", "uri": "opchoice.mako", "source_encoding": "utf-8", "line_map": {"16": 1, "26": 0, "32": 9, "33": 45, "34": 45, "40": 34}}
__M_END_METADATA
"""
