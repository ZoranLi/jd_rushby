#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

if __name__ == "__main__":
    chrome_browser = webdriver.Chrome()  # path形参缺省为环境变量 / 打包为exe后缺省为exe当前目录
    chrome_browser.maximize_window()
    chrome_browser.get("https://www.baidu.com")
    print('-chrome_browser-->')

    # time.sleep(10)
    # chrome_browser.refresh()
    # print(chrome_browser.get_cookies())
    # chrome_browser.implicitly_wait()

    # 查找元素
    element = chrome_browser.find_element(by="id", value='s_lg_img_new')
    print(element.text)
    print(element.get_attribute('src'))

# print(chrome_browser)
