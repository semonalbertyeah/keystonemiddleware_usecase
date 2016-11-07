# -*- coding:utf-8 -*-

import os,sys
from paste.deploy import loadapp, loadserver

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, CUR_DIR)

wsgi_app = loadapp('config:%s' % os.path.join(CUR_DIR, 'config.ini'))
print 'app:', wsgi_app

print ''

wsgi_server = loadserver('config:%s' % os.path.join(CUR_DIR, 'config.ini'))
print 'server:', wsgi_server


if __name__ == '__main__':
    wsgi_server(wsgi_app)



