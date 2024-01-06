import concurrent.futures
import argparse
import json
import sys
from requests import get


def load_tester(url,count):
    """
    Sends HTTP requests and print response code
    :url: URL where request should be sent
    :count: The number of requests to be sent
    """
    response_codes = []
    urls = [url] * count
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(get, url, timeout=10) for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            data = future.result()
            response_codes.append(data.status_code)
            if future.exception() is not None:
                print(f'ERROR: {future}: {future.exception()}')
    print(response_codes)
    return response_codes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog='load_tester',
                        description='Load test using python',
                        epilog='')
    # group = parser.add_mutually_exclusive_group()
    parser.add_argument("-url", type=str, help="url")
    parser.add_argument("-n", "--number", dest="number", type=int,
                        help="number of requests")

    parser.add_argument("-readFromFile", type=str, help="filename")
    args = parser.parse_args()
    if args.readFromFile and (args.url or args.number):
        print("readFromFile and url|number are mutually exclusive")
        sys.exit(2)
    if args.readFromFile:
        with open(args.readFromFile, 'r', encoding='utf-8') as f:
            input_data = json.load(f)
            args.url = input_data["url"]
            args.number = input_data["number"]
    load_tester(args.url,args.number)
