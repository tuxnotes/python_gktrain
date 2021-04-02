from selenium import webdriver
import time

try:
    browser = webdriver.chrome
    # 需要安装Chrome driver,且防止到PATH中, driver的版本要与浏览器的版本一致
    browser.get('https://www.douban.com')
    time.sleep(1)

    browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    btm1 = browser.find_element_by_xpath('html/body/div[1]/div[1]/ul[1]/li[2]')
    btm1.click()

    browser.find_element_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')
    browser.find_element_by_id('password').send_keys('test123test123')
    time.sleep(1)
    browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()
    cookies = browser.get_cookies() # 获取cookie
except Exception as e:
    print(e)


finally:
    browser.close()