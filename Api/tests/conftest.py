import os
from datetime import datetime
import pytest
import psycopg2
from dotenv import load_dotenv
from db_data import db_utils
from data import database
import warnings
from fastapi.testclient import TestClient

load_dotenv()

from main import app

client = TestClient(app)


user_password = os.getenv('userpassword')
# invalid_user = {"username": "EFrQjeqVSwyPx_t6O", "password": "stringst"}
# invalid_username = {"username": "EFrQjeqVSwyPx_t6O", "password": f"{valid_password}"}
# invalid_admin_password = {"username": "adminfortest", "password": "stringst"}
# invalid_prof_password = {"username": "testuser1", "password": "stringst"}
# invalid_comp_password =  {"username": "testuser4", "password": "stringst"}
# valid_admin = {"username": "adminfortest", "password": f"{valid_password}"}
# valid_professional = {"username": "testuser1", "password": f"{valid_password}"}
# valid_company = {"username": "testuser4", "password": f"{valid_password}"}

@pytest.fixture
def valid_password():
    return user_password

@pytest.fixture
def invalid_user():
    return {"username": "EFrQjeqVSwyPx_t6O", "password": "stringst"}

@pytest.fixture
def invalid_username():
    return {"username": "EFrQjeqVSwyPx_t6O", "password": user_password}

@pytest.fixture
def invalid_admin_password():
    return {"username": "adminfortest", "password": "stringst"}

@pytest.fixture
def invalid_prof_password():
    return {"username": "testuser1", "password": "stringst"}

@pytest.fixture
def invalid_comp_password():
    return {"username": "testuser4", "password": "stringst"}

@pytest.fixture
def valid_admin():
    return {"username": "adminfortest", "password": user_password}

@pytest.fixture
def valid_professional():
    return {"username": "testuser1", "password": user_password}

@pytest.fixture
def valid_company():
    return {"username": "testuser4", "password": user_password}

@pytest.fixture
def proftoken(valid_professional):
    try:
        result = client.post("/login/professionals", json=valid_professional).json()["token"]
    except Exception as e:
        raise Exception from e
    return result

@pytest.fixture
def companytoken(valid_company):
    try:
        result = client.post("/login/companies", json=valid_company).json()["token"]
    except Exception as e:
        raise Exception from e
    return result

@pytest.fixture
def admintoken(valid_admin):
    try:
        result = client.post("/login/admins", json=valid_admin).json()["token"]
    except Exception as e:
        raise Exception from e
    return result


remoteorlocal = os.getenv('remoteorlocal')
if remoteorlocal == 'remote':
    pass
if remoteorlocal == 'local':
    pass
##Hardcoded for local for the time being
remote,remoteorlocal= False,'local'

@pytest.fixture
def example_fixture():
    return 1

@pytest.fixture(autouse=False)
def disable_db_calls(monkeypatch):
    def stunted_get_connection():
        raise RuntimeError("DB access not allowed during testing!")
    monkeypatch.setattr(database, "_get_connection", lambda *args, **kwargs: stunted_get_connection())

###CHANGES DB to a dynamically created test_db database, apply consideration if changing
###BEGIN
def test_db_get_connection():
    return psycopg2.connect(
        host = 'db.gboblangoijwxkkvkmsn.supabase.co' if remoteorlocal=="remote" else "localhost",
        user = 'postgres',
        dbname = 'test_db',
        options='-c search_path=test_schema',
        password = os.getenv('jobgrepass') if remoteorlocal=="remote" else os.getenv("password"),
        port = 5432
    )

@pytest.fixture(autouse=True)
def replace_db_conn(monkeypatch):
    print(datetime.now())
    monkeypatch.setattr(database, "_get_connection", lambda *args, **kwargs: test_db_get_connection())
    expected = [('adminfortest',),]
    result = database.read_query("select username from users where id = 1", ())
    if expected != result:
        pytest.skip("Skipping remaining tests, test_db validation failed, cannot guarantee prod db is not being tested.")

@pytest.fixture(autouse=True, scope='session')
def pre_post_fixture():
    print(datetime.now())
    db_utils.main(silent_action='createdb',silent_remote=remote)
    db_utils.main(silent_action='drop_and_imp',silent_remote=remote,silent_test_sql=True)
    yield
    db_utils.main(silent_action='dropdb',silent_remote=remote)
###/CHANGES DB to a dynamically created test_db database, apply consideration if changing
###END


# ##Hook patterns not sure if functional
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_setup(item):
#     # Set up resources or perform other tasks before the test is run
#     yield
#     # Tear down resources or perform other tasks after the test is run

# @pytest.hookimpl(hookwrapper=True)
# def pytest_load_initial_conftests(early_config, parser, args):
#     pass
#     # Do stuff before any tests

#py -m pytest -durations=3 -vv
# @pytest.hookimpl
# def pytest_report_teststatus(report, config):
#     if report.when == "call":
#         print("duration reported immediately after test execution:", report.duration)

# @pytest.hookimpl
# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#     for reps in terminalreporter.stats.values():
#         for rep in reps:
#             if rep.when == "call":
#                 print("duration reported after all tests passed:", rep.nodeid, rep.duration)