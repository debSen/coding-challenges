from requests import get
from sys import argv

def load_tester(url):
    res = get(url)
    print(res.status_code)

if __name__ == '__main__':
    load_tester(argv[1])
