# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1638269422.543317
_enable_loop = True
_template_filename = 'htdocs/opresult.mako'
_template_uri = 'opresult.mako'
_source_encoding = 'utf-8'
_exports = []



from html import entities as htmlentitydefs
import re

# this pattern matches substrings of reserved and non-ASCII characters
pattern = re.compile(r"[&<>\"\x80-\xff]+")

# create character map
entity_map = {}

for i in range(256):
    entity_map[chr(i)] = "&#%d;" % i

for entity, char in htmlentitydefs.entitydefs.items():
    if char in entity_map:
        entity_map[char] = "&%s;" % entity

def escape_entity(m, get=entity_map.get):
    return "".join(map(get, m.group()))

def escape(string):
    return pattern.sub(escape_entity, string)

def create_result(userinfo, user_id, id_token):
    """
        Creates a display of user information.
        """
    element = "<h3>You have successfully authenticated!</h3>"
    if id_token:
      element += '<h3>With the following authentication information</h3>'
      for key, value in id_token.items():
          element += "<div class='row'>"
          element += "<div class='col-md-3'>" +  escape(str(key)) + "</div>"
          element += "<div class='col-md-7'>" + escape(str(value)) + "</div>"
          element += "</div>"
    if user_id:
      element += '<h3>And are now known to the RP as:</h3>'
      element += '<i>'+userid+'</i>'
    if userinfo:
      element += '<h3>With the following user information</h3>'
      for key, value in userinfo.items():
          element += "<div class='row'>"
          element += "<div class='col-md-3'>" +  escape(str(key)) + "</div>"
          element += "<div class='col-md-7'>" + escape(str(value)) + "</div>"
          element += "</div>"
    return element


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        userinfo = context.get('userinfo', UNDEFINED)
        user_id = context.get('user_id', UNDEFINED)
        check_session_iframe_url = context.get('check_session_iframe_url', UNDEFINED)
        id_token = context.get('id_token', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n\r\n')
        __M_writer('\r\n\r\n<html>\r\n<head>\r\n    <title>pyoidc RP</title>\r\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n    <!-- Bootstrap -->\r\n    <link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">\r\n    <link href="static/style.css" rel="stylesheet" media="all">\r\n\r\n    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\r\n    <!--[if lt IE 9]>\r\n    <script src="../../assets/js/html5shiv.js"></script>\r\n    <script src="../../assets/js/respond.min.js"></script>\r\n    <![endif]-->\r\n</head>\r\n<body>\r\n\r\n<!-- Static navbar -->\r\n<div class="navbar navbar-default navbar-fixed-top">\r\n    <div class="navbar-header">\r\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n        </button>\r\n        <a class="navbar-brand" href="#">pyoidc RP</a>\r\n    </div>\r\n    <div class="navbar-collapse collapse">\r\n        <ul class="nav navbar-nav">\r\n        </ul>\r\n        <ul class="nav navbar-nav navbar-right">\r\n            <li><a href="logout">Logout</a></li>\r\n        </ul>\r\n    </div>\r\n    <!--/.nav-collapse -->\r\n</div>\r\n\r\n<div class="container">\r\n    <!-- Main component for a primary marketing message or call to action -->\r\n    <div class="jumbotron">\r\n        <h1>OP result</h1>\r\n        ')
        __M_writer(str(create_result(userinfo, user_id, id_token)))
        __M_writer('\r\n    </div>\r\n\r\n</div>\r\n<!-- /container -->\r\n\r\n\r\n')
        if check_session_iframe_url is not UNDEFINED:
            __M_writer('    <iframe id="rp_iframe" src="/session_iframe" hidden></iframe>\r\n    <iframe id="op_iframe" src="')
            __M_writer(str(check_session_iframe_url))
            __M_writer('" hidden></iframe>\r\n')
        __M_writer('\r\n\r\n<!-- jQuery (necessary for Bootstrap\'s JavaScript plugins) -->\r\n<script src="/static/jquery.min.1.9.1.js"></script>\r\n<!-- Include all compiled plugins (below), or include individual files as needed -->\r\n<script src="/static/bootstrap/js/bootstrap.min.js"></script>\r\n\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "htdocs/opresult.mako", "uri": "opresult.mako", "source_encoding": "utf-8", "line_map": {"16": 3, "64": 0, "73": 1, "74": 49, "75": 91, "76": 91, "77": 98, "78": 99, "79": 100, "80": 100, "81": 102, "87": 81}}
__M_END_METADATA
"""
