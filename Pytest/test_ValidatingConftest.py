#This page is to validate the correct functioning of our configuration with conftest
import pytest


def test_configValidation(preSetup):
    print("test_configValidation")

def test_configModuleScope(moduleFixture):
    print("Validating the fixture scope first")

def test_configModuleScope2(moduleFixture):#for this function, the setup won´t be printed
    print("Validating the fixture scope second")

def test_sessionValidation(sessionFixture):
    print("Session was correctly validated")

@pytest.mark.smoke
def test_smokeTest2(preSetup):
    print("smoke test2 function was correctly made")