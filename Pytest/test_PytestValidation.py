import pytest



def  test_firstCheck(preSetup):
    print("First line using python+pytest+playwright")
    #let´s validate a return from this function
    assert preSetup=="Setup for function was made"
    #This is one way to make Setup and teardowns but we can use the keyword yield to make it more readable and understandable

def test_secondCheck(preSetup):
    print("Second line using python+pytest+playwright")

def test_teardown(tearddownFixture):
    print("Teardown function was correctly made")

@pytest.mark.skip(reason="Skipped test, not needed now")
def test_skipped(preSetup):
    print("Skipped function was correctly made")

@pytest.mark.smoke
def test_smokeTest1(preSetup):
    print("smoke test1 function was correctly made")