from selenium import webdriver

browser = webdriver.Firefox()


class Item(object):
    ip = None
    port = None
    anonymous = None
    type = None
    local = None


class getproxy(object):
    def __init__(self):
        self.starturl = 'http://www.kuaidaili.com/free/inha/'
        self.urls = self.get_urls()
        self.proxylist = self.get_proxy_list(self.urls)
        self.filename = 'proxy.txt'
        self.saveFile(self.filename, self.proxylist)

    def get_urls(self):
        urls = []
        for i in range(1, 2):
            url = self.starturl + str(i)
            urls.append(url)
        return urls

    def get_proxy_list(self, urls):
        proxy_list = []

        for url in urls:
            browser.get(url)
            browser.implicitly_wait(3)
            # 找到代理table的位置
            elements = browser.find_elements_by_xpath('//tbody/tr')
            for element in elements:
                item = Item()
                item.ip = element.find_element_by_xpath('./td[1]').text
                item.port = element.find_element_by_xpath('./td[2]').text
                item.anonymous = element.find_element_by_xpath('./td[3]').text
                item.type = element.find_element_by_xpath('./td[4]').text
                item.local = element.find_element_by_xpath('./td[5]').text
                print(item.ip)
                proxy_list.append(item)
        browser.quit()
        return proxy_list

    def saveFile(self, filename, proxy_list):
        with open(filename, 'w') as f:
            for item in proxy_list:
                f.write(item.ip + '\t')
                f.write(item.port + '\t')
                f.write(item.anonymous + '\t')
                f.write(item.type + '\t')
                f.write(item.local + '\n\n')


if __name__ == '__main__':
    get = getproxy()