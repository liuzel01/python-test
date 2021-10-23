import concurrent.futures
import requests

out = []
CONNECTIONS = 100
TIMEOUT = 5

urls = []
with open("urllist.txt") as reader:
    for url in reader:
        urls.append(url.strip())

def load_url(url, timeout):
    ans = requests.get(url, timeout=timeout)
    return ans.status_code

with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = (executor.submit(load_url, url, TIMEOUT) for url in urls)
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data = future.result()
        except Exception as exc:
            data = str(type(exc))
        finally:
            out.append(data)
            print(data)

