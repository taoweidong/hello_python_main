# -*- coding: utf-8 -*-
from selenium import webdriver

if __name__ == '__main__':
    # 创建浏览器驱动实例
    driver = webdriver.Chrome()

    # 最大化浏览器窗口
    driver.maximize_window()

    # 打开新窗口
    driver.execute_script("window.open('about:blank', 'new_window')")

    # 切换到新窗口
    driver.switch_to.window(driver.window_handles[-1])

    # 打开网页
    url = "https://www.linuxprobe.com/python-selenium-linux.html"
    driver.get(url)

    # 截图并保存到本地
    driver.save_screenshot("screenshot.png")

    # 关闭浏览器驱动实例
    driver.quit()
