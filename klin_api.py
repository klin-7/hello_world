from urllib.parse import parse_qs
from wsgiref.simple_server import make_server


def web_api(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    output = b'fsdfsdf\n'
    for item in environ:
        print(item, ': ', environ[item], sep='')

    return [output]


if __name__ == '__main__':
    http_srv = make_server('localhost', 55555, web_api)
    http_srv.serve_forever()