## REQUIREMENTS
# python3 install.py

## TO RUN:
# python3 app.py

from flask import Flask, request
from waitress import serve

app = Flask(__name__)

@app.route('/firstGet')
def firstGet():
    # print(request.json)
    return 'This is the response for the FIRST get:\n' + request.data.decode("utf-8") + '\n\n'

@app.route('/secondGet')
def secondGet():
    return 'This is the response for the SECOND get:\n' + request.data.decode("utf-8") + '\n\n'

@app.route('/thirdGet')
def thirdGet():
    return 'This is the response for the THIRD get:\n' + request.data.decode("utf-8") + '\n\n'

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=6789)