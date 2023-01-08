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

# todo(liuzel01): 跳转到填写日报页面，并打开新建任务页
# todo(liuel01): 通过读取本地文件，填写任务的字段

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

    # 根据xpath获取登录按钮
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
    time.sleep(10)
    action.move_by_offset(100,100).click().perform()
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
