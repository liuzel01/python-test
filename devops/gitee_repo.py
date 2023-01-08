# -*- coding:utf-8 -*-
import requests
import sys
import io

__author__ = "liuzel01"
__EMAIL__ = "@hilonggroup.com"

'''此程序是为了方便统计 gitee 的所有代码，以及其所属项目、对应的研发负责人信息
'''
if __name__ == "__main__":

    # 改变标准输出的默认编码
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

    # 登录后才能访问的网页
    url = 'https://e.gitee.com/hilong_1/code/repos'

    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    cookie_str = r'user_locale=zh-CN; oschina_new_user=false; tz=Asia%2FShanghai; slide_id=9; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218585fb948058f-04cec43b46dd84-26021151-2073600-18585fb9481f6d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218585fb948058f-04cec43b46dd84-26021151-2073600-18585fb9481f6d%22%7D; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; Hm_lvt_24f17767262929947cc3631f99bfd274=1672990136; gitee-session-n=dWFSV29wZ0NLc055OEh0aE8wYnlObnlQOGZqMmVDVHFVTUZtZWlEVVVmMzB1U0htWHQ1WE5tNEFJMGlYUHZjL1cyWk41dnZ4eVFucVE1c1hSMXE0MGV5cTJqNVprUUEvWnNFK1FVMHFOQ1Q1Z2JWMXo0SGlYd2liWXJEdG9DNXE5ZE56VFU1dEdseldqeHFGK20xdDNINWM3cHpCaFBDdGNrMzk0QnVLYmpwZVhXVFVPMklLZGZxZHpQQi92dUhzVU9hdElhV0dBUWcwSTh2Q0FiMG55OEJlckJ5TVo3dFJmL2lHTWhjWU5od0hOdkdvcU5DWFQwVWxkcjdxeWxxUnBvcXVRdFI5YTFvSWhZaXdFYWlBT1dIem1CY011clQrWlM2UWx6aWpnakFXQ3RmVEZDT090RVdpWG1iZXVEWU1PazN0RENHUG9QM1FDQm9iWUVUQ21vZFhaemZPV09jZEdSak1xNTFXK0pzOG82bEwrS1ZqRklIdFdrZ01GcWJjUUduM0c4ZGU4N0FlQ1VPZWVZS1JYT3VMdnpMSzhDdE1FY052OUdHVkMzbExxK3J0NkRXS2NzOG5vM01hYXJrTi0tWG92VVN1TklYRXpqTGV6NmNDMzRrQT09--36799ca3f4aec5a0b361fe0ba35d4d6767d96e5e; Hm_lpvt_24f17767262929947cc3631f99bfd274=1672990140'

    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value

    # 设置请求头
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    # 在发送get请求时带上请求头和cookies
    resp = requests.get(url, headers=headers, cookies=cookies)

    print(resp.content.decode('utf-8'))
