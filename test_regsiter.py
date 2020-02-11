import requests
from common.connect_mysql import execute_sql
import pytest

s = requests.session()


@pytest.fixture(scope="function")
def delete_user():
    """先删除已经注册的用户数据"""
    delete_sql = 'DELETE  from auth_user where username="小晓的筱";'
    execute_sql(delete_sql)


def test_regsiter(delete_user):
    """注册登录接口"""
    url = 'http://49.235.92.12:9000/api/v1/register'
    body = {
        "username": "小晓的筱",
        "password": "123456",
        "mail": "xiaoxiao@qq.com"
    }
    r = s.post(url, json=body)
    # print(r.text)
    print(r.json())
    assert r.json()['msg'] == '注册成功!'
