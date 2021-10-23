# from tornado import ioloop, httpclient
#
# i = 0
#
# def handle_request(response):
#     print(response.code)
#     global i
#     i -= 1
#     if i == 0:
#         ioloop.IOLoop.instance().stop()
#
# http_client = httpclient.AsyncHTTPClient()
#
# for url in open('urllist.txt'):
#     i += 1
#     print(i)
#     http_client.fetch(url.strip(), handle_request, method='GET')
#
# ioloop.IOLoop.instance().start()

from tornado import ioloop, httpclient

def handle_request(response):
    if response.error:
        print ("Error:", response.error)
    else:
        print (response.body)
    ioloop.IOLoop.instance().stop()

http_client = httpclient.AsyncHTTPClient()
http_client.fetch("https://cn.bing.com/", handle_request)
ioloop.IOLoop.instance().start()