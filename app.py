## REQUIREMENTS
# python3 install.py

## TO RUN:
# python3 app.py

from flask import Flask, request
from waitress import serve

app = Flask(__name__)

@app.route('/firstGet')
def firstGet():
    return 'This is the payload of the FIRST get:\n\n' + request.data.decode("utf-8") + '\n\n'

@app.route('/secondGet')
def secondGet():
    return 'This is the payload of the SECOND get:\n\n' + request.data.decode("utf-8") + '\n\n'

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=6789)