# 新浪微博
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://weibo.com/')
browser.implicitly_wait(3)
time.sleep(8)

name = browser.find_element_by_id('loginname')
passowrd = browser.find_element_by_name('password')
name.send_keys('18244325218')
passowrd.send_keys('fywy.fifa1998')
t = browser.find_element_by_xpath('//div[@class="info_list login_btn"]/a')
t.click()
# 睡眠三秒, 等待账户登录成功
time.sleep(3)
browser.get('https://d.weibo.com/')
browser.implicitly_wait(3)

contents1 = browser.find_elements_by_xpath('//div[@class="WB_cardwrap WB_feed_type S_bg2 WB_feed_like"]')
contents2 = browser.find_elements_by_xpath('//div[@class="WB_cardwrap WB_feed_type S_bg2 WB_feed_vipcover WB_feed_like"]')
if len(contents1) > 0:
    for i in contents1:
        name = i.find_element_by_xpath('.//div[@class="WB_info"]/a[1]').text
        times = i.find_element_by_xpath('.//div[@class="WB_from S_txt2"]').text
        txt = i.find_element_by_xpath('.//div[@class="WB_text W_f14"]').text
        comment = i.find_element_by_xpath('.//ul[@class="WB_row_line WB_row_r4 clearfix S_line2"]/li[3]/a')
        print('%s\n%s\n%s\n\n' % (name, times, txt))
        comment.click()
else:
    print('没有匹配到数据!')


if len(contents2) > 0:
    for i in contents2:
        name = i.find_element_by_xpath('.//div[@class="WB_info"]/a[1]').text
        times = i.find_element_by_xpath('.//div[@class="WB_from S_txt2"]').text
        txt = i.find_element_by_xpath('.//div[@class="WB_text W_f14"]').text
        comment = i.find_element_by_xpath('.//ul[@class="WB_row_line WB_row_r4 clearfix S_line2"]/li[3]/a')
        print('%s\n%s\n%s\n\n' % (name, times, txt))
        comment.click()
else:
    print('没有匹配到数据!')
