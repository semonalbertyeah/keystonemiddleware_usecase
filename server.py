# -*- coding:utf-8 -*-

from waitress import serve


def get_server(global_config, **config):
    port = int(config['port'])
    host = config['host']

    def serve_forever(app):
        serve(app, host=host, port=port)
    return serve_forever


