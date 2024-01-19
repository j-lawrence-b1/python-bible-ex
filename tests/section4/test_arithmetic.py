from app.section4 import arithmetic

def test_can_add():
    try:
        arithmetic(2,2)
    catch NotImplementedError:
        assert False

def test_add_int():
    ret = arithmetic.add(2,2)
    assert type(ret) == "<class 'int'>"
    assert ret == 2