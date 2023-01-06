# -*- coding:utf-8 -*-
import requests
import xlwings as xw

__author__ = "liuzel01"
__EMAIL__ = "@hilonggroup.com"

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
    start_num = int(input("enter start num:")) - 1
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
    # print(dic_obj)
    # json_name = json.loads(dic_obj)
    app = xw.App(visible=False, add_book=False)
    # app = xw.App(visible=True, add_book=False)
    wb = app.books.add()
    sht = wb.sheets['Sheet1']

    sht.range('A1').value ='序号'
    sht.range('B1').value ='排名'
    sht.range('C1').value ='名称'
    sht.range('D1').value ='评分'
    sht.range('E1').value ='上映日期'
    sht.range('F1').value ='国家'

    try:
        i = 1
        for dic_item in dic_obj:
            print('cnt:',i,'title ',dic_item['title'],'\r\n')
            sht.range('A'+str(i+1)).value = i
            sht.range('B'+str(i+1)).value = dic_item['rank']
            sht.range('C'+str(i+1)).value = dic_item['title']
            sht.range('D'+str(i+1)).value = dic_item['rating'][0]
            sht.range('E'+str(i+1)).value = dic_item['release_date']
            sht.range('F'+str(i+1)).value = dic_item['regions'][0]
            i += 1
    except:
        print('发生异常')
    wb.save('movie_rank.xlsx')
    wb.close()
    app.quit()

    print('完成')
