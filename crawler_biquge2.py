# 爬取笔趣阁, 多线程版本
# 容易被封IP
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool


downloaded_book = []

def get_html(url):
    try:
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
        r = requests.get(url, timeout=30, headers=header)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ERROR"

def get_book():
    # 获取不同排行榜的书单
    url = 'http://www.qu.la/paihangbang/'
    soup = BeautifulSoup(get_html(url), 'lxml')
    tags = soup.find_all('div', class_='index_toplist')
    novel = []
    nums = 1
    for i in tags:
        type_name = i.find('span').text
        novel.append({'type': type_name})
        id = 'tabData_' + str(nums)
        novel_list = i.find('div', {'id': id})
        for n in novel_list.find_all('a'):
            novel.append({n.text: 'http://www.qu.la'+n.get('href')})
        nums += 1
    return novel


def download_list(name):
    global downloaded_book
    for n, h in name.items():
        if h[-2:] == "排行":
            if h != "玄幻奇幻排行":
                print('\n\n')
            print(h)
        else:
            if n not in downloaded_book:
                print("下载===>%s" % n)
                downloaded_book.append(n)
                download_novel_chapter(n, h)

def download_novel_chapter(name, link):
    # 获取每本书籍对应的章节列表
    try:
        soup = BeautifulSoup(get_html(link), 'lxml')
        characters = soup.find_all('div', {'id': 'list'})
        characters = BeautifulSoup(str(characters), 'lxml')
        characters = characters.find_all('a')
        for i in characters:
            chapter_name = i.text
            chapter_link = 'http://www.qu.la' + i.get('href')
            download_novel(name, chapter_name, chapter_link)
    except:
        print("获取小说章节出错")

def download_novel(name, chapter_name, chapter_link):
    # 下载章节内容
    try:
        soup = BeautifulSoup(get_html(chapter_link).replace('<br/>', '\n'), 'lxml')
        content = soup.find('div', {'id': 'content'}).text.replace('chaptererror();', '')
        with open('{}.txt'.format(name), 'a+') as f:
            print("下载:%s" % chapter_name)
            f.write(chapter_name + '\n\n')
            f.write(content)
    except:
        print("下载小说中发生错误")


if __name__ == '__main__':
    pool = Pool()
    pool = Pool(4)
    # 线程数量
    novels = get_book()
    pool.map(download_list, novels)