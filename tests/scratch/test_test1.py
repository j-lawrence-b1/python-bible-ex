from app.scratch import test1

# test_with_pytest.py

def test_foo():
    assert test1.foo() == "foo!"

def test_main():
    assert test1.main() == "foo!"