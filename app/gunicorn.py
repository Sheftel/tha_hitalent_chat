bind = '0.0.0.0:8000'
wsgi_app = 'config.wsgi'


keepalive = 5

graceful_timeout = 15

accesslog = '/var/log/gunicorn.access.log'
errorlog = '/var/log/gunicorn.error.log'
loglevel = 'info'