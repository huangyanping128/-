import requests
import pytest
from common.login_info import login


@pytest.fixture(scope='function')
def login_fron():
    print("这是登录前置操作")
    s = requests.session()
    login(s)
    return s

@pytest.fixture(scope='function')
def unlogin_fron():
    print("这是不登录的前置操作")
    s = requests.session()
    h = {"Authorization": "Token sdsdsdsadsadsad32312"}
    s.headers.update(h)
    return s


# 测试修改个人中心接口
def test_update_info_01(login_fron):
    s = login_fron
    url = 'http://49.235.92.12:9000/api/v1/userinfo'
    body = {"name": "test",
            "sex": "M",
            "age": 20,
            "mail": "283340479@qq.com"}
    r = s.get(url, data=body)
    print(r.text)
    assert r.json()['msg'] == 'sucess!'
    assert r.json()['code'] == 0


#
#
def test_update_info_02(unlogin_fron):
    s = unlogin_fron
    s.headers.update({'token': '598b946261a6209f5d504fdd75e55ec9da4f4b17'})
    url = 'http://49.235.92.12:9000/api/v1/userinfo'
    body = {"name": "test",
            "sex": "M",
            "age": 20,
            "mail": "283340479@qq.com"}
    r = s.get(url, data=body)
    print(r.text)
    # assert r.json()['msg'] == 'sucess!'
    # assert r.json()['code'] == 0
