from wsgiref.simple_server import make_server
from html import escape
import re

def get_schedule(environ):
    url_args = environ['web_api.url_args']
    if url_args:
        url_args_user = escape(url_args[0])
    else:
        url_args_user = ''
    return [url_args_user.encode()]

def not_found():
    return [b'invalid request']

url_dispatcher = [
    (r'get/schedule/([a-zA-Z0-9 ]+)/?$', get_schedule)
]

def web_api(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in url_dispatcher:
        match = re.search(regex, path)
        if match is not None:
            environ['web_api.url_args'] = match.groups()
            return callback(environ)
        else:
            return not_found()


if __name__ == '__main__':
    http_srv = make_server('localhost', 55555, web_api)
    http_srv.serve_forever()