import requests
import pytest
import os
from common.read_yaml import readyml
# test_data = [
#     [{"username": "test", "password": "123456"}, {'code': 0, 'msg': 'login success!'}],
#     [{"username": "test1", "password": "32323"}, {'code': 3003, 'msg': '账号或密码不正确'}]
# ]
yamlPath = 'D:/xiaoxiao/learn/test_data.yaml'
test_data=readyml(yamlPath)['body']
print(test_data)


@pytest.mark.parametrize("test_input,expect", test_data)
def test_login(test_input, expect):
    url = 'http://49.235.92.12:9000/api/v1/login'
    body = test_input
    print(test_input)

    r = requests.post(url, json=body)
    assert r.json()["code"] == expect["code"]
    assert r.json()["msg"] == expect["msg"]


if __name__ == '__main__':
    test_login()
