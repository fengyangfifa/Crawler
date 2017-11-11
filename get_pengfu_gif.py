import urllib.request
import re
# 下载捧腹网动图


def get_and_download_gif(url, page):
    global img_nums
    head = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"}
    request = urllib.request.Request(url=url, headers=head)
    data = urllib.request.urlopen(request).read().decode('utf-8')
    gif_and_img_url = re.findall(r'<h1 class="dp-b"><a href="https://www.pengfu.com/(.*?)" target="_blank">.*?</a>', data)
    # 得到所有的url
    gif_and_img = []
    for i in gif_and_img_url:
        date = re.findall(r'<h1 class="dp-b"><a href="https://www.pengfu.com/%s" target="_blank">(.*?)</a>.*?</h1>.*?<div class="content-img clearfix pt10 relative">.*?<img src=".*?" width=".*?" height=".*?" gifsrc="(.*?)">.*?</div>' % i, data, re.S)
        gif_and_img.append(date)
    # 得到gif_and_img的url
    gif = []
    really_gif_and_img = []
    for i in gif_and_img:
        # print(i)
        if i == []:
            pass
        else:
            really_gif_and_img.append(i)
    gif_and_img = really_gif_and_img
    # 删除空的内容和赋值给原来的列表
    for i in range(len(gif_and_img) - 1):
        k = i + 1
        if gif_and_img[i][0][1] != gif_and_img[k][0][1]:
            gif.append(gif_and_img[i])
        if k == len(gif_and_img) - 1:
            gif.append(gif_and_img[k])
    # 排除重复的动图和与名字不对的图片
    print("开始下载第%d页图片..." % page)
    for i in gif:
        print("开始下载第%d张图片..." % img_nums)
        path = "/home/fifa/Downloads/%s" % i[0][0]
        urllib.request.urlretrieve(i[0][1], path)
        img_nums += 1
    print("第%d页图片下载完成..." % page)

img_nums = 1
print("开始下载gif图片...")
for i in range(1, 3):
    url = "https://www.pengfu.com/index_%s.html" % i
    get_and_download_gif(url, i)
print("图片下载完成...")
