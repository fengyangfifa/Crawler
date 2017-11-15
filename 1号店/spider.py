# 爬取1号店
import re
import time
import requests
from bs4 import BeautifulSoup

def get_address(commodity_id):
    """通过while实现对配送地址的选择和得到地址对应的字符"""
    url = 'https://item.yhd.com/{}.html'.format(commodity_id)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    address = soup.find_all('a', class_='sec_item')
    region = []
    for i in address:
        addr = {}
        addr[i.string] = i['data-id']
        region.append(addr)
    city_address = ''
    nums = 2
    while True:
        parentId = ''
        for i in region:
            for k, v in i.items():
                print('%s ' % k, end='')
        print('\n')
        city = input('输入配送地区:')
        for i in region:
            for k, v in i.items():
                if k == city:
                    parentId = v
        city_address += parentId
        url = 'https://item.yhd.com/squ/item/ajaxGetAreas.do?type={}&parentId={}'.format(nums, parentId)
        region = []
        nums += 1
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        address = soup.find_all('a', class_='sec_item')
        flag = soup.find('div', class_='errortext')
        if r.text == '':
            city_address += '_0'
            break
        if flag:
            break
        for i in address:
            addr = {}
            addr[i.string] = i['data-id']
            region.append(addr)
        city_address += '_'
    return city_address

def get_commodity(name):
    """搜索商品, 获取数据"""
    all_commodity = []
    url = 'https://search.yhd.com/c0-0/k' + name
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    commoditys = soup.find_all('div', class_='mod_search_pro')
    for i in commoditys:
        commodity = {}
        commodity['price'] = i.find('p', class_='proPrice').get_text().replace('\n', '')
        info = i.find('p', class_='proName clearfix')
        commodity['configure'] = info.find('a').string.replace('\n', '')
        commodity['commodity_url'] = 'https' + info.find('a')['href']
        all_commodity.append(commodity)
    return all_commodity


if __name__ == '__main__':
    commodity = input('请输入你需要查询的商品:')
    all_commodity_id = []
    commodity_info = get_commodity(commodity)
    for i in commodity_info:
        commodity_id = i['commodity_url'].split('/')[-1].replace('.html', '')
        all_commodity_id.append(commodity_id)


    address = get_address(all_commodity_id[0])
    print('正在搜索相关商品')
    for i in range(len(all_commodity_id)):
        """通过地址, 得到商品的库存"""
        times = int(time.time()*1000)
        url = 'https://c0.3.cn/stock?extraParam=%7B%22originid%22:%221%22%7D' \
              '&ch=1&skuId={}&area={}' \
              '&cat=9987%2C653%2C655' \
              '&buyNum=1&fqsp=0&_={}'.format(all_commodity_id[i], '22_2058_2061_41134', times)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        content = soup.find('p').get_text()
        stock = re.findall(r'"stockDesc":"(.*?)","venderType"', content)[0]
        commodity_info[i]['stock'] = stock
    print('搜索完毕......正在处理数据')
    for i in commodity_info:
        print('型号: %s 价格: %s 库存: %s 地址: %s' %
              (i['configure'], i['price'], i['stock'], i['commodity_url']))