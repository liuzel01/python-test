# -*- coding:utf-8 -*-
import requests
import json
import xlwings as xw

__author__ = "liuzel01"
__EMAIL__ = "@hilonggroup.com"

'''此程序是为了方便统计 gitee 的所有代码，以及其所属项目、对应的研发负责人信息
'''
# # 改变标准输出的默认编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#
# #登录后才能访问的网页
# url = 'https://gitee.com'
#
# #浏览器登录后得到的cookie，也就是刚才复制的字符串
# cookie_str = r'Hm_lvt_24f17767262929947cc3631f99bfd274=1672717565; sajssdk_2015_cross_new_user=1; user_locale=zh-CN; oschina_new_user=false; tz=Asia%2FShanghai; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; csrf_token=JZPpjiQDui7icq3R2maqzbFWoQPgfs3GPmjkntetJm8RBwB4Sf6x2CxNecpJ8Qt3wT093DePkFUQCdsFBkGqpA%3D%3D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22185761750b6d4b-03c3dce226a0d58-26021151-2073600-185761750b7ee6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1NzViYzk5MjM2OGEtMGY4NmI1MGZhOTc5MDMtMjYwMjExNTEtMjA3MzYwMC0xODU3NWJjOTkyNGRmZCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6Ijc1NTM5OTMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%227553993%22%7D%2C%22%24device_id%22%3A%2218575bc992368a-0f86b50fa97903-26021151-2073600-18575bc9924dfd%22%7D; feature_log_id=9; slide_id=9; gitee-session-n=bmMyUDU0ZU54QVhmbmJIS3F4N0NZMUVNODZMaVd6T0hudHhtZDgzbWc2Q1JLR3VEUTZOaWlCcnl3SzdGWXJmVmswSzJRYzNXazdNQ2pqSmN0YUxvamxMSlJVKzlqZW5RSHVGSUxQVU1xbWlpVFhqS3VMVTd1WjR2VUNtTkJuV0k0dnQ2TnNQL1JNcENSamFmalVEOWtWK1FzenFDMk04T2s1dXF4cDNENllxaVVxU3NyVElZZlVvMVdqWGI4alFCOWl4VzVUN2pETDU2WjZZL0E4QlB3WlZCZmlya0ZVVFFVVXdENUR2SWdraWFjUVorcFE3TkRWcURmOGU5TlF4UkhhaUVuQ2swWU92MkFudFZYb1M5LzlBemZwWFlXbC8yL0wrSVFxQitYbG5QUlIvRE9SNzBaM05YMkNJU0FFSG1qVmtBS25pZzBMbUZYazNPVUo2OTFFbFNRZ0dIdW45RlNkRjVodlc2bVJKbDNVc3VvemN2ak9QdFo4ZnlscUo1c0NNSHcxdmV4MUdKR2h3MWlZRDRMYUVFZmRGWG05TjlQZEk5MmtBemIxMFA5L3A0Z09OYzVCblNqcTJyWlh2Zi0tSlNEcktzSUhDVFluUXkrdkdXeSt4QT09--d77413927a4a577e73176904de22f3f78d2038a4; Hm_lpvt_24f17767262929947cc3631f99bfd274=1672723525'
#
# #把cookie字符串处理成字典，以便接下来使用
# cookies = {}
# for line in cookie_str.split(';'):
#     key, value = line.split('=', 1)
#     cookies[key] = value


#UA:User-Agent(请求载体的身份标识)
#UA检测，网站检测到UA不是正常浏览器身份标识，则服务器端很有可能会拒绝该请求
#UA伪装，让爬虫对应的请求载体UA标识伪装成某一浏览器
#解析豆瓣电影
#页面局部刷新 XHR请求

# 指定url，发起请求，获取响应数据，存储
if  __name__ == "__main__":
    # UA:将对应的User_Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    url = "https://movie.douban.com/j/chart/top_list"
    start_num = input("enter start num:")
    limit_num = input("enter limit num:")
    param = {
        'type': '5',
        'interval_id': '100:90',
        'action':'',
        'start': start_num,
        'limit': limit_num,
    }
    # 处理url携带的参数：封装到字典中
    response = requests.get(url=url, params=param, headers=headers)
    # print(response.text)
    # ps_name = json.loads(response.text).get('ps_name')
    # print('\r\n',ps_name)
    # 确认服务器返回的json则可以使用json
    dic_obj = response.json()
    # json_name = json.loads(dic_obj)
    # app = xw.App(visible=False, add_book=False)
    app = xw.App(visible=True, add_book=False)
    # wb = app.books.add()
    # sht = wb.sheets['Sheet1']

    # sht.range('A1').value ='序号'
    # sht.range('B1').value ='排名'
    # sht.range('C1').value ='名称'
    # sht.range('D1').value ='评分'
    # sht.range('E1').value ='上映日期'
    # sht.range('F1').value ='国家'
    #
    # i=1
    # for dic_item in dic_obj:
    #     print('cnt:',i,'title ',dic_item['title'],'\r\n')
    #     sht.range('A'+str(i+1)).value = i
    #     sht.range('B'+str(i+1)).value = dic_item['rank']
    #     sht.range('C'+str(i+1)).value = dic_item['title']
    #     sht.range('D'+str(i+1)).value = dic_item['rating'][0]
    #     sht.range('E'+str(i+1)).value = dic_item['release_date']
    #     sht.range('F'+str(i+1)).value = dic_item['regions'][0]
    #     i += 1
    # wb.save('movie_rank.xlsx')
    # wb.close()
    # app.quit()
