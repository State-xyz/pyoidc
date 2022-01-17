# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1639932896.3136458
_enable_loop = True
_template_filename = 'htdocs/operror.mako'
_template_uri = 'operror.mako'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        error = context.get('error', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n\r\n<html>\r\n<head>\r\n    <title>pyoidc RP</title>\r\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n    <!-- Bootstrap -->\r\n    <link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">\r\n    <link href="static/style.css" rel="stylesheet" media="all">\r\n\r\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\r\n    <!--[if lt IE 9]>\r\n    <script src="../../assets/js/html5shiv.js"></script>\r\n    <script src="../../assets/js/respond.min.js"></script>\r\n    <![endif]-->\r\n</head>\r\n<body>\r\n\r\n<!-- Static navbar -->\r\n<div class="navbar navbar-default navbar-fixed-top">\r\n    <div class="navbar-header">\r\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n        </button>\r\n        <a class="navbar-brand" href="#">pyoidc RP</a>\r\n    </div>\r\n    <div class="navbar-collapse collapse">\r\n        <ul class="nav navbar-nav">\r\n        </ul>\r\n        <ul class="nav navbar-nav navbar-right">\r\n            <li><a href="logout">Logout</a></li>\r\n        </ul>\r\n    </div>\r\n    <!--/.nav-collapse -->\r\n</div>\r\n\r\n<div class="container">\r\n    <!-- Main component for a primary marketing message or call to action -->\r\n    <div class="jumbotron">\r\n        <h1>OP result</h1>\r\n\r\n        <p>You have failed to connect to the designated OP with the message:</p>\r\n\r\n        <p>')
        __M_writer(str(error))
        __M_writer('</p>\r\n    </div>\r\n\r\n</div>\r\n<!-- /container -->\r\n<!-- jQuery (necessary for Bootstrap\'s JavaScript plugins) -->\r\n<script src="/static/jquery.min.1.9.1.js"></script>\r\n<!-- Include all compiled plugins (below), or include individual files as needed -->\r\n<script src="/static/bootstrap/js/bootstrap.min.js"></script>\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "htdocs/operror.mako", "uri": "operror.mako", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 46, "24": 46, "30": 24}}
__M_END_METADATA
"""
