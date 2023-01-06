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


if __name__ == "__main__":

    # 规避相应的检测
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled --headless")
    # 这里填入你自己的chromedriver的安装路径
    driver = webdriver.Chrome(executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe',options=chrome_options)

    driver.get('https://gitee.com/login')

    # 根据id获取用户账号输入框、密码输入框
    # username_tag = driver.find_element_by_id('user_login')
    # password_tag = driver.find_element_by_id('user_password')
    username_tag = driver.find_element(By.ID,'user_login')
    password_tag = driver.find_element(By.ID,'user_password')

    # 填入自己的账号和密码
    username_tag.send_keys('liuzelin01@outlook.com')
    time.sleep(1)
    password_tag.send_keys('LIUzeLIN678^&*<>?')

    # 根据id获取登录按钮
    # login_btn = driver.find_element_by_id('J-login')
    login_btn = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[1]/div[2]/div[1]/form[1]/div/div/div/div[4]/input')

    # 点击登录按钮
    login_btn.click()
    # 这里必须得休眠，不然运行速度太夸，代码难以定位到滑块
    # time.sleep(5)
    # # span = driver.find_element_by_css_selector('.btn_slide')
    # span = driver.find_element(By.CSS_SELECTOR,'.btn_slide')

    # gitee 上无需滑块以及动作链
    # # 定义动作链，点击并拖拽
    # aco = ActionChains(driver)
    # # 点击并长按
    # aco.click_and_hold(span)
    #
    # # perform()立即执行动作链操作
    # for i in range(5):
    #     aco.move_by_offset(25,0).perform()
    #     time.sleep(0.3)
    #
    # # 释放动作链
    # aco.release()

    time.sleep(2)
    # ok_btn = driver.find_element_by_css_selector('.ok')
    # ok_btn = driver.find_element(By.CSS_SELECTOR,'.ok')
    # ok_btn.click()

    # 延迟5秒后，自动关闭浏览器
    # time.sleep(5)
    # driver.quit()

    # 在执行完动作后，不关闭浏览器
    browser = webdriver.Chrome()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
