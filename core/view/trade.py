# -*- coding: utf-8 -*-
# Author: xiaxiang
# Datetime: 19/5/21 下午5:17
from flask import jsonify, request
from core import app


@app.route('/trade/getRefundResult/', methods=['GET'])
def get_refund_result():
    data = {
        'code': '0',
        'result': {
            'failFinal': True
        }
    }

    return jsonify(data)


@app.route('/trade/refundOfflineFinish', methods=['POST'])
def refund_offline():

    return jsonify({'code': 0})