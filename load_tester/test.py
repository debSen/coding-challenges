from load_tester import load_tester

def test_load_tester():
    url = "http://eu.httpbin.org/get"
    count = 5
    assert load_tester(url, count) == [200] * 5
