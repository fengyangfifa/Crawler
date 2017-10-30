import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return "ERROR"

def get_content(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    tags = soup.find_all('li', {'class': ' j_thread_list clearfix'})
    for tag in tags:
        replynum = tag.find('span', {'class': "threadlist_rep_num center_text"}).text
        link = 'http://tieba.baidu.com'+tag.find('a', {'class': 'j_th_tit'}).get('href')
        name = tag.find('span', {'class': "frs-author-name-wrap"}).text
        time = tag.find('span', {'class': "pull-right is_show_create_time"}).text
        title = tag.find('a', {'class': 'j_th_tit '}).text
        print('标题:%s  链接:%s  发帖人:%s  发帖时间:%s  回复数量:%s' % (title, link, name, time, replynum))


num = int(input("爬取页面数量:"))
for i in range(num):
    print("爬取第%s页" % (i + 1))
    url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'+str(50*i)
    get_content(url)