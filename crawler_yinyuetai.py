# 爬取音悦tai
import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
        r = requests.get(url, timeout=30, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('ERROR')

def get_music_list():
    # 得到音乐榜
    url = 'http://vchart.yinyuetai.com/vchart/trends'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    try:
        tags = soup.find('div', class_='search-area')
        list = tags.find_all('a')
        music_list = []
        for music in list:
            music_list.append({music.text: 'http://vchart.yinyuetai.com%s' % music.get('href')})
        return music_list
    except:
        print('获取音乐榜单时发生错误')

def get_music():
    music_list = get_music_list()
    for i in music_list:
        for name, link in i.items():
            print(name)
            html = get_html(link)
            soup = BeautifulSoup(html, 'lxml')
            try:
                list = soup.find_all('li', {'class': 'vitem J_li_toggle_date '})
                for music in list:
                    score = music.find('h3').text
                    top_num = music.find('div', class_='top_num').text
                    name = music.find('a', class_='mvname').text
                    singer_name = music.find('a', class_='special').text
                    date = music.find('p', class_='c9').text
                    print('分数:%s 排名:%s 名字:%s %s 歌手:%s' % (score, top_num, name, date, singer_name))
                print('\n\n')
            except:
                print('获取音乐信息时发生误错误')


if __name__ == '__main__':
    get_music()