import argparse
from requests import get

def load_tester(url,count):
    """
    Sends HTTP requests and print response code
    :url: URL where request should be sent
    :count: The number of requests to be sent
    """
    while count:
        res = get(url, timeout=10)
        print(res.status_code)
        count -= 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog='load_tester',
                        description='Load test using python',
                        epilog='')
    parser.add_argument("url", type=str, help="url")
    parser.add_argument('-n', '--number', dest='number', type=int,
                        default=1, help='number of requests')
    args = parser.parse_args()
    load_tester(args.url,args.number)
