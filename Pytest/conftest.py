import pytest

#We define the conftest to implement my fixtures globally
@pytest.fixture(scope="function")#Here, I specify that this fixture will execute before every function in this module
def preSetup():
    print("webdriver Pre-setup on functions")
    return "Setup for function was made"

@pytest.fixture(scope="module")
def moduleFixture():
    print("Setup only for the module")

@pytest.fixture(scope="session")#we implement a fixture that runs every testing session
def sessionFixture():
    print("Session setup for the whole set of tests")

@pytest.fixture(scope="module")
def tearddownFixture():
    print("Session started")
    yield
    print("Session ended")