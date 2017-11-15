# 爬取it之家热评
import time
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool

# 生成器函数
def get_new(page):
    header = {'User_Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
    if page == 1:
        url = 'http://android.ithome.com/androidphone/'
        r = requests.get(url, headers=header)
    else:
        url = 'http://android.ithome.com/ithome/getajaxdata.aspx'
        data = {
            'categoryid': '74',
            'type': 'pccategorypage',
            'page': str(page)
        }
        r = requests.post(url, data=data, headers=header)
    try:
        soup = BeautifulSoup(r.text, 'lxml')
        new_list = soup.find_all('a', class_='list_thumbnail')
        for new in new_list:
            yield new['href'].split('/')[-1].replace('.htm', '')
    except:
        print('获取新闻id发生错误')

def hot_comment(page):
    print('爬取第%s页' % page)
    new_list = get_new(page)
    header = {'User_Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
    comment_url = 'https://dyn.ithome.com/ithome/getajaxdata.aspx'
    for new_id in new_list:
        data = {
            'newsID': new_id,
            'type': 'hotcomment',
        }
        try:
            r = requests.post(comment_url, data=data, headers=header)
            soup = BeautifulSoup(r.text, 'lxml')
            hot_list = soup.find_all('li', {'nid': new_id})
            for comment in hot_list:
                name = comment.find('strong', class_='nick').string
                phone = comment.find('span', class_='mobile android')
                if phone:
                    phone = phone.string
                else:
                    phone = ''
                push_time = comment.find('span', class_='posandtime').string
                comment_text = comment.find('p').get_text()
                save_comment('{} {} {}\n{}\n\n'.format(name, phone, push_time, comment_text))
        except:
            print('获取热评失败')

def save_comment(comment):
    with open('hot_comments.txt', 'a') as f:
        f.write(comment)


if __name__ == '__main__':
    pool = Pool()
    pool = Pool(30)
    start = time.time()
    pool.map(hot_comment, [i for i in range(1, 50)])
    end = time.time()
    print('运行%s seconds' % int(end - start))