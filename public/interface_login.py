#coding=utf-8

import requests
import json

test_url = "https://release-api.patozon.net"

def login_test_brand(store_id):
    '''登录预发布环境会员系统'''
    url = test_url + "/api/permission/user/login"
    data = {"username":"sunny_hong","password":"123456!@#","store_id":store_id}
    r = requests.post(url,data)
    result = r.text
    print(result)
    assert json.loads(result)["code"] == 1
    return json.loads(result)["data"]["token"]


def delete_email(store_id,email):
    """删除账号"""
    token = login_test_brand(store_id)
    url = test_url + "/api/admin/customer/forceDelete"
    data = {"store_id": store_id, "operator": "sunny_hong", "token": token, "account": email}
    r = requests.post(url, data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    # assert  json.loads(result)["data"][0]["account"] == email
    return "delete email success"


if __name__ == '__main__':
    delete_email(1,"kstgac61408@chacuo.net")