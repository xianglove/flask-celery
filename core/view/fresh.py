# -*- coding: utf-8 -*-
from flask import jsonify, request
from core import app
from core.const.data_config import Config
import time


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/tms/syncCollectionStatus', methods=['GET'])
def sync_status():
    response = {
        "msg": "成功",
        "success": True
    }
    return jsonify(response)


@app.route('/api/tms/decrypt', methods=['GET'])
def decrypt():
    response = {
        "msg": "成功",
        "success": True,
        "data": "15210910321"
    }

    return jsonify(response)


@app.route('/api/tms/collectionStatus', methods=['GET'])
def get_status():
    response = {
        "msg": "成功",
        "success": True,
        "status": 0
    }
    return jsonify(response)


@app.route('/api/tms/collection', methods=['GET'])
def get_detail():
    collection_id = request.args.get('collectionId')
    config = Config()
    result = config.fresh_detail
    result['data']['collectionId'] = collection_id
    result['data']['orderItems'][0]['orderId'] = '6' + str(int(time.time()))
    result['data']['orderItems'][1]['orderId'] = '7' + str(int(time.time()))

    return jsonify(result)

