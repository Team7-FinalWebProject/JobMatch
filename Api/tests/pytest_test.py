import pytest
from tests.fixtures import example_fixture

@pytest.mark.usefixtures("example_fixture")
def test_with_fixture(example_fixture):
    assert example_fixture == 1
