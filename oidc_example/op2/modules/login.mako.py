# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1639096897.1578672
_enable_loop = True
_template_filename = 'htdocs/login.mako'
_template_uri = 'login.mako'
_source_encoding = 'utf-8'
_exports = ['add_js']


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
    return runtime._inherit_from(context, 'root.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        logo_uri = context.get('logo_uri', UNDEFINED)
        acr = context.get('acr', UNDEFINED)
        password = context.get('password', UNDEFINED)
        policy_uri = context.get('policy_uri', UNDEFINED)
        tos_uri = context.get('tos_uri', UNDEFINED)
        title = context.get('title', UNDEFINED)
        submit_text = context.get('submit_text', UNDEFINED)
        passwd_title = context.get('passwd_title', UNDEFINED)
        login = context.get('login', UNDEFINED)
        action = context.get('action', UNDEFINED)
        login_title = context.get('login_title', UNDEFINED)
        query = context.get('query', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<head>\r\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n    <!-- Bootstrap -->\r\n    <link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">\r\n    <link href="static/style.css" rel="stylesheet" media="all">\r\n</head>\r\n<body>\r\n    <div class="container">\r\n        <div class="header">\r\n            <h1><a href="/">')
        __M_writer(str(title))
        __M_writer('</a></h1>\r\n        </div>\r\n        <div class="login_form" class="block">\r\n            <form action="')
        __M_writer(str(action))
        __M_writer('" method="post" class="login form">\r\n                <input type="hidden" name="query" value="')
        __M_writer(str(query))
        __M_writer('"/>\r\n                <input type="hidden" name="acr_values" value="')
        __M_writer(str(acr))
        __M_writer('"/>\r\n                <table>\r\n                    <tr>\r\n                        <td>')
        __M_writer(str(login_title))
        __M_writer('</td>\r\n                        <td><input type="text" name="login" value="')
        __M_writer(str(login))
        __M_writer('" placeholder="id"/></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td>')
        __M_writer(str(passwd_title))
        __M_writer('</td>\r\n                        <td><input type="password" name="password" placeholder="pass"\r\n                        value="')
        __M_writer(str(password))
        __M_writer('"/></td>\r\n                    </tr>\r\n                    <tr>\r\n                        </td>\r\n                        <td><input type="submit" name="form.commit"\r\n                                value="')
        __M_writer(str(submit_text))
        __M_writer('"/></td>\r\n                    </tr>\r\n                </table>\r\n            </form>\r\n')
        if logo_uri:
            __M_writer('                <img src="')
            __M_writer(str(logo_uri))
            __M_writer('" alt="Client logo">\r\n')
        if policy_uri:
            __M_writer('                <a href="')
            __M_writer(str(policy_uri))
            __M_writer('"><strong>Client&#39;s Policy</strong></a>\r\n')
        if tos_uri:
            __M_writer('                <a href="')
            __M_writer(str(tos_uri))
            __M_writer('"><strong>Client&#39;s Terms of Service</strong></a>\r\n')
        __M_writer('        </div>\r\n    </div>\r\n</body>\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_add_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\r\n    <script type="text/javascript">\r\n        $(document).ready(function() {\r\n            bookie.login.init();\r\n        });\r\n    </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "htdocs/login.mako", "uri": "login.mako", "source_encoding": "utf-8", "line_map": {"27": 0, "44": 1, "45": 11, "46": 11, "47": 14, "48": 14, "49": 15, "50": 15, "51": 16, "52": 16, "53": 19, "54": 19, "55": 20, "56": 20, "57": 23, "58": 23, "59": 25, "60": 25, "61": 30, "62": 30, "63": 34, "64": 35, "65": 35, "66": 35, "67": 37, "68": 38, "69": 38, "70": 38, "71": 40, "72": 41, "73": 41, "74": 41, "75": 43, "76": 53, "82": 47, "86": 47, "92": 86}}
__M_END_METADATA
"""
