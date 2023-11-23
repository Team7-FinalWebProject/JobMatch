import pytest
from data import database
from data.database import read_query
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

@pytest.mark.usefixtures("example_fixture")
def test_with_fixture(example_fixture):
    assert example_fixture == 1

@pytest.mark.usefixtures("disable_db_calls")
def test_db_conn_fails_with_fixture():
    with pytest.raises(RuntimeError):
        assert database._get_connection()

@pytest.mark.usefixtures("disable_db_calls")
@pytest.mark.xfail
def test_db_conn_test_fail_skipped_with_xfail():
    assert database._get_connection()

@pytest.mark.usefixtures("disable_db_calls")
@pytest.mark.skip
def test_db_conn_test_skipped_with_skip():
    assert database._get_connection()

def test_db_conn():
    expected = [('adminuser',), ('testuser1',), ('testuser2',), ('testuser3',), ('testuser4',), ('testuser5',),('testuser6',),('Ivo',)]
    result = read_query("select username from users", ())
    assert expected == result

def is_gtr_11(val):
    return val > 11
        
@pytest.mark.parametrize("valid_value", [
    12,
    15,
    22,
    121,
    50000,
])
def test_is_value_gtr_11(valid_value):
    assert is_gtr_11(valid_value)

@pytest.mark.parametrize("invalid_value", [
    0,
    10,
    -20,
    -3000
])
def test_is_value_not_gtr_11(invalid_value):
    assert not is_gtr_11(invalid_value)


def a_gtr_rest(val, *vals):
    return all(val > x for x in vals)
        

@pytest.mark.parametrize("big,small1,small2", [
    (12,1,2),
    (15,1,14),
    (22,-1,-2),
    (121,99,2),
    (50000,2,-50),
])
def test_is_value_gtr_all_rest(big,small1,small2):
    assert a_gtr_rest(big,small1,small2)

@pytest.mark.parametrize("big,small1,small2", [
    (0,10,10),
    (0,10,-1),
    (-20,1,0),
    (-3000,50,1000),
    pytest.param(50, 1, 2, marks=pytest.mark.xfail),
    pytest.param(5, 20, 30, marks=pytest.mark.xfail),
])
def test_is_value_not_gtr_all_rest(big,small1,small2):
    assert not a_gtr_rest(big,small1,small2)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "JobUtopia"
