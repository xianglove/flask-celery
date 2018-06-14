# -*- coding: UTF-8 -*-

import time
from flask import Flask
from flask import jsonify, request
from config import Config

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/tms/syncCollectionStatus/')
def sync_status():
    response = {
        "msg": "成功",
        "success": "true"
    }
    return jsonify(response)


@app.route('/api/tms/decrypt/')
def decrypt():
    response = {
        "msg": "成功",
        "success": "true",
        "data": "15210910321"
    }

    return jsonify(response)


@app.route('/api/tms/collectionStatus/')
def get_status():
    response = {
        "msg": "成功",
        "success": "true",
        "status": 1
    }
    return jsonify(response)


@app.route('/api/tms/collection/')
def get_detail():
    collection_id = request.args.get('collectionId')
    config = Config()
    result = config.fresh_detail
    result['data']['collectionId'] = collection_id
    result['data']['orderItems'][0]['orderId'] = '6' + str(int(time.time()))
    result['data']['orderItems'][1]['orderId'] = '7' + str(int(time.time()))

    return jsonify(result)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5002)
