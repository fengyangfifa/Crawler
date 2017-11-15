# coding=utf-8
"""
获取车站名称以及对应的简写
"""
# import re
# import requests
#
#
# name_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9030'
# html = requests.get(name_url, verify=False).text
# pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)' 匹配车站名和对应的简写
# [\u4e00-\u9fa5]中文汉字的起始字以及结尾字
# result = re.findall(pattern, html)
# station = dict(result)
# print(station)


stations = {'口前': 'KQL', '华容东': 'HPN', '石柱县': 'OSW', '宝华山': 'BWH', '斜河涧': 'EEP', '夏邑县': 'EJH', '长临河': 'FVH', '湘府路': 'FVQ', '通沟': 'TOL', '朝阳镇': 'CZL', '隆化': 'UHP', '灵璧': 'GMH', '阿南庄': 'AZM', '燕子砭': 'YZY', '章丘': 'ZTK', '湛江': 'ZJZ', '奎山': 'KAB', '敖力布告': 'ALD', '石桥': 'SQE', '长冲': 'CCM', '二龙山屯': 'ELA', '白城': 'BCT', '白壁关': 'BGV', '太阳升': 'TQT', '大安北': 'RNT', '溧水': 'LDH', '弋江': 'RVH', '都格': 'DMM', '宁家': 'NVT', '兰岗': 'LNB', '马鞍山': 'MAH', '新和': 'XIR', '陆川': 'LKZ', '苏州': 'SZH', '贺州': 'HXZ', '潮汕': 'CBQ', '柳园': 'DHR', '西林': 'XYB', '襄汾': 'XFV', '乌拉山': 'WSC', '运城': 'YNV', '盘锦北': 'PBD', '白沟': 'FEP', '图强': 'TQX', '天义': 'TND', '石城': 'SCT', '香坊': 'XFB', '双峰北': 'NFQ', '南平南': 'NNS', '银瓶': 'KPQ', '桓台': 'VTK', '兴城': 'XCD', '肃宁': 'SYP', '梅州': 'MOQ', '古交': 'GJV', '葛店南': 'GNN', '凤凰城': 'FHT', '大陆号': 'DLC', '高碑店': 'GBP', '永康南': 'QUH', '北京东': 'BOP', '毛坝': 'MBY', '小河沿': 'XYD', '孝感东': 'GDN', '盘关': 'PAM', '乌奴耳': 'WRX', '莱阳': 'LYK', '石林': 'SLM', '萧县北': 'QSH', '热水': 'RSD', '长春南': 'CET', '桥西': 'QXJ', '大连西': 'GZT', '梁平': 'UQW', '红兴隆': 'VHB', '莆田': 'PTS', '孝感北': 'XJN', '正镶白旗': 'ZXC', '南宁': 'NNZ', '通州西': 'TAP', '汾河': 'FEV', '赤峰西': 'CID', '漯河西': 'LBN', '西哲里木': 'XRD', '阿尔山': 'ART', '白音胡硕': 'BCD', '秦安': 'QGJ', '昆明西': 'KXM', '水家湖': 'SQH', '垫江': 'DJE', '张家界': 'DIQ', '满洲里': 'MLX', '能家': 'NJD', '闻喜': 'WXV', '百色': 'BIZ', '新李': 'XLJ', '开江': 'KAW', '建瓯': 'JVS', '耒阳': 'LYQ', '界首市': 'JUN', '都匀': 'RYW', '上虞': 'BDH', '弥勒': 'MLM', '安康': 'AKY', '大通西': 'DTO', '犀浦东': 'XAW', '石岭': 'SOL', '眉山东': 'IUW', '嘉善': 'JSH', '文安': 'WBP', '张桥': 'ZQY', '鸳鸯镇': 'YYJ', '襄阳': 'XFN', '阳澄湖': 'AIH', '宜耐': 'YVM', '砀山南': 'PRH', '红光镇': 'IGW', '北京': 'BJP', '台前': 'TTK', '六盘水': 'UMW', '林东': 'LRC', '绩溪北': 'NRH', '万州': 'WYW', '蔡家沟': 'CJT', '开阳': 'KVW', '哈尔滨北': 'HTB', '甸心': 'DXM', '韶关东': 'SGQ', '南博山': 'NBK', '濑湍': 'LVZ', '桂林西': 'GEZ', '禄丰南': 'LQM', '新晃': 'XLQ', '石家庄': 'SJP', '黑冲滩': 'HCJ', '杏树屯': 'XDT', '义马': 'YMF', '浑河': 'HHT', '鄂尔多斯': 'EEC', '三江口': 'SKD', '洮南': 'TVT', '梁平南': 'LPE', '宝清': 'BUB', '青铜峡': 'QTJ', '金河': 'JHX', '东海': 'DHB', '南翔北': 'NEH', '集安': 'JAL', '宜春西': 'YCG', '抚松': 'FSL', '叶城': 'YER', '滁州北': 'CUH', '简阳南': 'JOW', '祁门': 'QIH', '化德': 'HGC', '北营': 'BIV', '当涂东': 'OWH', '黄流': 'KLQ', '贵阳东': 'KEW', '泗水': 'OSK', '兴安北': 'XDZ', '南京南': 'NKH', '纳雍': 'NYE', '沈阳南': 'SOT', '钟山西': 'ZAZ', '衡南': 'HNG', '同心': 'TXJ', '泽普': 'ZPR', '昌图': 'CTT', '杭锦后旗': 'HDC', '越西': 'YHW', '吴桥': 'WUP', '漳浦': 'ZCS', '郑州东': 'ZAF', '辽阳': 'LYT', '孙镇': 'OZY', '如东': 'RIH', '芙蓉南': 'KCQ', '潘家店': 'PDP', '长农': 'CNJ', '阿龙山': 'ASX', '暮云': 'KIQ', '奎屯': 'KTR', '大拟': 'DNZ', '东升': 'DRQ', '池州': 'IYH', '松树': 'SFT', '花园口': 'HYT', '钟家村': 'ZJY', '勉县': 'MVY', '黄瓜园': 'HYM', '乐昌东': 'ILQ', '江门东': 'JWQ', '孝感': 'XGN', '水泉': 'SID', '五大连池': 'WRB', '介休东': 'JDV', '通渭': 'TWJ', '霍城': 'SER', '敖汉': 'YED', '婺源': 'WYG', '长汀': 'CES', '三都县': 'KKW', '石头': 'OTB', '浮图峪': 'FYP', '临高南': 'KGQ', '白鸡坡': 'BBM', '和硕': 'VUR', '东至': 'DCH', '益阳': 'AEQ', '丹东': 'DUT', '永康': 'RFH', '醴陵': 'LLG', '宁东': 'NOJ', '兴义': 'XRZ', '廊坊北': 'LFP', '田东': 'TDZ', '察素齐': 'CSC', '安庆': 'AQH', '吴圩': 'WYZ', '怀柔北': 'HBP', '倭肯': 'WQB', '精河南': 'JIR', '兴安': 'XAZ', '牛家': 'NJB', '邵阳': 'SYQ', '钦州东': 'QDZ', '江山': 'JUH', '涞源': 'LYP', '梧州南': 'WBZ', '兑镇': 'DWV', '金坑': 'JKT', '喀什': 'KSR', '南河川': 'NHJ', '水洞': 'SIL', '红山': 'VSB', '介休': 'JXV', '万州北': 'WZE', '马鞍山东': 'OMH', '长治北': 'CBF', '杨杖子': 'YZD', '羊草': 'YAB', '宁海': 'NHH', '霍州': 'HZV', '商洛': 'OLY', '杨柳青': 'YQP', '苏家屯': 'SXT', '丹霞山': 'IRQ', '平庄': 'PZD', '卫东': 'WVT', '合阳北': 'HTY', '仪征': 'UZH', '王家营西': 'KNM', '丰水村': 'FSJ', '柳江': 'UQZ', '黄山': 'HKH', '野三坡': 'AIP', '莒县': 'JKK', '磨刀石': 'MOB', '庆阳山': 'QSJ', '青堆': 'QET', '灌水': 'GST', '汉川': 'HCN', '武夷山北': 'WBS', '绍兴东': 'SSH', '东莞': 'RTQ', '田东北': 'TBZ', '绍兴北': 'SLH', '璧山': 'FZW', '吉林': 'JLL', '海阳北': 'HEK', '绩溪县': 'JRH', '宁波东': 'NVH', '金马村': 'JMM', '沿河城': 'YHP', '姚安': 'YAC', '洞庙河': 'DEP', '梁山': 'LMK', '亭亮': 'TIZ', '陆丰': 'LLQ', '厦门北': 'XKS', '喜德': 'EDW', '泽润里': 'ZLM', '寒葱沟': 'HKB', '一面坡': 'YPB', '东京城': 'DJB', '前苇塘': 'QWP', '将乐': 'JLS', '费县': 'FXK', '安图西': 'AXL', '成高子': 'CZB', '廊坊': 'LJP', '资溪': 'ZXS', '许昌': 'XCF', '雨格': 'VTM', '涵江': 'HJS', '汪清': 'WQL', '芦潮港': 'UCH', '班猫箐': 'BNM', '中华门': 'VNH', '魏杖子': 'WKD', '临河': 'LHC', '大板': 'DBC', '宜昌东': 'HAN', '兰棱': 'LLB', '乌兰哈达': 'WLC', '祁县东': 'QGV', '定边': 'DYJ', '石林南': 'LNM', '菏泽': 'HIK', '伊宁东': 'YNR', '江永': 'JYZ', '板城': 'BUP', '长垣': 'CYF', '沙桥': 'SQM', '江桥': 'JQX', '东营': 'DPK', '镇西': 'ZVT', '盐津': 'AEW', '兴和西': 'XEC', '大成': 'DCT', '园墩': 'YAJ', '乐山': 'IVW', '遵义西': 'ZIW', '塔石嘴': 'TIM', '庆安': 'QAB', '彭阳': 'PYJ', '燕岗': 'YGW', '黄州': 'VON', '口东': 'KEQ', '德清': 'DRH', '长征': 'CZJ', '鹤壁': 'HAF', '花家庄': 'HJM', '松江镇': 'OZL', '朔州': 'SUV', '峨眉': 'EMW', '全州南': 'QNZ', '阿克苏': 'ASR', '石林西': 'SYM', '磁县': 'CIP', '汤山城': 'TCT', '迁安': 'QQP', '连云港': 'UIH', '乌龙泉南': 'WFN', '小岭': 'XLB', '黄梅': 'VEH', '常州北': 'ESH', '甘泉': 'GQY', '晏城': 'YEK', '沙后所': 'SSD', '茶陵南': 'CNG', '万宁': 'WNQ', '株洲南': 'KVQ', '额济纳': 'EJC', '福州': 'FZS', '太原': 'TYV', '建始': 'JRN', '合浦': 'HVZ', '库伦': 'KLD', '青山': 'QSB', '云东海': 'NAQ', '黄陵南': 'VLY', '大营子': 'DZD', '碧鸡关': 'BJM', '清水': 'QUJ', '新立屯': 'XLD', '长山屯': 'CVT', '锦州': 'JZD', '墨玉': 'MUR', '通远堡': 'TYT', '黄石北': 'KSN', '胜芳': 'SUP', '大青沟': 'DSD', '纸坊东': 'ZMN', '图们北': 'QSL', '缙云': 'JYH', '酉阳': 'AFW', '威海': 'WKK', '康熙岭': 'KXZ', '下板城': 'EBP', '七台河': 'QTB', '白石山': 'BAL', '南阳': 'NFF', '曹县': 'CXK', '桑根达来': 'OGC', '昭化': 'ZHW', '东戌': 'RXP', '深圳坪山': 'IFQ', '衡山西': 'HEQ', '伊图里河': 'YEX', '蚌埠南': 'BMH', '青白江东': 'QFW', '临汾': 'LFV', '新城子': 'XCT', '松滋': 'SIN', '五常': 'WCB', '安庆西': 'APH', '潞城': 'UTP', '下马塘': 'XAT', '新乡': 'XXF', '下台子': 'EIP', '旅顺': 'LST', '宽甸': 'KDT', '崇仁': 'CRG', '日喀则': 'RKO', '舍力虎': 'VLD', '崇左': 'CZZ', '天津南': 'TIP', '敦煌': 'DHJ', '灵宝': 'LBF', '南召': 'NAF', '兴宁': 'ENQ', '胶州北': 'JZK', '成吉思汗': 'CJX', '台安': 'TID', '湟源': 'HNO', '苍石': 'CST', '金华': 'JBH', '榆树': 'YRT', '桃村': 'TCK', '锦河': 'JHB', '延吉': 'YJL', '绵阳': 'MYW', '宝林': 'BNB', '霸州西': 'FOP', '高各庄': 'GGP', '永福南': 'YBZ', '盘锦': 'PVD', '南峪': 'NUP', '小扬气': 'XYX', '许三湾': 'XSJ', '马林': 'MID', '荆门': 'JMN', '三间房': 'SFX', '兴国': 'EUG', '蓟州': 'JKP', '织金北': 'ZJE', '上海南': 'SNH', '固始': 'GXN', '衡阳东': 'HVQ', '简阳': 'JYW', '溆浦南': 'EMQ', '珠海': 'ZHQ', '莱芜东': 'LWK', '天河机场': 'TJN', '苇河': 'WHB', '向塘': 'XTG', '桂林北': 'GBZ', '哈密': 'HMR', '艾河': 'AHP', '大连': 'DLT', '汐子': 'XZD', '甘旗卡': 'GQD', '福海': 'FHR', '清华园': 'QHP', '包头': 'BTC', '庙庄': 'MZJ', '金杖子': 'JYD', '普者黑': 'PZM', '咸宁': 'XNN', '菇园': 'GYL', '梁底下': 'LDP', '公主岭': 'GLT', '阳泉北': 'YPP', '信阳': 'XUN', '中宁': 'VNJ', '武夷山': 'WAS', '藤县': 'TAZ', '祁家堡': 'QBT', '五莲': 'WLK', '泗洪': 'GQH', '沈阳': 'SYT', '尚志': 'SZB', '富裕': 'FYX', '桐梓': 'TZW', '谷城': 'GCN', '昆山南': 'KNH', '塘沽': 'TGP', '加格达奇': 'JGX', '大理': 'DKM', '苍溪': 'CXE', '广宁': 'FBQ', '闽清北': 'MBS', '双流机场': 'IPW', '泉阳': 'QYL', '通途': 'TUT', '定陶': 'DQK', '瓦屋山': 'WAH', '榆树台': 'YUT', '齐齐哈尔': 'QHX', '低庄': 'DVQ', '白沙坡': 'BPM', '伊敏': 'YMX', '免渡河': 'MDX', '茶陵': 'CDG', '始兴': 'IPQ', '温岭': 'VHH', '土门子': 'TCJ', '北安': 'BAB', '株洲': 'ZZQ', '亳州': 'BZH', '军粮城北': 'JMP', '瓦房店': 'WDT', '石景山南': 'SRP', '固安': 'GFP', '石磷': 'SPB', '双辽': 'ZJD', '太原东': 'TDV', '岳池': 'AWW', '阆中': 'LZE', '阳邑': 'ARP', '五营': 'WWB', '首山': 'SAT', '从江': 'KNW', '香樟路': 'FNQ', '水洋': 'OYP', '攸县': 'YOG', '邵武': 'SWS', '襄阳东': 'XWN', '英德西': 'IIQ', '黄河景区': 'HCF', '合阳': 'HAY', '沧州': 'COP', '新帐房': 'XZX', '三营': 'OEJ', '南杂木': 'NZT', '燕郊': 'AJP', '刘家河': 'LVT', '滨海': 'FHP', '泰州': 'UTH', '昂昂溪': 'AAX', '西大庙': 'XMP', '定西北': 'DNJ', '小哨': 'XAM', '丽水': 'USH', '公主岭南': 'GBT', '陶赖昭': 'TPT', '美溪': 'MEB', '老营': 'LXL', '许家屯': 'XJT', '白涧': 'BAP', '草市': 'CSL', '万源': 'WYY', '福利屯': 'FTB', '天柱山': 'QWH', '乐清': 'UPH', '惠山': 'VCH', '商都': 'SXC', '青城山': 'QSW', '阳泉': 'AQP', '天水南': 'TIJ', '渭南北': 'WBY', '双城堡': 'SCB', '秧草地': 'YKM', '焉耆': 'YSR', '三门峡': 'SMF', '汤池': 'TCX', '新安县': 'XAF', '歙县北': 'NPH', '神头': 'SEV', '杏树': 'XSB', '福利区': 'FLJ', '哲里木': 'ZLC', '羊尾哨': 'YWM', '绅坊': 'OLH', '明光': 'MGH', '孙家': 'SUB', '新化南': 'EJQ', '勃利': 'BLB', '高山子': 'GSD', '大庆西': 'RHX', '道州': 'DFZ', '昆阳': 'KAM', '镇江': 'ZJH', '淮滨': 'HVN', '稷山': 'JVV', '阿尔山北': 'ARX', '对青山': 'DQB', '平洋': 'PYX', '枝城': 'ZCN', '天津北': 'TBP', '曾口': 'ZKE', '新江': 'XJM', '台州': 'TZH', '大石头南': 'DAL', '萍乡北': 'PBG', '呼鲁斯太': 'VTJ', '阿城': 'ACB', '太原北': 'TBV', '吐鲁番': 'TFR', '白奎堡': 'BKB', '南陵': 'LLH', '资阳': 'ZYW', '那罗': 'ULZ', '彭水': 'PHW', '五女山': 'WET', '迎宾路': 'YFW', '黄松甸': 'HDL', '皮口': 'PUT', '江油': 'JFW', '白洋淀': 'FWP', '瑞昌': 'RCG', '焦作东': 'WEF', '靖边': 'JIY', '柳园南': 'LNR', '晋城北': 'JEF', '兖州': 'YZK', '阳信': 'YVK', '大庆东': 'LFX', '汉口': 'HKN', '水富': 'OTW', '长寿湖': 'CSE', '西昌': 'ECW', '泾县': 'LOH', '宏庆': 'HEY', '滨江': 'BJB', '施家嘴': 'SHM', '偃师': 'YSF', '通道': 'TRQ', '达拉特西': 'DNC', '樟树': 'ZSG', '巩义': 'GXF', '忻州': 'XXV', '吕梁': 'LHV', '普安县': 'PUE', '南口前': 'NKT', '富川': 'FDZ', '小得江': 'EJM', '阜新南': 'FXD', '綦江': 'QJW', '定襄': 'DXV', '乌拉特前旗': 'WQC', '奇峰塔': 'QVP', '白河': 'BEL', '洛阳': 'LYF', '蒙自': 'MZM', '静海': 'JHP', '松江': 'SAH', '曲靖': 'QJM', '白山市': 'HJL', '穆棱': 'MLB', '坡底下': 'PXJ', '潮阳': 'CNQ', '镇江南': 'ZEH', '阿金': 'AJD', '孟庄': 'MZF', '自贡': 'ZGW', '吉舒': 'JSL', '资中北': 'WZW', '小东': 'XOD', '刘家店': 'UDT', '渭南': 'WNY', '郭磊庄': 'GLP', '无锡东': 'WGH', '新坪田': 'XPM', '鹤壁东': 'HFF', '金昌': 'JCJ', '小西庄': 'XXP', '滨海北': 'FCP', '宣汉': 'XHY', '精河': 'JHR', '西乡': 'XQY', '定州': 'DXP', '仙桃西': 'XAN', '清徐': 'QUV', '海坨子': 'HZT', '淮南东': 'HOH', '宜州': 'YSZ', '朗乡': 'LXB', '南口': 'NKP', '南充北': 'NCE', '黎塘': 'LTZ', '惠州': 'HCQ', '辛集': 'ENP', '平顶山西': 'BFF', '塔哈': 'THX', '隆安东': 'IDZ', '张掖西': 'ZEJ', '澧县': 'LEQ', '韩麻营': 'HYP', '阳谷': 'YIK', '舒兰': 'SLL', '归流河': 'GHT', '红江': 'HFM', '兴泉堡': 'XQJ', '小董': 'XEZ', '苍南': 'CEH', '南平北': 'NBS', '德州': 'DZP', '东通化': 'DTL', '狮山': 'KSQ', '鸡冠山': 'JST', '七营': 'QYJ', '济南东': 'JAK', '阜南': 'FNH', '高桥镇': 'GZD', '珠窝': 'ZOP', '楚雄南': 'COM', '昌乐': 'CLK', '四平': 'SPT', '永安': 'YAS', '通海': 'TAM', '龙里': 'LLW', '大口屯': 'DKP', '皇姑屯': 'HTT', '克一河': 'KHX', '中和': 'ZHX', '凌源东': 'LDD', '广德': 'GRH', '娘子关': 'NIP', '大孤山': 'RMT', '常平东': 'FQQ', '窑上': 'ASP', '小寺沟': 'ESP', '瑞安': 'RAH', '怀化南': 'KAQ', '滨州': 'BIK', '义县': 'YXD', '南芬': 'NFT', '扎鲁特': 'ZLD', '露水河': 'LUL', '礼泉': 'LGY', '千河': 'QUY', '长沙': 'CSQ', '五台山': 'WSV', '保康': 'BKD', '良各庄': 'LGP', '板塘': 'NGQ', '尚家': 'SJB', '三水南': 'RNQ', '午汲': 'WJP', '石泉县': 'SXY', '广宁寺': 'GQT', '小河镇': 'EKY', '西安北': 'EAY', '仙林': 'XPH', '庆丰': 'QFT', '东光': 'DGP', '上饶': 'SRG', '咸宁南': 'UNN', '亚布力': 'YBB', '广宁寺南': 'GNT', '文地': 'WNZ', '泊头': 'BZP', '遂平': 'SON', '威箐': 'WAM', '长阳': 'CYN', '绥德': 'ODY', '济南': 'JNK', '六枝': 'LIW', '桂林': 'GLZ', '酒泉': 'JQJ', '葵潭': 'KTQ', '辰溪': 'CXQ', '查干湖': 'VAT', '龙爪沟': 'LZT', '洛门': 'LMJ', '莱西北': 'LBK', '巢湖东': 'GUH', '索伦': 'SNT', '焦作': 'JOF', '繁峙': 'FSV', '株洲西': 'ZAQ', '潼南': 'TVW', '茂舍祖': 'MOM', '民和南': 'MNO', '葫芦岛北': 'HPD', '沙河市': 'VOP', '土地堂东': 'TTN', '仙游': 'XWS', '老城镇': 'ACQ', '红花沟': 'VHD', '邵阳北': 'OVQ', '疏勒河': 'SHJ', '西宁': 'XNO', '库车': 'KCR', '角美': 'JES', '白旗': 'BQP', '柴沟堡': 'CGV', '蔺家楼': 'ULK', '雷州': 'UAQ', '琼海': 'QYQ', '坪上': 'PSK', '通远堡西': 'TST', '红岘台': 'HTJ', '上西铺': 'SXM', '深圳北': 'IOQ', '长汀南': 'CNS', '石河子': 'SZR', '燕家庄': 'AZK', '荷塘': 'KXQ', '张辛': 'ZIP', '孝南': 'XNV', '平房': 'PFB', '沂水': 'YUK', '嘉善南': 'EAH', '临城': 'UUP', '福鼎': 'FES', '天河街': 'TEN', '安陆': 'ALN', '祁阳': 'QWQ', '莫尔道嘎': 'MRX', '衡水': 'HSP', '柏果': 'BGM', '农安': 'NAT', '喇嘛甸': 'LMX', '诏安': 'ZDS', '萍乡': 'PXG', '澄城': 'CUY', '建安': 'JUL', '裴德': 'PDB', '建阳': 'JYS', '汉源': 'WHW', '沙坡头': 'SFJ', '工农湖': 'GRT', '黄村': 'HCP', '如皋': 'RBH', '白银市': 'BNJ', '银滩': 'CTQ', '都江堰': 'DDW', '大磴沟': 'DKJ', '朱日和': 'ZRC', '大堡': 'DVT', '沧州西': 'CBP', '三家店': 'ODP', '施秉': 'AQW', '内乡': 'NXF', '汾阳': 'FAV', '兴隆镇': 'XZB', '广州南': 'IZQ', '安广': 'AGT', '青州市': 'QZK', '鄂州': 'ECN', '鲅鱼圈': 'BYT', '木里图': 'MUD', '孝西': 'XOV', '平昌': 'PCE', '中牟': 'ZGF', '德保': 'RBZ', '嘉峪关南': 'JBJ', '融水': 'RSZ', '东戴河': 'RDD', '东岔': 'DCJ', '漳州': 'ZUS', '富宁': 'FNM', '运粮河': 'YEF', '太谷西': 'TIV', '世博园': 'ZWT', '舒城': 'OCH', '五家': 'WUB', '绥棱': 'SIB', '西街口': 'EKM', '狮山北': 'NSQ', '达家沟': 'DJT', '石龙': 'SLQ', '珠斯花': 'ZHD', '大足南': 'FQW', '高村': 'GCV', '平旺': 'PWV', '格尔木': 'GRO', '新杖子': 'ERP', '荣成': 'RCK', '襄河': 'XXB', '集宁南': 'JAC', '襄垣': 'EIF', '广州西': 'GXQ', '郑州': 'ZZF', '贵定北': 'FMW', '新余': 'XUG', '郓城': 'YPK', '许家台': 'XTJ', '炎陵': 'YAG', '宝坻': 'BPP', '德伯斯': 'RDT', '康金井': 'KJB', '张维屯': 'ZWB', '林盛堡': 'LBT', '龙游': 'LMH', '青岛': 'QDK', '仁布': 'RUO', '杭州南': 'XHH', '榆中': 'IZJ', '通化': 'THL', '子长': 'ZHY', '贵定南': 'IDW', '牟平': 'MBK', '三阳川': 'SYJ', '丰都': 'FUW', '芦沟': 'LOM', '桐子林': 'TEW', '兴平': 'XPY', '土桥子': 'TQJ', '平原堡': 'PPJ', '沂南': 'YNK', '鄄城': 'JCK', '汤阴': 'TYF', '长寿': 'EFW', '乃林': 'NLD', '磐安镇': 'PAJ', '常德': 'VGQ', '聊城': 'UCK', '平度': 'PAK', '惠安': 'HNS', '昭山': 'KWQ', '吉首': 'JIQ', '彭州': 'PMW', '义乌': 'YWH', '沙沱': 'SFM', '永嘉': 'URH', '淮北': 'HRH', '平庄南': 'PND', '武穴': 'WXN', '高州': 'GSQ', '莲江口': 'LHB', '桐柏': 'TBF', '盘龙城': 'PNN', '洛湾三江': 'KRW', '城固': 'CGY', '大盘石': 'RPP', '杨陵南': 'YEY', '林源': 'LYX', '芜湖': 'WHH', '鸭园': 'YYL', '枣强': 'ZVP', '盐池': 'YKJ', '渠旧': 'QJZ', '会同': 'VTQ', '长城': 'CEJ', '桃村北': 'TOK', '白狼': 'BAT', '蓝村': 'LCK', '北台': 'BTT', '萨拉齐': 'SLC', '灵石东': 'UDV', '西乌旗': 'XWC', '扶余': 'FYT', '柳树屯': 'LSD', '邯郸': 'HDP', '彝良': 'ALW', '苏州新区': 'ITH', '漯河': 'LON', '兴隆县': 'EXP', '涡阳': 'GYH', '英吉沙': 'YIR', '商城': 'SWN', '宜宾': 'YBW', '望都': 'WDP', '查布嘎': 'CBC', '开通': 'KTT', '平社': 'PSV', '经棚': 'JPC', '皮山': 'PSR', '东明县': 'DNF', '京山': 'JCN', '遂宁': 'NIW', '永济北': 'AJV', '伊拉哈': 'YLX', '青田': 'QVH', '吴家川': 'WCJ', '延庆': 'YNP', '春阳': 'CAL', '阳新': 'YON', '北马圈子': 'BRP', '南城': 'NDG', '定南': 'DNG', '深圳': 'SZQ', '宋': 'SOB', '武夷山东': 'WCS', '旺苍': 'WEW', '宣城': 'ECH', '王团庄': 'WZJ', '郫县西': 'PCW', '牙屯堡': 'YTZ', '凯里南': 'QKW', '文登东': 'WGK', '呼兰': 'HUB', '三源浦': 'SYL', '甘泉北': 'GEY', '上万': 'SWP', '塔崖驿': 'TYP', '庙山': 'MSN', '青莲': 'QEW', '蔡家坡': 'CJY', '麻尾': 'VAW', '光山': 'GUN', '营口': 'YKT', '乐东': 'UQQ', '长甸': 'CDT', '郴州西': 'ICQ', '柳州': 'LZZ', '枝江北': 'ZIN', '官厅': 'GTP', '怀化': 'HHQ', '大关': 'RGW', '白芨沟': 'BJJ', '砀山': 'DKH', '韦庄': 'WZY', '宝拉格': 'BQC', '屏边': 'PBM', '花桥': 'VQH', '长兴南': 'CFH', '武当山': 'WRN', '靖西': 'JMZ', '虎林': 'VLB', '红安西': 'VXN', '鹰潭': 'YTG', '王瞳': 'WTP', '大湾子': 'DFM', '独山': 'RWW', '咸宁北': 'XRN', '九江': 'JJG', '吉文': 'JWX', '沙城': 'SCP', '营山': 'NUW', '榆次': 'YCV', '莎车': 'SCR', '笔架山': 'BSB', '海城西': 'HXT', '虞城县': 'IXH', '枫林': 'FLN', '安塘': 'ATV', '换新天': 'VTB', '辽中': 'LZD', '周口': 'ZKN', '东津': 'DKB', '上高镇': 'SVK', '安顺': 'ASW', '新沂': 'VIH', '沙岭子西': 'IXP', '泥河子': 'NHD', '东湾': 'DRJ', '井店': 'JFP', '黄羊镇': 'HYJ', '天镇': 'TZV', '兰陵北': 'COK', '平南南': 'PAZ', '惠州南': 'KNQ', '酒泉南': 'JNJ', '土溪': 'TSW', '晋中': 'JZV', '阳高': 'YOV', '衢州': 'QEH', '罗平': 'LPM', '叶柏寿': 'YBD', '阳朔': 'YCZ', '长沙南': 'CWQ', '临江': 'LQL', '井陉': 'JJP', '定州东': 'DOP', '古田会址': 'STS', '建宁县北': 'JCS', '烟筒山': 'YSL', '玉溪西': 'YXM', '修武': 'XWF', '攀枝花': 'PRW', '靖远西': 'JXJ', '亚布力南': 'YWB', '土贵乌拉': 'TGC', '安家': 'AJB', '肇东': 'ZDB', '杨陵': 'YSY', '莱芜西': 'UXK', '绥中': 'SZD', '清水北': 'QEJ', '铁岭西': 'PXT', '渭津': 'WJL', '汤旺河': 'THB', '韶山': 'SSQ', '彰武': 'ZWD', '海石湾': 'HSO', '子洲': 'ZZY', '泗县': 'GPH', '得耳布尔': 'DRX', '昆明': 'KMM', '惠州西': 'VXQ', '城子坦': 'CWT', '洪洞西': 'HTV', '武威南': 'WWJ', '南朗': 'NNQ', '阜阳': 'FYH', '蔡山': 'CON', '合川': 'WKW', '和田': 'VTR', '乌鲁木齐': 'WAR', '余粮堡': 'YLD', '息烽': 'XFW', '赛汗塔拉': 'SHC', '宝龙山': 'BND', '乐山北': 'UTW', '四道湾': 'OUD', '老边': 'LLT', '沐滂': 'MPQ', '新津南': 'ITW', '白音察干': 'BYC', '运城北': 'ABV', '美兰': 'MHQ', '大荔': 'DNY', '大石头': 'DSL', '北滘': 'IBQ', '开封北': 'KBF', '安化': 'PKQ', '大安': 'RAT', '珠海北': 'ZIQ', '东丰': 'DIL', '阿里河': 'AHX', '华山北': 'HDY', '沙海': 'SED', '新绛': 'XJV', '泰来': 'TLX', '东淤地': 'DBV', '铁厂': 'TCL', '怀仁': 'HRV', '瓜州': 'GZJ', '巩义南': 'GYF', '偏岭': 'PNT', '合肥北城': 'COH', '广南卫': 'GNM', '博兴': 'BXK', '槐荫': 'IYN', '荣昌': 'RCW', '谭家井': 'TNJ', '湾沟': 'WGL', '长春': 'CCT', '眉山': 'MSW', '惠农': 'HMJ', '慈利': 'CUQ', '武功': 'WGY', '溆浦': 'EPQ', '河津': 'HJV', '平岗': 'PGL', '容县': 'RXZ', '武汉': 'WHN', '大石桥': 'DQT', '白水县': 'BGY', '泉州': 'QYS', '读书铺': 'DPM', '丹东西': 'RWT', '峨眉山': 'IXW', '大禾塘': 'SOQ', '分宜': 'FYG', '吴官田': 'WGM', '开鲁': 'KLC', '青岛北': 'QHK', '岩会': 'AEP', '泡子': 'POD', '西八里': 'XLP', '那铺': 'NPZ', '南通': 'NUH', '东海县': 'DQH', '合肥南': 'ENH', '山坡东': 'SBN', '代县': 'DKV', '黑水': 'HOT', '乾安': 'QOT', '白泉': 'BQL', '涿州': 'ZXP', '南湾子': 'NWP', '织金': 'IZW', '于都': 'YDG', '耒阳西': 'LPQ', '周水子': 'ZIT', '漳平': 'ZPS', '万乐': 'WEB', '三关口': 'OKJ', '鹿道': 'LDL', '建瓯西': 'JUS', '富源': 'FYM', '巨野': 'JYK', '牡丹江': 'MDB', '田师府': 'TFT', '落垡': 'LOP', '麻城': 'MCN', '贵港': 'GGZ', '石家庄北': 'VVP', '王兆屯': 'WZB', '迤资': 'YQM', '棋子湾': 'QZQ', '桐城': 'TTH', '贺胜桥东': 'HLN', '江华': 'JHZ', '滦河沿': 'UNP', '东乡': 'DXG', '新都东': 'EWW', '黑旺': 'HWK', '银浪': 'YJX', '刀尔登': 'DRD', '安阳': 'AYF', '阿木尔': 'JTX', '兰州西': 'LAJ', '茅草坪': 'KPM', '古莲': 'GRX', '陇西': 'LXJ', '天水': 'TSJ', '汝州': 'ROF', '松原': 'VYT', '泗阳': 'MPH', '汨罗东': 'MQQ', '丹阳': 'DYH', '罗山': 'LRN', '七里河': 'QLD', '新阳镇': 'XZJ', '新晃西': 'EWQ', '河唇': 'HCZ', '灵宝西': 'LPF', '邓州': 'DOF', '江都': 'UDH', '彭山北': 'PPW', '枣庄': 'ZEK', '古城镇': 'GZB', '卫星': 'WVB', '郴州': 'CZQ', '于家堡': 'YKP', '温州南': 'VRH', '连山关': 'LGT', '南靖': 'NJS', '盐城': 'AFH', '西岗子': 'NBB', '白音他拉': 'BID', '古东': 'GDV', '秦家': 'QJB', '钟山': 'ZSZ', '湖州': 'VZH', '南充': 'NCW', '济源': 'JYF', '长武': 'CWY', '满归': 'MHX', '六道河子': 'LVP', '猛洞河': 'MUQ', '罗源': 'LVS', '新绰源': 'XRX', '中宁东': 'ZDJ', '定西': 'DSJ', '克拉玛依': 'KHR', '镇安': 'ZEY', '福山镇': 'FZQ', '松河': 'SBM', '依安': 'YAX', '镇赉': 'ZLT', '沈家河': 'OJJ', '宿松': 'OAH', '永川东': 'WMW', '建水': 'JSM', '克山': 'KSB', '七甸': 'QDM', '大方南': 'DNE', '高滩': 'GAY', '红寺堡': 'HSJ', '官高': 'GVP', '黑河': 'HJB', '山丹': 'SDJ', '西安南': 'CAY', '兰州新区': 'LQJ', '诸暨': 'ZDH', '邵家堂': 'SJJ', '太姥山': 'TLS', '潜江': 'QJN', '丰城': 'FCG', '章党': 'ZHT', '登沙河': 'DWT', '商丘': 'SQF', '灵石': 'LSV', '商河': 'SOK', '歙县': 'OVH', '兰州东': 'LVJ', '信丰': 'EFG', '东辛庄': 'DXD', '公营子': 'GYD', '北票南': 'RPD', '海拉尔': 'HRX', '包头东': 'BDC', '十渡': 'SEP', '咸阳': 'XYY', '瑞昌西': 'RXG', '锦州南': 'JOD', '密山': 'MSB', '大涧': 'DFP', '元宝山': 'YUD', '获嘉': 'HJF', '许昌东': 'XVF', '前磨头': 'QMP', '肇庆': 'ZVQ', '牛心台': 'NXT', '双吉': 'SML', '绥化': 'SHB', '柴河': 'CHB', '皮口南': 'PKT', '伊林': 'YLB', '万年': 'WWG', '凌源': 'LYD', '二道沟门': 'RDP', '双城北': 'SBB', '落坡岭': 'LPP', '林西': 'LXC', '源迁': 'AQK', '建三江': 'JIB', '布列开': 'BLR', '乌兰浩特': 'WWT', '郭家店': 'GDT', '原平': 'YPV', '旌德': 'NSH', '阿拉山口': 'AKR', '南江口': 'NDQ', '灵武': 'LNJ', '新友谊': 'EYB', '双流西': 'IQW', '武山': 'WSJ', '祁县': 'QXV', '天岗': 'TGL', '平安': 'PAL', '松桃': 'MZQ', '黄冈': 'KGN', '阳泉曲': 'YYV', '项城': 'ERN', '横沟桥东': 'HNN', '阿勒泰': 'AUR', '南观村': 'NGP', '卢龙': 'UAP', '普安': 'PAN', '天津': 'TJP', '桦南': 'HNB', '本溪': 'BXT', '汕头': 'OTQ', '微子镇': 'WQP', '鲁番': 'LVM', '大战场': 'DTJ', '盖州': 'GXT', '弓棚子': 'GPT', '范镇': 'VZK', '重庆南': 'CRW', '桑园子': 'SAJ', '太平川': 'TIT', '砚川': 'YYY', '武胜': 'WSE', '温春': 'WDB', '金华南': 'RNH', '南城司': 'NSP', '疏勒': 'SUR', '江边村': 'JBG', '莒南': 'JOK', '麦园': 'MYS', '梧州': 'WZZ', '鲘门': 'KMQ', '诸城': 'ZQK', '汝箕沟': 'RQJ', '通北': 'TBB', '滕州东': 'TEK', '抚宁': 'FNP', '五道沟': 'WDL', '尤溪': 'YXS', '灯塔': 'DGT', '涟源': 'LAQ', '永登': 'YDJ', '吉安': 'VAG', '坂田': 'BTQ', '天桥岭': 'TQL', '顺义': 'SOP', '古田北': 'GBS', '洞井': 'FWQ', '西阳村': 'XQF', '定远': 'EWH', '岐山': 'QAY', '照福铺': 'ZFM', '北屯市': 'BXR', '安口窑': 'AYY', '侯马西': 'HPV', '东镇': 'DNV', '哈拉苏': 'HAX', '广通北': 'GPM', '金沟屯': 'VGP', '西湖东': 'WDQ', '唐山北': 'FUP', '大田边': 'DBM', '北戴河': 'BEP', '栟茶': 'FWH', '邵东': 'FIQ', '济宁': 'JIK', '德阳': 'DYW', '钦州': 'QRZ', '饶阳': 'RVP', '平型关': 'PGV', '九台': 'JTL', '珲春': 'HUL', '平原': 'PYK', '日照': 'RZK', '峻德': 'JDB', '光泽': 'GZS', '江宁': 'JJH', '渑池': 'MCF', '庙城': 'MAP', '元氏': 'YSP', '娄底': 'LDQ', '绿博园': 'LCF', '重庆': 'CQW', '苏州园区': 'KAH', '海东西': 'HDO', '鹿寨北': 'LSZ', '哈尔滨西': 'VAB', '贵定县': 'KIW', '延安': 'YWY', '乌尔旗汗': 'WHX', '白银西': 'BXJ', '康庄': 'KZP', '青县': 'QXP', '马三家': 'MJT', '靖州': 'JEQ', '艾家村': 'AJJ', '宜兴': 'YUH', '淮安': 'AUH', '哈拉海': 'HIT', '湛江西': 'ZWQ', '新乡东': 'EGF', '米易': 'MMW', '三堂集': 'SDH', '左岭': 'ZSN', '玉屏': 'YZW', '背荫河': 'BYB', '湖口': 'HKG', '汤原': 'TYB', '梅河口': 'MHL', '唐河': 'THF', '石嘴山': 'QQJ', '凤州': 'FZY', '海宁': 'HNH', '泾川': 'JAJ', '藁城': 'GEP', '金宝屯': 'JBD', '隆昌北': 'NWW', '铜仁': 'RDQ', '兴隆店': 'XDD', '惠环': 'KHQ', '悬钟': 'XRP', '拉古': 'LGB', '蒲城东': 'PEY', '交城': 'JNV', '西安': 'XAY', '滦河': 'UDP', '怀仁东': 'HFV', '田心东': 'KQQ', '陵城': 'LGK', '宁安': 'NAB', '郁南': 'YKQ', '长岭子': 'CLT', '江津': 'JJW', '宿州东': 'SRH', '四合永': 'OHD', '抚远': 'FYB', '武义': 'RYH', '一间堡': 'YJT', '安靖': 'PYW', '绿化': 'LWJ', '海口': 'VUQ', '团结': 'TIX', '会昌北': 'XEG', '进贤南': 'JXG', '三水北': 'ARQ', '贵安': 'GAE', '大坝': 'DBJ', '福安': 'FAS', '海宁西': 'EUH', '嘉兴南': 'EPH', '李石寨': 'LET', '南湖东': 'NDN', '草河口': 'CKT', '犀浦': 'XIW', '中宁南': 'ZNJ', '樟木头东': 'ZRQ', '肇庆东': 'FCQ', '榆林': 'ALY', '邯郸东': 'HPP', '瓦拉干': 'WVX', '姚千户屯': 'YQT', '禹城': 'YCK', '桐乡': 'TCH', '无锡': 'WXH', '辽源': 'LYL', '抚顺北': 'FET', '泉州东': 'QRS', '通安驿': 'TAJ', '嵩明': 'SVM', '繁昌西': 'PUH', '扬州': 'YLH', '九台南': 'JNL', '苏尼特左旗': 'ONC', '二龙': 'RLD', '沃皮': 'WPT', '普雄': 'POW', '洛阳龙门': 'LLF', '昌黎': 'CLP', '枣林': 'ZIV', '玉溪': 'AXM', '羊者窝': 'AEM', '玛纳斯': 'MSR', '六安': 'UAH', '碾子山': 'NZX', '松原北': 'OCT', '连云港东': 'UKH', '句容西': 'JWH', '和什托洛盖': 'VSR', '双阳': 'OYT', '洪河': 'HPB', '姜堰': 'UEH', '霍州东': 'HWV', '前山': 'QXQ', '卓资东': 'ZDC', '唐家湾': 'PDQ', '玉门': 'YXJ', '鹤北': 'HMB', '临湘': 'LXQ', '嘉峰': 'JFF', '韩城': 'HCY', '临澧': 'LWQ', '岳家井': 'YGJ', '巢湖': 'CIH', '锡林浩特': 'XTC', '道清': 'DML', '玉泉': 'YQB', '徽县': 'HYY', '赤壁北': 'CIN', '小新街': 'XXM', '鄂州东': 'EFN', '乌鲁木齐南': 'WMR', '王杨': 'WYB', '夏石': 'XIZ', '册亨': 'CHZ', '镇平': 'ZPF', '磁山': 'CSP', '马皇': 'MHZ', '富海': 'FHX', '二连': 'RLC', '渠县': 'QRW', '阎良': 'YNY', '二道湾': 'RDX', '扎兰屯': 'ZTX', '北京西': 'BXP', '新华': 'XHB', '蚌埠': 'BBH', '庄河北': 'ZUT', '黑井': 'HIM', '西平': 'XPN', '安溪': 'AXS', '临邑': 'LUK', '凭祥': 'PXZ', '新窝铺': 'EPD', '肥东': 'FIH', '山城镇': 'SCL', '绍兴': 'SOH', '庄桥': 'ZQH', '高邑': 'GIP', '棕溪': 'ZOY', '大庆': 'DZX', '周家屯': 'ZOD', '佳木斯': 'JMB', '宜良北': 'YSM', '邹城': 'ZIK', '龙南': 'UNG', '十堰': 'SNN', '茂名': 'MDQ', '揭阳': 'JRQ', '赵城': 'ZCV', '安达': 'ADX', '鄯善': 'SSR', '重庆北': 'CUW', '白河县': 'BEY', '来宾北': 'UCZ', '抚州东': 'FDG', '新青': 'XQB', '宋城路': 'SFF', '姚渡': 'AOJ', '滁州': 'CXH', '安亭北': 'ASH', '百宜': 'FHW', '仙人桥': 'XRL', '夏官营': 'XGJ', '全椒': 'INH', '东胜': 'DOC', '乌伊岭': 'WPB', '西麻山': 'XMB', '彭泽': 'PZG', '小村': 'XEM', '伊通': 'YTL', '威虎岭北': 'WBL', '磁西': 'CRP', '高安': 'GCG', '新会': 'EFQ', '丹徒': 'RUH', '哈达铺': 'HDJ', '乐平市': 'LPG', '玉舍': 'AUM', '中山北': 'ZGQ', '昆山': 'KSH', '黄山北': 'NYH', '南昌': 'NCG', '合肥': 'HFH', '金银潭': 'JTN', '茶卡': 'CVO', '扶余北': 'FBT', '咋子': 'ZAL', '潢川': 'KCN', '阳明堡': 'YVV', '蒙自北': 'MBM', '黄羊滩': 'HGJ', '石人': 'SRL', '月山': 'YBF', '桃山': 'TAB', '长治': 'CZF', '承德东': 'CCP', '汨罗': 'MLQ', '龙塘坝': 'LBM', '冕宁': 'UGW', '平遥古城': 'PDV', '寒岭': 'HAT', '宣和': 'XWJ', '双牌': 'SBZ', '平安驿': 'PNO', '达州': 'RXW', '新肇': 'XZT', '瓦窑田': 'WIM', '平湖': 'PHQ', '深圳东': 'BJQ', '宁东南': 'NDJ', '蕲春': 'QRN', '东明村': 'DMD', '永州': 'AOQ', '武陟': 'WIF', '宣化': 'XHP', '徐州': 'XCH', '厦门高崎': 'XBS', '陶家屯': 'TOT', '旧庄窝': 'JVP', '横道河子': 'HDB', '师宗': 'SEM', '东台': 'DBH', '正定机场': 'ZHP', '海北': 'HEB', '巴中东': 'BDE', '共青城': 'GAG', '黄泥河': 'HHL', '果松': 'GSL', '拉萨': 'LSO', '南丹': 'NDZ', '大杖子': 'DAP', '永丰营': 'YYM', '大王滩': 'DZZ', '城阳': 'CEK', '双河镇': 'SEL', '枣庄西': 'ZFK', '阳岔': 'YAL', '广汉北': 'GVW', '桦林': 'HIB', '恭城': 'GCZ', '发耳': 'FEM', '醴陵东': 'UKQ', '迎春': 'YYB', '乌西': 'WXR', '修武西': 'EXF', '泰安': 'TMK', '遂溪': 'SXZ', '轮台': 'LAR', '塘豹': 'TBQ', '唐山': 'TSP', '平顶山': 'PEN', '双丰': 'OFB', '太阳山': 'TYJ', '路口铺': 'LKQ', '阳曲': 'YQV', '秀山': 'ETW', '统军庄': 'TZP', '山海关': 'SHD', '涿州东': 'ZAP', '曹子里': 'CFP', '南头': 'NOQ', '贵阳北': 'KQW', '五棵树': 'WKT', '巴彦高勒': 'BAC', '大旺': 'WWQ', '滦平': 'UPP', '先锋': 'NQQ', '大苴': 'DIM', '张兰': 'ZLV', '玉林': 'YLZ', '红彦': 'VIX', '来宾': 'UBZ', '博克图': 'BKX', '双鸭山': 'SSB', '金山屯': 'JTB', '秦皇岛': 'QTP', '韶关': 'SNQ', '新安': 'EAM', '陇南': 'INJ', '广安': 'VJW', '寿阳': 'SYV', '汉中': 'HOY', '洛阳东': 'LDF', '武隆': 'WLW', '佛山': 'FSQ', '凤凰机场': 'FJQ', '青龙山': 'QGH', '陈官营': 'CAJ', '伊宁': 'YMR', '南仇': 'NCK', '法启': 'FQE', '玉山南': 'YGG', '二营': 'RYJ', '三十里堡': 'SST', '壮志': 'ZUX', '博乐': 'BOR', '上腰墩': 'SPJ', '曲阜': 'QFK', '石坝': 'OBJ', '东方': 'UFQ', '赵光': 'ZGB', '西昌南': 'ENW', '甘草店': 'GDJ', '龙川': 'LUQ', '八仙筒': 'VXD', '上海西': 'SXH', '松江河': 'SJL', '韶山南': 'INQ', '雁翅': 'YAP', '浠水': 'XZN', '树木岭': 'FMQ', '鹤岗': 'HGB', '羊臼河': 'YHM', '罗城': 'VCZ', '普宁': 'PEQ', '南曹': 'NEF', '元谋': 'YMM', '抚州': 'FZG', '高花': 'HGD', '大杨树': 'DUX', '扎赉诺尔西': 'ZXX', '打柴沟': 'DGJ', '德安': 'DAG', '南平': 'NPS', '绥阳': 'SYB', '布海': 'BUT', '郯城': 'TZK', '拉哈': 'LHX', '开原': 'KYT', '达拉特旗': 'DIC', '南京': 'NJH', '三井子': 'OJT', '瑞金': 'RJG', '金城江': 'JJZ', '华城': 'VCQ', '吐列毛杜': 'TMD', '三江县': 'SOZ', '光明城': 'IMQ', '陵水': 'LIQ', '林口': 'LKB', '河间西': 'HXP', '米沙子': 'MST', '霍林郭勒': 'HWD', '清河门': 'QHD', '哈尔滨': 'HBB', '赤壁': 'CBN', '弋阳': 'YIG', '新邱': 'XQD', '王安镇': 'WVP', '应县': 'YZV', '马兰': 'MLR', '六盘山': 'UPJ', '驼腰岭': 'TIL', '郑州西': 'XPF', '信阳东': 'OYN', '长葛': 'CEF', '樟木头': 'ZOQ', '安仁': 'ARG', '三十家': 'SRD', '白沙铺': 'BSN', '北京北': 'VAP', '同江': 'TJB', '龙华': 'LHP', '两家': 'UJT', '河源': 'VIQ', '巴山': 'BAY', '蒲城': 'PCY', '超梁沟': 'CYP', '阿图什': 'ATR', '明水河': 'MUT', '杨树岭': 'YAD', '宁武': 'NWV', '白马井': 'BFQ', '上板城': 'SBP', '利津南': 'LNK', '高密': 'GMK', '浩良河': 'HHB', '宜春': 'YEG', '南昌西': 'NXG', '清河': 'QIP', '宁波': 'NGH', '内江': 'NJW', '图里河': 'TEX', '保定': 'BDP', '瓢儿屯': 'PRT', '尼木': 'NMO', '太平镇': 'TEB', '大兴沟': 'DXL', '凤阳': 'FUH', '里木店': 'LMB', '新兴县': 'XGQ', '凯里': 'KLW', '富锦': 'FIB', '清涧县': 'QNY', '清远': 'QBQ', '沁阳': 'QYF', '金山北': 'EGH', '渠黎': 'QLZ', '漳州东': 'GOS', '普湾': 'PWT', '魏善庄': 'WSP', '公庙子': 'GMC', '呼和浩特': 'HHC', '河口南': 'HKJ', '信宜': 'EEQ', '新保安': 'XAP', '南华北': 'NHS', '尖峰': 'PFQ', '榆树屯': 'YSX', '南木': 'NMX', '宣威': 'XWM', '大雁': 'DYX', '平凉南': 'POJ', '九三': 'SSX', '德惠': 'DHT', '凤城东': 'FDT', '杭州': 'HZH', '蓬安': 'PAW', '昌平': 'CPP', '临泽南': 'LDJ', '福山口': 'FKP', '福泉': 'VMW', '田阳': 'TRZ', '大同': 'DTV', '化州': 'HZZ', '六合': 'KLH', '百浪': 'BRZ', '南关岭': 'NLT', '镜铁山': 'JVJ', '北碚': 'BPW', '大余': 'DYG', '虎门': 'IUQ', '柳河': 'LNL', '豆庄': 'ROP', '涉县': 'OEP', '兰考南': 'LUF', '福州南': 'FYS', '泰和': 'THG', '小市': 'XST', '五道河': 'WHP', '广汉': 'GHW', '近海': 'JHD', '秦岭': 'QLY', '黄陵': 'ULY', '白水镇': 'BUM', '前锋': 'QFB', '大元': 'DYZ', '虢镇': 'GZY', '安图': 'ATL', '海湾': 'RWH', '西柳': 'GCT', '来舟': 'LZS', '岷县': 'MXJ', '铜陵': 'TJH', '那曲': 'NQO', '临西': 'UEP', '云霄': 'YBS', '沈阳北': 'SBT', '乐都': 'LDO', '李家坪': 'LIJ', '曲水县': 'QSO', '大石寨': 'RZT', '漳县': 'ZXJ', '陇县': 'LXY', '白水江': 'BSY', '小金口': 'NKQ', '芨岭': 'JLJ', '龙井': 'LJL', '大英东': 'IAW', '朝阳川': 'CYL', '云居寺': 'AFP', '茅岭': 'MLZ', '武清': 'WWP', '大连北': 'DFT', '三亚': 'SEQ', '西峡': 'XIF', '弥渡': 'MDF', '桥头': 'QAT', '烟筒屯': 'YUX', '闽清': 'MQS', '海阳': 'HYK', '余姚北': 'CTH', '山阴': 'SNV', '褚家湾': 'CWJ', '龙骨甸': 'LGM', '常州': 'CZH', '贲红': 'BVC', '长坡岭': 'CPM', '永济': 'YIV', '南阳寨': 'NYF', '太原南': 'TNV', '资中': 'ZZW', '息县': 'ENN', '江所田': 'JOM', '娄底南': 'UOQ', '临沂': 'LVK', '新乐': 'ELP', '临汾西': 'LXV', '永泰': 'YTS', '三汇镇': 'OZW', '扶绥': 'FSZ', '葫芦岛': 'HLD', '杜家': 'DJL', '三穗': 'QHW', '喀喇其': 'KQX', '邳州': 'PJH', '泰山': 'TAK', '富拉尔基': 'FRX', '武威': 'WUJ', '神州': 'SRQ', '曲阜东': 'QAK', '丽江': 'LHM', '钟祥': 'ZTN', '徘徊北': 'PHP', '固镇': 'GEH', '平关': 'PGM', '花棚子': 'HZM', '月亮田': 'YUM', '东港北': 'RGT', '长春西': 'CRT', '南大庙': 'NMP', '新县': 'XSN', '台安南': 'TAD', '德令哈': 'DHO', '牙克石': 'YKX', '紫荆关': 'ZYP', '霸州': 'RMP', '民乐': 'MBJ', '杨林': 'YLM', '驻马店西': 'ZLN', '武昌': 'WCN', '南宫东': 'NFP', '阿克陶': 'AER', '三明': 'SMS', '凤县': 'FXY', '鞍山': 'AST', '海安县': 'HIH', '老府': 'UFD', '古浪': 'GLJ', '向阳': 'XDB', '西小召': 'XZC', '海城': 'HCT', '峡江': 'EJG', '平安镇': 'PZT', '东': 'FDC', '石峡子': 'SXJ', '白音华南': 'FNC', '新华屯': 'XAX', '成都南': 'CNW', '神木': 'OMY', '华家': 'HJT', '乳山': 'ROK', '东来': 'RVD', '贵溪': 'GXG', '朱家沟': 'ZUB', '宁陵县': 'NLF', '克东': 'KOB', '东二道河': 'DRB', '门源': 'MYO', '呼和浩特东': 'NDC', '盖州西': 'GAT', '杨村': 'YBP', '平遥': 'PYV', '临沂北': 'UYK', '罗江东': 'IKW', '花山南': 'KNN', '广水': 'GSN', '阳平关': 'YAY', '建湖': 'AJH', '荣昌北': 'RQW', '松江南': 'IMH', '濮阳': 'PYF', '前进镇': 'QEB', '北流': 'BOZ', '无为': 'IIH', '渭南镇': 'WNJ', '黄柏': 'HBL', '歪头山': 'WIT', '江宁西': 'OKH', '仲恺': 'KKQ', '岔江': 'CAM', '上园': 'SUD', '东胜西': 'DYC', '开封': 'KFF', '田林': 'TFZ', '丰顺': 'FUQ', '宝鸡南': 'BBY', '永安乡': 'YNB', '鸡东': 'JOB', '佛山西': 'FOQ', '新林': 'XPX', '大巴': 'DBD', '华容': 'HRN', '枣庄东': 'ZNK', '八面城': 'BMD', '容桂': 'RUQ', '龙泉寺': 'UQJ', '湘潭': 'XTQ', '顺德': 'ORQ', '五龙背东': 'WMT', '内江北': 'NKW', '宁国': 'NNH', '高邑西': 'GNP', '霍尔果斯': 'HFR', '华山': 'HSY', '玉山': 'YNG', '商南': 'ONY', '小榄': 'EAQ', '怀集': 'FAQ', '吴堡': 'WUY', '广州': 'GZQ', '南部': 'NBE', '花湖': 'KHN', '顺德学院': 'OJQ', '柞水': 'ZSY', '孙吴': 'SKB', '绥中北': 'SND', '抚顺': 'FST', '崔黄口': 'CHP', '融安': 'RAZ', '富县': 'FEY', '友好': 'YOB', '吴家屯': 'WJT', '上板城南': 'OBP', '龙市': 'LAG', '安平': 'APT', '黄花筒': 'HUD', '文水': 'WEV', '滦县': 'UXP', '大屯': 'DNT', '新松浦': 'XOB', '八面通': 'BMB', '德昌': 'DVW', '衡阳': 'HYQ', '卓资山': 'ZZC', '沙岭子': 'SLP', '汉阴': 'HQY', '马龙': 'MGM', '恩施': 'ESN', '卧里屯': 'WLX', '宁明': 'NMZ', '南雄': 'NCQ', '奈曼': 'NMD', '漫水湾': 'MKW', '草海': 'WBW', '长庆桥': 'CQJ', '花园': 'HUN', '三家寨': 'SMM', '曾家坪子': 'ZBW', '平田': 'PTM', '南台': 'NTT', '贵定': 'GTW', '麻山': 'MAB', '都匀东': 'KJW', '中卫': 'ZWJ', '磁窑': 'CYK', '盘山': 'PUD', '和龙': 'HLL', '华容南': 'KRN', '荆州': 'JBN', '上海': 'SHH', '沈家': 'OJB', '侯马': 'HMV', '瓦房店西': 'WXT', '小雨谷': 'XHM', '茂名西': 'MMZ', '文昌': 'WEQ', '鼎湖东': 'UWQ', '芷江': 'ZPQ', '成都': 'CDW', '库尔勒': 'KLR', '赣州': 'GZG', '金寨': 'JZH', '熊岳城': 'XYT', '白河东': 'BIY', '岳阳东': 'YIQ', '五五': 'WVR', '高平': 'GPF', '赶水': 'GSW', '黄石东': 'OSN', '红安': 'HWN', '创业村': 'CEX', '和平': 'VAQ', '新郑机场': 'EZF', '海伦': 'HLB', '天祝': 'TZJ', '渭源': 'WEJ', '甲山': 'JOP', '龙洞堡': 'FVW', '鼎湖山': 'NVQ', '民权': 'MQF', '渑池南': 'MNF', '崖州': 'YUQ', '山市': 'SQB', '柳林南': 'LKV', '风陵渡': 'FLV', '渭南南': 'WVY', '四方台': 'STB', '楚山': 'CSB', '老莱': 'LAX', '泰宁': 'TNS', '大虎山': 'DHD', '十家子': 'SJD', '杨岗': 'YRB', '辰清': 'CQB', '防城港北': 'FBZ', '淮南': 'HAH', '广州东': 'GGQ', '岢岚': 'KLV', '甘河': 'GAX', '皋兰': 'GEJ', '鹰潭北': 'YKG', '汝阳': 'RYF', '进贤': 'JUG', '玛纳斯湖': 'MNR', '山河屯': 'SHL', '八步': 'BBE', '三河县': 'OXP', '乌兰察布': 'WPC', '安龙': 'AUZ', '缙云西': 'PYH', '小月旧': 'XFM', '汤逊湖': 'THN', '周家': 'ZOB', '亚': 'JUQ', '陈相屯': 'CXT', '偏店': 'PRP', '蛟河西': 'JOL', '紫阳': 'ZVY', '中山': 'ZSQ', '黔江': 'QNW', '郫县': 'PWW', '安多': 'ADO', '安德': 'ARW', '抚州北': 'FBG', '富县东': 'FDY', '平山': 'PSB', '三水': 'SJQ', '咸宁东': 'XKN', '鹤庆': 'HQM', '建昌': 'JFD', '芦台': 'LTP', '嘉峪关': 'JGJ', '碧江': 'BLQ', '祥云': 'EXM', '岱岳': 'RYV', '丹阳北': 'EXH', '五寨': 'WZV', '云彩岭': 'ACP', '昆都仑召': 'KDC', '大灰厂': 'DHP', '金月湾': 'PYQ', '丰城南': 'FNG', '司家岭': 'OLK', '明港东': 'MDN', '怀柔': 'HRP', '南宁西': 'NXZ', '沙河': 'SHP', '徐闻': 'XJQ', '朱家窑': 'ZUJ', '端州': 'WZQ', '黑台': 'HQB', '孤家子': 'GKT', '冷水江东': 'UDQ', '轩岗': 'XGV', '三江南': 'SWZ', '廉江': 'LJZ', '峨边': 'EBW', '晋江': 'JJS', '永定': 'YGS', '沙河口': 'SKT', '华蓥': 'HUW', '保定东': 'BMP', '北井子': 'BRT', '和静': 'HJR', '暖泉': 'NQJ', '榆社': 'YSV', '四会': 'AHQ', '康城': 'KCP', '鹰手营子': 'YIP', '嘎什甸子': 'GXD', '横峰': 'HFG', '旬阳': 'XUY', '乾县': 'QBY', '丹凤': 'DGY', '大平房': 'DPD', '长汀镇': 'CDB', '前卫': 'QWD', '官厅西': 'KEP', '黄冈东': 'KAN', '上海虹桥': 'AOH', '龙江': 'LJX', '玉田县': 'ATP', '鳌江': 'ARH', '临川': 'LCG', '威海北': 'WHK', '塔河': 'TXX', '三门县': 'OQH', '兴业': 'SNZ', '马桥河': 'MQB', '昌平北': 'VBP', '邢台东': 'EDP', '一面山': 'YST', '帽儿山': 'MRB', '骆驼巷': 'LTJ', '兰州': 'LZJ', '福田': 'NZQ', '文登': 'WBK', '丰镇': 'FZC', '深州': 'OZP', '普定': 'PGW', '威舍': 'WSM', '九郎山': 'KJQ', '神池': 'SMV', '东庄': 'DZV', '临泽': 'LEJ', '汉寿': 'VSQ', '井冈山': 'JGG', '明城': 'MCL', '湘乡': 'XXQ', '三原': 'SAY', '新津': 'IRW', '余江': 'YHG', '德兴': 'DWG', '深圳西': 'OSQ', '宝泉岭': 'BQB', '李家': 'LJB', '石人城': 'SRB', '石门县北': 'VFQ', '青神': 'QVW', '离堆公园': 'INW', '孤山口': 'GSP', '营口东': 'YGT', '吐哈': 'THR', '榆树沟': 'YGP', '高楼房': 'GFM', '夹心子': 'JXT', '朝阳': 'CYD', '哈尔滨东': 'VBB', '洪洞': 'HDV', '新余北': 'XBG', '大兴': 'DXX', '建设': 'JET', '三道湖': 'SDL', '安定': 'ADP', '昆明南': 'KOM', '巨宝': 'JRT', '三明北': 'SHS', '石梯': 'STE', '庆盛': 'QSQ', '临清': 'UQK', '龙丰': 'KFQ', '毛坝关': 'MGY', '带岭': 'DLB', '阳春': 'YQQ', '中川机场': 'ZJJ', '溧阳': 'LEH', '阿巴嘎旗': 'AQC', '南岔': 'NCB', '燕山': 'AOP', '榕江': 'RVW', '天门南': 'TNN', '阳城': 'YNF', '泰康': 'TKX', '棠海': 'THM', '麻城北': 'MBN', '井南': 'JNP', '嫩江': 'NGX', '庙岭': 'MLL', '王家湾': 'WJJ', '德清西': 'MOH', '徐州东': 'UUH', '嵯岗': 'CAX', '百里峡': 'AAP', '纪家沟': 'VJD', '卫辉': 'WHF', '昭通': 'ZDW', '东边井': 'DBB', '乌海': 'WVC', '德惠西': 'DXT', '库都尔': 'KDX', '旬阳北': 'XBY', '贺家店': 'HJJ', '吐鲁番北': 'TAR', '英德': 'YDQ', '铜仁南': 'TNW', '关林': 'GLF', '后湖': 'IHN', '朝阳地': 'CDD', '民权北': 'MIF', '新干': 'EGG', '晋城': 'JCF', '南宁东': 'NFZ', '巴楚': 'BCR', '漠河': 'MVX', '石山': 'SAD', '下花园': 'XYP', '太湖': 'TKH', '余杭': 'EVH', '海林': 'HRB', '岳阳': 'YYQ', '通化县': 'TXL', '北海': 'BHZ', '干塘': 'GNJ', '樟树东': 'ZOG', '五府山': 'WFG', '竹园坝': 'ZAW', '神树': 'SWB', '彬县': 'BXY', '火连寨': 'HLT', '常平': 'DAQ', '天门': 'TMN', '曲江': 'QIM', '富源北': 'FBM', '应城': 'YHN', '东方红': 'DFB', '黄冈西': 'KXN', '河边': 'HBV', '张家口南': 'ZMP', '永郎': 'YLW', '源潭': 'YTQ', '龙镇': 'LZA', '根河': 'GEX', '大埔': 'DPI', '兰考': 'LKF', '云浮东': 'IXQ', '宜昌': 'YCN', '三义井': 'OYD', '铜陵北': 'KXH', '东安东': 'DCZ', '永修': 'ACG', '滕州': 'TXK', '衡山': 'HSQ', '晨明': 'CMB', '韩府湾': 'HXJ', '安阳东': 'ADF', '李旺': 'VLJ', '西固城': 'XUJ', '饶平': 'RVQ', '合肥西': 'HTH', '高碑店东': 'GMP', '成都东': 'ICW', '广州北': 'GBQ', '大丰': 'KRQ', '商丘南': 'SPF', '曲靖北': 'QBM', '黎城': 'UCP', '亮甲店': 'LRT', '干沟': 'GGL', '师庄': 'SNM', '大冶北': 'DBN', '顺昌': 'SCS', '坪石': 'PSQ', '龙里北': 'KFW', '米脂': 'MEY', '连江': 'LKS', '秦家庄': 'QZV', '官字井': 'GOT', '确山': 'QSN', '春湾': 'CQQ', '西固': 'XIJ', '随州': 'SZN', '云山': 'KZQ', '颍上': 'YVH', '大营镇': 'DJP', '巴东': 'BNN', '四平东': 'PPT', '临海': 'UFH', '葛根庙': 'GGT', '香兰': 'XNB', '车转湾': 'CWM', '虎什哈': 'HHP', '索图罕': 'SHX', '南桥': 'NQD', '水源': 'OYJ', '孟家岗': 'MGB', '沈阳东': 'SDT', '姜家': 'JJB', '甘洛': 'VOW', '沥林北': 'KBQ', '沟帮子': 'GBD', '铁岭': 'TLT', '银川': 'YIJ', '张家口': 'ZKP', '南芬北': 'NUT', '广南县': 'GXM', '齐齐哈尔南': 'QNB', '石门县': 'OMQ', '关岭': 'GLE', '祁阳北': 'QVQ', '广元': 'GYW', '张百湾': 'ZUP', '龙嘉': 'UJL', '晋州': 'JXP', '万发屯': 'WFB', '西丰': 'XFT', '旗下营': 'QXC', '霞浦': 'XOS', '鲁山': 'LAF', '平坝南': 'PBE', '龙岩': 'LYS', '北宅': 'BVP', '洋河': 'GTH', '汕尾': 'OGQ', '莱西': 'LXK', '兴凯': 'EKB', '博鳌': 'BWQ', '张掖': 'ZYJ', '徐水': 'XSP', '闵集': 'MJN', '济南西': 'JGK', '武义北': 'WDH', '红果': 'HEM', '豆张庄': 'RZP', '大其拉哈': 'DQX', '三合庄': 'SVP', '阜宁': 'AKH', '霍邱': 'FBH', '两当': 'LDY', '庐江': 'UJH', '昌图西': 'CPT', '松树镇': 'SSL', '深井子': 'SWT', '本溪湖': 'BHT', '永城北': 'RGH', '景泰': 'JTJ', '宝鸡': 'BJY', '余姚': 'YYH', '烟台南': 'YLK', '大红旗': 'DQD', '麻阳': 'MVQ', '襄汾西': 'XTV', '平峪': 'PYP', '金州': 'JZT', '龙山镇': 'LAS', '密云北': 'MUP', '滴道': 'DDB', '鸡西': 'JXB', '贵阳': 'GIW', '武安': 'WAP', '羊堡': 'ABM', '流水沟': 'USP', '葡萄菁': 'PTW', '长兴': 'CBH', '甘谷': 'GGJ', '镇远': 'ZUW', '新化': 'EHQ', '章古台': 'ZGD', '乌海西': 'WXC', '杭州东': 'HGH', '温州': 'RZH', '博白': 'BBZ', '涪陵': 'FLW', '承德': 'CDP', '沙湾县': 'SXR', '东莞东': 'DMQ', '蛟河': 'JHL', '新立镇': 'XGT', '招柏': 'ZBP', '立志': 'LZX', '临颍': 'LNF', '广元南': 'GAW', '雁荡山': 'YGH', '普兰店': 'PLT', '上杭': 'JBS', '靖远': 'JYJ', '江源': 'SZL', '青龙': 'QIB', '宾阳': 'UKZ', '二密河': 'RML', '什里店': 'OMP', '海口东': 'HMQ', '乐昌': 'LCQ', '明珠': 'MFQ', '尼勒克': 'NIR', '岑溪': 'CNZ', '开原西': 'KXT', '黄口': 'KOH', '即墨北': 'JVK', '豆罗': 'DLV', '伊尔施': 'YET', '图们': 'TML', '治安': 'ZAD', '淄博': 'ZBK', '绥芬河': 'SFB', '零陵': 'UWZ', '任丘': 'RQP', '资阳北': 'FYW', '东营南': 'DOK', '平凉': 'PIJ', '沭阳': 'FMH', '冠豸山': 'GSS', '北京南': 'VNP', '淮安南': 'AMH', '福清': 'FQS', '湘潭北': 'EDQ', '永川': 'YCW', '桂平': 'GAZ', '宁德': 'NES', '潍坊': 'WFK', '营盘水': 'YZJ', '永乐店': 'YDY', '鹤立': 'HOB', '范家屯': 'FTT', '绕阳河': 'RHD', '宁村': 'NCZ', '拉林': 'LAB', '彭山': 'PSW', '驻马店': 'ZDN', '五龙背': 'WBT', '石桥子': 'SQT', '奉化': 'FHH', '烟台': 'YAK', '高台南': 'GAJ', '祁东北': 'QRQ', '陆良': 'LRM', '永寿': 'ASY', '潼关': 'TGY', '鄯善北': 'SMR', '茂林': 'MLD', '拉鲊': 'LEM', '通辽': 'TLD', '惠东': 'KDQ', '王岗': 'WGB', '大武口': 'DFJ', '当阳': 'DYN', '八达岭': 'ILP', '石岘': 'SXL', '厦门': 'XMS', '固原': 'GUJ', '大营': 'DYV', '苏州北': 'OHH', '中寨': 'ZZM', '三门峡南': 'SCF', '柴岗': 'CGT', '祁东': 'QMQ', '林海': 'LXX', '梨树镇': 'LSB', '沁县': 'QVV', '嘉祥': 'JUK', '德州东': 'DIP', '亚龙湾': 'TWQ', '云梦': 'YMN', '安顺西': 'ASE', '河口北': 'HBM', '靖宇': 'JYL', '五原': 'WYC', '镇城底': 'ZDV', '南江': 'FIW', '太谷': 'TGV', '旗下营南': 'QNC', '咸阳秦都': 'XOY', '嘉兴': 'JXH', '景德镇': 'JCG', '磐石': 'PSL', '天津西': 'TXP', '马莲河': 'MHB', '复盛': 'FAW', '鹿寨': 'LIZ', '庐山': 'LSG', '巴林': 'BLX', '邢台': 'XTP', '巴中': 'IEW', '大官屯': 'DTT', '大竹园': 'DZY', '潮州': 'CKQ', '古田': 'GTS', '平泉': 'PQP', '到保': 'RBT', '广安南': 'VUW', '虎石台': 'HUT', '六合镇': 'LEX', '冯屯': 'FTX', '北屯': 'BYP', '沙县': 'SAS', '白云鄂博': 'BEC', '涪陵北': 'FEW', '清河城': 'QYP', '灵丘': 'LVV', '无锡新区': 'IFH', '平邑': 'PIK', '闻喜西': 'WOV', '红砂岘': 'VSJ', '下社': 'XSV', '苇子沟': 'WZL', '尹地': 'YDM', '南丰': 'NFG', '土牧尔台': 'TRC', '敦化': 'DHL', '独立屯': 'DTX', '八角台': 'BTD', '凌海': 'JID', '高台': 'GTJ', '贾鲁河': 'JLF', '龙沟': 'LGJ', '狼尾山': 'LRJ', '隆昌': 'LCW', '沈丘': 'SQN', '新民': 'XMD', '武乡': 'WVV', '营街': 'YAM', '讷河': 'NHX', '正定': 'ZDP', '三门峡西': 'SXF', '谢家镇': 'XMT', '略阳': 'LYY', '延吉西': 'YXL', '胶州': 'JXK', '丰乐镇': 'FZB', '五叉沟': 'WCT', '红星': 'VXB', '芦溪': 'LUG', '平台': 'PVT', '毛陈': 'MHN', '攸县南': 'YXG', '营城子': 'YCT', '长寿北': 'COW', '铁力': 'TLB', '利川': 'LCN', '玉石': 'YSJ', '低窝铺': 'DWJ', '本溪新城': 'BVT', '开安': 'KAT', '黄石': 'HSN', '平河口': 'PHM', '赤峰': 'CFD', '塔尔气': 'TVX', '乐都南': 'LVO', '汉沽': 'HGP', '盘州': 'PAE', '乐善村': 'LUM', '姚家': 'YAT', '宁乡': 'NXQ', '海龙': 'HIL', '古镇': 'GNQ', '常庄': 'CVK', '戚墅堰': 'QYH', '清原': 'QYT', '徐家': 'XJB', '革居': 'GEM', '平果': 'PGZ', '明港': 'MGN', '伊春': 'YCB', '罗江': 'LJW', '枣阳': 'ZYN', '大林': 'DLD', '王府': 'WUT', '千阳': 'QOY', '鞍山西': 'AXT', '宜城': 'YIN', '下城子': 'XCB', '兰溪': 'LWH', '宿州': 'OXH'}
# 车站简写和对应的中文名称

def get_train(name):
    # 通过车站简写获取车站中文名
    for m, n in stations.items():
        if name == n:
            return m


def get_name(train):
    # 通过车站中文名获取车站简写
    for m, n in stations.items():
        if train == m:
            return n
