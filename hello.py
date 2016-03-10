#!/usr/local/bin/python

def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    #with open('/home/box/web/log.log','a') as f:
    #    f.write(env['QUERY_STRING'])
    result = '<br>'.join(env['QUERY_STRING'].split('&'))
    return [env['QUERY_STRING']]
    return [result]
