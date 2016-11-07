# -*- coding:utf-8 -*-

import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route(r'/dump/', methods=['GET'])
def dump():
    print 'headers:', json.dumps(dict(request.headers), indent=4)
    print 'cookies:', json.dumps(dict(request.cookies), indent=4)
    print 'query string:', json.dumps(dict(request.args), indent=4)
    print 'body:'
    print repr(request.data)
    
    return jsonify({
        'headers': dict(request.headers),
        'cookies': dict(request.cookies),
        'query_string': dict(request.args),
        'body': repr(request.data)
    })

def get_app(default, **kwargs):
    print 'get_app:'
    print 'default:', default
    print 'kwargs:', kwargs
    global app
    return app




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8020, debug=True, threaded=True)


