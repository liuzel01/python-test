import grequests

urls = []
with open("urllist.txt") as reader:
    for url in reader:
        urls.append(url.strip())

rs = (grequests.get(u) for u in urls)

for result in grequests.map(rs):
    print(result.status_code, result.url)
