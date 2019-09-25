from py_test_strategy.app import App


def test_app():
    a = App()
    assert a.add(one=1, two=2) == 3
