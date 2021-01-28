from flask import request


def test_get(test_client):
    response = test_client.get('/employee/')
    assert response.status_code == 200
    assert b'Employees' in response.data
    assert b'New' in response.data


def test_new_btn(test_client):
    response = test_client.get('/employee/')
    assert response.status_code == 200
    assert b'/employee/new' in response.data
    assert b'New' in response.data


def test_employee_data(test_client, test_employees):
    response = test_client.get('/employee/')
    assert b'TEST_1' in response.data
    assert b'TEST_2' in response.data