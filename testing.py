import pytest

@pytest.fixture()
def tester():
    FullName = "Adip"      
    Contact = 9863208029    
    Address = "Balaju"    
    return [FullName,Contact,Address]

def testing_1(tester):
    first_name = ""    
    assert tester[0] == first_name

def testing_2(tester):
    first_name = "Adip"    
    assert tester[0] == first_name

def testing_3(tester):
    phone_no = 9863208029 
    assert tester[1] == phone_no

def testing_4(tester):
    phone_no=9800000000
    assert tester[2] == phone_no

def testing_5(tester):
    place = "Balaju"    
    assert tester[2] == place

def testing_6(tester):
    place="Macchapokhari"
    assert tester[2] == place




