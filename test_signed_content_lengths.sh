#!/bin/bash

# The frontend sees two requests to /firstGet,
# while Waitress sees a request to /firstGet
# and another one to /secondGet.

(printf 'GET http://localhost:6789/firstGet HTTP/1.1\r\n'\
'Content-Length: +53\r\n'\
'\r\n'\
'GET http://localhost:6789/firstGet HTTP/1.1\r\n'\
'Dummy: GET http://localhost:6789/secondGet HTTP/1.1\r\n'\
'\r\n'; sleep 1) | nc localhost 6789