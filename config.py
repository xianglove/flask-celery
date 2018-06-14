# -*- coding: utf-8 -*-
import time


class Config():
    fresh_detail = {
        "msg": "成功",
        "success": "true",
        "data": {
            "collectionId": "7FRESH-DZGC-2674088",
            "containers": [{
                "containerNo": "EPP000510",
                "containerType": "2",
                "containerName": "箱子"
            }],
            "orderItems": [{
                "orderId": '6' + str(time.time()),
                "price": 209.68,
                "shippedQuantity": 13.00,
                "storeId": 131229,
                "storeName": "大族广场店",
                "volume": 19318000.000,
                "returnUrl": "http://tms-gateway.7fresh.com/api/tms/syncOrderStatus",
                "address": "上海市浦东新区乳山路93号",
                "customerLatitude": "31.229023",
                "customerLongitude": "121.517973",
                "customerName": "张昭君",
                "expectedArriveDate": 1517500800000,
                "expectedArrivePeriodTime": "15:00-17:00",
                "grossWeight": 4.80,
                "mobile": "a-TWU57HVkbN67r9b1WH3vLQ==",
                "mobileMask": "159****6909",
                "netWeight": 4.80
            },{
                "orderId": '6' + str(time.time()),
                "price": 209.68,
                "shippedQuantity": 13.00,
                "storeId": 131229,
                "storeName": "大族广场店",
                "volume": 19318000.000,
                "returnUrl": "http://tms-gateway.7fresh.com/api/tms/syncOrderStatus",
                "address": "上海市浦东新区乳山路93号",
                "customerLatitude": "31.229023",
                "customerLongitude": "121.517973",
                "customerName": "疾风剑豪",
                "expectedArriveDate": 1517500800000,
                "expectedArrivePeriodTime": "15:00-17:00",
                "grossWeight": 4.80,
                "mobile": "a-TWU57HVkbN67r9b1WH3vLQ==",
                "mobileMask": "159****6909",
                "netWeight": 4.80
            }],
            "totalQuantity": 13.00,
            "sourceId": 73753
        }
    }
