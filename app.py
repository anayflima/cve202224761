## PRÉ REQUISITOS - instalar com
# python3 install.py

## RODAR COM:
# waitress-serve --port=6789 request:app

from flask import Flask, request
from waitress import serve

app = Flask(__name__)
# app.run(host = '0.0.0.0')

@app.route('/testeget')
def query_example():
    return 'Recebeu o Teste Get\n'

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
    # serve(app, host='0.0.0.0', port=5000)
    # run app in debug mode on port 5000
    # app.run(debug=False, port=5000)


'''
TESTES:

Rodar em um outro terminal:

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

Saída:

*na versão antiga:*

HTTP/1.1 200 OK
Content-Length: 20
Content-Type: text/html; charset=utf-8
Date: Sat, 07 May 2022 15:04:51 GMT
Server: waitress

Recebeu o Teste Get
HTTP/1.1 200 OK
Content-Length: 20
Content-Type: text/html; charset=utf-8
Date: Sat, 07 May 2022 15:04:51 GMT
Server: waitress

Recebeu o Teste Get


*na versão nova:*

HTTP/1.1 400 Bad Request
Connection: close
Content-Length: 65
Content-Type: text/plain
Date: Sat, 07 May 2022 15:01:25 GMT
Server: waitress

Bad Request

Invalid chunk extension


TESTES:

Rodar em um outro terminal:

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

Saída:

*na versão antiga:*

HTTP/1.1 200 OK
Content-Length: 20
Content-Type: text/html; charset=utf-8
Date: Sat, 07 May 2022 15:04:51 GMT
Server: waitress

Recebeu o Teste Get
HTTP/1.1 200 OK
Content-Length: 20
Content-Type: text/html; charset=utf-8
Date: Sat, 07 May 2022 15:04:51 GMT
Server: waitress

Recebeu o Teste Get


*na versão nova:*

HTTP/1.1 400 Bad Request
Connection: close
Content-Length: 65
Content-Type: text/plain
Date: Sat, 07 May 2022 15:01:25 GMT
Server: waitress

Bad Request

Invalid chunk extension


'''

