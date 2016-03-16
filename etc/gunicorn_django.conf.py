CONFIG = {
    'working_dir': '/home/box/web/ask/',
    'args': ( '--bind=0.0.0.0:8000', 
              '--env DJANGO_SETTINGS_MODULE=ask.settings'
              'ask:wsgi', ),
}
