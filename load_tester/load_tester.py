import argparse
from requests import get

def load_tester(url,count):
    """
    Sends HTTP requests and print response code
    :url: URL where request should be sent
    :count: The number of requests to be sent
    """
    response_codes = []
    while count:
        res = get(url, timeout=10)
        response_codes.append(res.status_code)
        count -= 1
    print(response_codes)
    return response_codes


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
