import argparse
from requests import get
import concurrent.futures

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
            try:
                data = future.result()
                response_codes.append(data.status_code)
            except Exception as exc:
                print('generated an exception: %s' % (exc))
            else:
                print('page is %d bytes' % (len(data.text)))
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
