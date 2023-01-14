# -*- coding:utf-8 -*-

from selenium import webdriver
from lxml import etree
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
# 实现无可视化界面
from selenium.webdriver.chrome.options import Options

'''
实现思路：
1. 自动登录网站（模拟人的行为进行登录、浏览）
2. 通过点击对应按钮，进入到填写日报页
3. 点击“新建任务”按钮，开始填写日报
4. 将对应字段填写完成，点击“新建”按钮，完成日报的创建
'''

# todo(liuzel01): 通过读取本地文件，填写任务的字段
# todo(liuzel01): 将函数 time.sleep 使用 while(1): try: 循环代替
# todo(liuzel01): XPATH 绝对路径不能保证后续程序的健壮性，需要更改

if __name__ == "__main__":

    # 规避相应的检测
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled --headless")

    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)

    # 这里填入你自己的chromedriver的安装路径
    driver = webdriver.Chrome(executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe',options=chrome_options)

    driver.get('https://gitee.com/login')
    driver.maximize_window()

    # 根据id获取用户账号输入框、密码输入框
    username_tag = driver.find_element(By.ID,'user_login')
    password_tag = driver.find_element(By.ID,'user_password')

    # 填入自己的账号和密码
    username_tag.send_keys('liuzelin01@outlook.com')
    time.sleep(1)
    password_tag.send_keys('LIUzeLIN678^&*<>?')

    # 通过xpath获取登录按钮
    login_btn = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[1]/div[2]/div[1]/form[1]/div/div/div/div[4]/input')
    # 点击登录按钮
    login_btn.click()

    # 进入企业
    time.sleep(5)
    # hlit_btn = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/a')
    # 根据元素内容来定位
    hlit_btn = driver.find_element(By.XPATH,"//h4[contains(text(),'海隆石油集团（上海）信息技术有限公司')]")
    hlit_btn.click()

    # 有新打开窗口，需要切换窗口
    windows = driver.window_handles
    driver.switch_to.window(windows[1])

    # 点击空白处，隐藏弹窗
    action = ActionChains(driver)
    time.sleep(15)
    action.move_by_offset(100,100).click().perform()

    # 进入填写日报页
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/a[3]').click()
    # 进入任务
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]/div/div/div/div[1]/div[1]/div/a[3]').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]/div/div/div/div[1]/a[1]').click()

    # 标题
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[1]/div[1]/div/div/input').send_keys('l01-日报')
    # driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[1]/div[2]/div[1]/div/div/div/div').send_keys('刘泽霖')
    # 负责人/协作者
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[1]/div[2]/div[1]/div/div/div/div').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/input').send_keys('liuzelin')
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/span[1]').click()

    # 类型是下拉选项框，这里先选择父节点，再触发子节点点击
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[1]/div[2]/div[2]/div/div/span[1]/input').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[3]/div/div/div/div[2]/div[1]/div/div/div[6]/div').click()
    # parent.find_element_by_xpath('.//option[@value="20"]').click()
    # 关联项目
    # driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[1]/div[3]/div[1]/div/div/span[1]/input').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[1]/div[3]/div[1]/div/div/span[1]/input').send_keys('软件产品部-日报')
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[3]/div/div/div/div[2]/div[1]/div/div/div[2]').click()

    # 计划时间
    # 日期选择框无法进行键盘输入
    current_time = time.strftime('%Y.%m.%d',time.localtime(time.time()))
    # js = "$('driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[1]/div[3]/div[2]/div/div/div/div/div[1]/input')').removeAttr('readonly')"
    js = "$('input[id=c-date1]').attr('readonly','')"
    js =
    driver.execute_script(js)

    # driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[1]/div[3]/div[2]/div/div/div/div/div[1]/input').send_keys(current_time)
    # driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[1]/div[3]/div[2]/div/div/div/div/div[3]/input').send_keys(current_time)

    # js = "$('input:eq(0)').removeAttr('readonly')"

    # 开始写入任务描述
    # driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/form/div[1]/div[4]/div/div[1]').click()
    # driver.get('https://e.gitee.com/hilong_1/dashboard')
    # # 进入工作项
    # time.sleep(3)
    # issue_btn = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/a[3]')
    # issue_btn.click()

    # time.sleep(2)
    # ok_btn = driver.find_element_by_css_selector('.ok')
    # ok_btn = driver.find_element(By.CSS_SELECTOR,'.ok')
    # ok_btn.click()

    # 延迟5秒后，自动关闭浏览器
    # time.sleep(5)
    # driver.quit()

    # # 在执行完动作后，不关闭浏览器
    # # browser = webdriver.Chrome()
    # ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
