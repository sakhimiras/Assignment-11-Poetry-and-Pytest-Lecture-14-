from assignment_11.main import sum, multiply

def test_sum():
    assert sum(1,1) == 2
    assert sum(5,7) == 12
    assert sum(8,7) == 15

def test_multiply():
    assert multiply(2,2) == 4
    assert multiply(5,10) == 50
    assert multiply(10,10) == 100