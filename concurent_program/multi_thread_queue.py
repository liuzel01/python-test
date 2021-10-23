from threading import Thread
import sys
from queue import Queue
import requests

concurrent = 200


def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        doSomethingWithResult(status, url)
        q.task_done()


def getStatus(ourl):
    try:
        res = requests.get(ourl)
        return res.status_code, ourl
    except:
        return "error", ourl


def doSomethingWithResult(status, url):
    print(status, url)


q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()

try:
    for url in open("urllist.txt"):
        q.put(url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
