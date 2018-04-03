from flask import Flask, request, jsonify
from random import randint
from time import time

app = Flask(__name__)

def generate_client_id():
    return "{0}.{1}".format(randint(100000000,999999999), int(time()))

def generate_datalayer_push(cid): 
    return """
        window.dataLayer = [] || window.dataLayer;
        window.dataLayer.push({
            clientId: '%s',
            event: 'setProxyClientId'
        })
    """ % cid  

@app.route('/getclientid')
def get_client_id():
    if '_ga' in request.cookies:
        client_id = request.cookies.get('_ga')
    else:
        client_id = generate_client_id()
    
    return generate_datalayer_push(client_id)

if __name__ == '__main__':
    app.run(debug = True)   