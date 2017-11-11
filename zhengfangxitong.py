# 模拟登录正方教育系统

import os
import requests
from PIL import Image
from bs4 import BeautifulSoup


session = requests.session()
# 自动保存cookie信息, 避免出现验证码错误问题
url = 'http://10.66.0.102:8088/default2.aspx'
def get_data():
    r = session.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    VIEWSTATE = soup.find('input', {'name': '__VIEWSTATE'}).attrs['value']
    # 得到网站随机值
    link = soup.find('img', {'id': 'icode'}).attrs['src']
    pic_link = 'http://10.66.0.102:8088/' + str(link)
    pic = session.get(pic_link)
    with open('pic.png', 'wb') as f:
        f.write(pic.content)
    # 下载验证码图片
    image = Image.open('{}/pic.png'.format(os.getcwd()))
    image.show()
    image.close()
    Verification_Code = input('输入图片中的验证码:')

    data = {
        '__VIEWSTATE': VIEWSTATE,
        'txtUserName': '150510216',
        'Textbox1': '',
        'TextBox2': 'fifa2314034614',
        'txtSecretCode': Verification_Code,
        'RadioButtonList1': '%D1%A7%C9%FA',
        'Button1': '',
        'lbLanguage': '',
        'hidPdrs': '',
        'hidsc': '',
    }
    return data


data = get_data()
try:
    response = session.post(url, data=data)
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find('span', {'id': 'xhxm'}).text
    print(name)
except:
    print('登录失败')