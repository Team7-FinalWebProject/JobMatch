import pytest
from data import database

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get_connection():
        raise RuntimeError("DB access not allowed during testing!")
    monkeypatch.setattr(database, "_get_connection", lambda *args, **kwargs: stunted_get_connection())

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