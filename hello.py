#!/usr/local/bin/python

def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    result = '<br>'.join(env['QUERY_STRING'].split('&'))
    return [result]