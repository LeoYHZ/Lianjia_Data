# -*- coding:utf-8 -*-

import requests
from lxml import etree
import random
import pandas as pd


class LianHome:
    def __init__(self, city):
        self.url = "https://" + city +".lianjia.com/ershoufang/pg{}/"
        self.headers = [
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
            },
            {
                "User-Agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"
            }
        ]
        self.city = city
        self.urls = [self.url.format(i) for i in range(1, 10, 1)]
        self.datas = list()

    def get_request(self, url):
        header = self.headers[random.randint(0, 1)]
        response = requests.get(url=url, headers=header)
        return response.content

    def parse_data(self, index, saver):
        next(saver)
        index_obj = etree.HTML(index)
        results = index_obj.xpath('//li[@class="clear LOGCLICKDATA" or @class="clear LOGVIEWDATA LOGCLICKDATA"]//div[@class="info clear"]')
        for result in results:
            home_dict = dict()
            home_dict["title"] = result.xpath('./div[@class="title"]/a/text()')[0]
            home_dict["url"] = result.xpath('./div[@class="title"]/a/@href')[0]
            home_dict["location"] = "".join(result.xpath('./div[@class="flood"]//a/text()'))
            base = result.xpath('.//div[@class="houseInfo"]/text()')[0].split(" | ")
            home_dict["layer"] = base[0]
            home_dict["area"] = float(base[1][0:-2])
            home_dict["direction"] = base[2]
            try:
                home_dict["price_all"] = float(result.xpath('./div[@class="priceInfo"]//span/text()')[0])
                home_dict["price_ave"] = int(result.xpath('./div[@class="priceInfo"]//span/text()')[1][0:-3].replace(",", ""))
            except ValueError:
                continue
            self.datas.append(home_dict)
            print("Get：" + self.datas[-1]["title"])
            saver.send(self.datas[-1])
            self.datas = list()

    def save_data(self):
        while True:
            n = yield
            if not n:
                return
            df = pd.DataFrame([n], columns=['title', 'url', 'location', 'layer', 'area', 'direction', 'price_all', 'price_ave'])
            df.to_csv( './home/' + self.city + '.csv', encoding="utf-8-sig", index=False ,header=0, mode='a')

    def run(self):
        for url in self.urls:
            response = self.get_request(url)
            c = self.save_data()
            self.parse_data(response,c)


if __name__ == "__main__":
    city_name_dic = {"aq": "安庆", "cz.fang": "滁州", "fy": "阜阳", "hf": "合肥", "mas": "马鞍山", "wuhu": "芜湖", "bj": "北京", "cq": "重庆", "fz": "福州", "quanzhou": "泉州", "xm": "厦门", "zhangzhou": "漳州", "dg": "东莞", "fs": "佛山", "gz": "广州", "hui": "惠州", "jiangmen": "江门", "qy": "清远", "sz": "深圳", "zh": "珠海", "zhanjiang": "湛江", "zs": "中山", "bh": "北海", "fcg": "防城港", "gl": "桂林", "liuzhou": "柳州", "nn": "南宁", "gy": "贵阳", "qxn.fang": "黔西南", "lz": "兰州", "tianshui": "天水", "bd": "保定", "chengde": "承德", "hd": "邯郸", "lf": "廊坊", "qhd.fang": "秦皇岛", "sjz": "石家庄", "ts": "唐山", "zjk": "张家口", "bt.fang": "保亭", "cm": "澄迈", "dz.fang": "儋州", "hk": "海口", "lg.fang": "临高", "ld.fang": "乐东", "ls.fang": "陵水", "qh.fang": "琼海", "san": "三亚", "wzs.fang": "五指山", "wc.fang": "文昌", "wn.fang": "万宁", "cs": "长沙", "changde": "常德", "xx": "湘西", "yy": "岳阳", "zhuzhou": "株洲", "jiyuan.fang": "济源", "kf": "开封", "luoyang": "洛阳", "pds": "平顶山", "py": "濮阳", "smx.fang": "三门峡", "xinxiang": "新乡", "xc": "许昌", "zz": "郑州", "zk": "周口", "zmd": "驻马店", "ez": "鄂州", "huangshi": "黄石", "wh": "武汉", "xy": "襄阳", "yichang": "宜昌", "hrb": "哈尔滨", "ganzhou": "赣州", "jiujiang": "九江", "jian": "吉安", "nc": "南昌", "sr": "上饶", "changzhou": "常州", "changshu": "常熟", "danyang": "丹阳", "haimen": "海门", "ha": "淮安", "jy": "江阴", "jr": "句容", "ks": "昆山", "nj": "南京", "nt": "南通", "su": "苏州", "taicang": "太仓", "wx": "无锡", "xz": "徐州", "yc": "盐城", "zj": "镇江", "cc": "长春", "jl": "吉林", "dl": "大连", "dd": "丹东", "fushun": "抚顺", "sy": "沈阳", "baotou": "包头", "byne.fang": "巴彦淖尔", "cf": "赤峰", "hhht": "呼和浩特", "tongliao": "通辽", "yinchuan": "银川", "heze": "菏泽", "jn": "济南", "jining": "济宁", "linyi": "临沂", "qd": "青岛", "ta": "泰安", "wf": "潍坊", "weihai": "威海", "yt": "烟台", "zb": "淄博", "cd": "成都", "dy": "德阳", "dazhou": "达州", "guangyuan": "广元", "leshan.fang": "乐山", "liangshan": "凉山", "mianyang": "绵阳", "ms.fang": "眉山", "nanchong": "南充", "pzh": "攀枝花", "sn": "遂宁", "yibin": "宜宾", "yaan": "雅安", "ziyang": "资阳", "baoji": "宝鸡", "hanzhong": "汉中", "xa": "西安", "xianyang": "咸阳", "jz": "晋中", "ty": "太原", "yuncheng": "运城", "sh": "上海", "tj": "天津", "wlmq": "乌鲁木齐", "dali": "大理", "km": "昆明", "xsbn.fang": "西双版纳", "hz": "杭州", "huzhou": "湖州", "jx": "嘉兴", "jh": "金华", "nb": "宁波", "quzhou": "衢州", "sx": "绍兴", "taizhou": "台州", "wz": "温州", "yw": "义乌"}
    for city_name in city_name_dic:
        print(city_name_dic[city_name])
        LianHome(city_name).run()

