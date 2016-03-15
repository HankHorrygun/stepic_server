#!/usr/local/bin/python

def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [ '%s\n' %x for x in env['QUERY_STRING'].split('&') ]
