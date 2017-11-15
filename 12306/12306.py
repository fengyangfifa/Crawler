# 爬取12306
import requests
from prettytable import PrettyTable
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from termcolor import *
from train_info import get_train, get_name

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def query_train():
    from_name = get_name(input("起始地:"))
    to_name = get_name(input("目的地:"))
    time = input("时间:<格式 2017-11-12>")
    card_type = input("类型:<高铁-G, 城际-C, 直达-Z, 特快-T, 快速-K>, 默认所有按enter") or None
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(time, from_name, to_name)
    try:
        html = requests.get(url, verify=False)
        raw_trains = html.json()['data']['result']
        pt = PrettyTable()
        pt._set_field_names('车次 车站 时间 历时 一等座 二等座 软卧 硬卧 硬座 无座'.split())
        for raw_train in raw_trains:
            data_list = raw_train.split('|')
            # 车次号码
            train_no = data_list[3]
            # 出发站
            from_station_code = data_list[6]
            from_station_name = get_train(from_station_code)
            # 终点站
            to_station_code = data_list[7]
            to_station_name = get_train(to_station_code)
            # 出发时间
            start_time = data_list[8]
            # 到达时间
            arrive_time = data_list[9]
            # 总耗时
            time_fucked_up = data_list[10]
            # 一等座
            first_class_seat = data_list[31] or '--'
            # 二等座
            second_class_seat = data_list[30] or '--'
            # 软卧
            soft_sleep = data_list[23] or '--'
            # 硬卧
            hard_sleep = data_list[28] or '--'
            # 硬座
            hard_seat = data_list[29] or '--'
            # 无座
            no_seat = data_list[26] or '--'
            # 打印查询结果
            if not card_type:
                pt.add_row([
                    train_no,
                    '\n'.join([colored(from_station_name, 'green'), colored(to_station_name, 'red')]),
                    '\n'.join([colored(start_time, 'green'), colored(arrive_time, 'red')]),
                    time_fucked_up, first_class_seat,
                    second_class_seat, soft_sleep,
                    hard_sleep, hard_seat, no_seat
                ])
            else:
                if train_no[0] in card_type:
                    pt.add_row([
                        train_no,
                        '\n'.join([colored(from_station_name, 'green'), colored(to_station_name, 'red')]),
                        '\n'.join([colored(start_time, 'green'), colored(arrive_time, 'red')]),
                        time_fucked_up, first_class_seat,
                        second_class_seat, soft_sleep,
                        hard_sleep, hard_seat, no_seat
                    ])
        print(pt)
    except:
        print("查看输入格式是否错误!!!")


if __name__ == '__main__':
    query_train()
