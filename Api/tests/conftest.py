import os
import pytest
import psycopg2
import db_sync
from data import database
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

remoteorlocal = os.getenv('remoteorlocal')
if remoteorlocal == 'remote':
    pass
if remoteorlocal == 'local':
    pass
remote,remoteorlocal= False,'local'

@pytest.fixture
def example_fixture():
    return 1

@pytest.fixture(autouse=True, scope='session')
def pre_post_fixture():
    print(datetime.now())
    db_sync.main(silent_action='createdb',silent_remote=remote)
    db_sync.main(silent_action='drop_and_imp',silent_remote=remote,silent_test_sql=True)
    yield
    print(datetime.now())
    db_sync.main(silent_action='dropdb',silent_remote=remote)

@pytest.fixture(autouse=False)
def disable_db_calls(monkeypatch):
    def stunted_get_connection():
        raise RuntimeError("DB access not allowed during testing!")
    monkeypatch.setattr(database, "_get_connection", lambda *args, **kwargs: stunted_get_connection())

def test_db_get_connection():
    return psycopg2.connect(
        host = 'db.gboblangoijwxkkvkmsn.supabase.co' if remoteorlocal=="remote" else "localhost",
        # host = "localhost",
        user = 'postgres',
        dbname = 'test_db',
        options='-c search_path=test_schema',
        password = os.getenv('jobgrepass') if remoteorlocal=="remote" else os.getenv("password"),
        # password = os.getenv("password"),
        port = 5432
    )

@pytest.fixture(autouse=True)
def replace_db_conn(monkeypatch):
    monkeypatch.setattr(database, "_get_connection", lambda *args, **kwargs: test_db_get_connection())


# @pytest.fixture(autouse=True)
# def import_mock(mocker):
#     return mocker.patch("db_data.config._REL_IMPORT_DUMP_PATH", new=r'\db_data\db_test.sql', autospec=False)


# @pytest.mark.usefixtures("test_db")


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