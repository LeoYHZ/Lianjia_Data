# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


def plot_pie(results_dic, file_name):
    # 绘制饼状图
    new_results_dic = sorted(results_dic.items(), key=lambda kv: (-kv[1], kv[0]))
    label = []
    data = []
    if (len(new_results_dic) > 8):
        # 对超过8组的数据处理，将第8组之后数据定义为“其他”
        for i in new_results_dic[:7]:
            label.append(i[0])
            data.append(i[1])
        data.append(sum(results_layer.values()) - sum(data))
        label.append("其他")
    else:
        for i in new_results_dic:
            label.append(i[0])
            data.append(i[1])
    plt.axes(aspect=1)
    plt.pie(x=data, labels=label, autopct='%.3f%%', pctdistance=0.7, labeldistance=1.1, textprops={'fontsize': 10, 'color': 'black', 'fontproperties': "SimSun"})
    plt.savefig(file_name + '.jpg')
    plt.clf()


class Data_Analysis:
    def __init__(self, city):
        self.city_data = pd.read_csv("./home/" + city + ".csv", header=None)
        self.city = city

    def data_ave(self, num):
        # 计算均值
        Sum_all = 0
        for i in self.city_data[num]:
            Sum_all += i
        return (Sum_all / len(self.city_data[num]))

    def data_class(self, num):
        # 将数据按照所有的类型进行统计
        class_all = {}
        for i in self.city_data[num]:
            if (i not in class_all):
                class_all[i] = 1
            else:
                class_all[i] += 1
        return class_all

    def run(self):
        # 依次解析各组数据
        area_ave = self.data_ave(4)
        price_all_ave = self.data_ave(6)
        price_ave_ave = self.data_ave(7)
        layer = self.data_class(3)
        direction = self.data_class(5)
        return (area_ave, price_all_ave, price_ave_ave, layer, direction)


if __name__ == "__main__":
    # 各地城市对应url内的简写
    city_name_dic = {"aq": "安庆", "cz.fang": "滁州", "fy": "阜阳", "hf": "合肥", "mas": "马鞍山", "wuhu": "芜湖", "bj": "北京", "cq": "重庆", "fz": "福州", "quanzhou": "泉州", "xm": "厦门", "zhangzhou": "漳州", "dg": "东莞", "fs": "佛山", "gz": "广州", "hui": "惠州", "jiangmen": "江门", "qy": "清远", "sz": "深圳", "zh": "珠海", "zhanjiang": "湛江", "zs": "中山", "bh": "北海", "fcg": "防城港", "gl": "桂林", "liuzhou": "柳州", "nn": "南宁", "gy": "贵阳", "qxn.fang": "黔西南", "lz": "兰州", "tianshui": "天水", "bd": "保定", "chengde": "承德", "hd": "邯郸", "lf": "廊坊", "qhd.fang": "秦皇岛", "sjz": "石家庄", "ts": "唐山", "zjk": "张家口", "bt.fang": "保亭", "cm": "澄迈", "dz.fang": "儋州", "hk": "海口", "lg.fang": "临高", "ld.fang": "乐东", "ls.fang": "陵水", "qh.fang": "琼海", "san": "三亚", "wzs.fang": "五指山", "wc.fang": "文昌", "wn.fang": "万宁", "cs": "长沙", "changde": "常德", "xx": "湘西", "yy": "岳阳", "zhuzhou": "株洲", "jiyuan.fang": "济源", "kf": "开封", "luoyang": "洛阳", "pds": "平顶山", "py": "濮阳", "smx.fang": "三门峡", "xinxiang": "新乡", "xc": "许昌", "zz": "郑州", "zk": "周口", "zmd": "驻马店", "ez": "鄂州", "huangshi": "黄石", "wh": "武汉", "xy": "襄阳", "yichang": "宜昌", "hrb": "哈尔滨", "ganzhou": "赣州", "jiujiang": "九江", "jian": "吉安", "nc": "南昌", "sr": "上饶", "changzhou": "常州", "changshu": "常熟", "danyang": "丹阳", "haimen": "海门", "ha": "淮安", "jy": "江阴", "jr": "句容", "ks": "昆山", "nj": "南京", "nt": "南通", "su": "苏州", "taicang": "太仓", "wx": "无锡", "xz": "徐州", "yc": "盐城", "zj": "镇江", "cc": "长春", "jl": "吉林", "dl": "大连", "dd": "丹东", "fushun": "抚顺", "sy": "沈阳", "baotou": "包头", "byne.fang": "巴彦淖尔", "cf": "赤峰", "hhht": "呼和浩特", "tongliao": "通辽", "yinchuan": "银川", "heze": "菏泽", "jn": "济南", "jining": "济宁", "linyi": "临沂", "qd": "青岛", "ta": "泰安", "wf": "潍坊", "weihai": "威海", "yt": "烟台", "zb": "淄博", "cd": "成都", "dy": "德阳", "dazhou": "达州", "guangyuan": "广元", "leshan.fang": "乐山", "liangshan": "凉山", "mianyang": "绵阳", "ms.fang": "眉山", "nanchong": "南充", "pzh": "攀枝花", "sn": "遂宁", "yibin": "宜宾", "yaan": "雅安", "ziyang": "资阳", "baoji": "宝鸡", "hanzhong": "汉中", "xa": "西安", "xianyang": "咸阳", "jz": "晋中", "ty": "太原", "yuncheng": "运城", "sh": "上海", "tj": "天津", "wlmq": "乌鲁木齐", "dali": "大理", "km": "昆明", "xsbn.fang": "西双版纳", "hz": "杭州", "huzhou": "湖州", "jx": "嘉兴", "jh": "金华", "nb": "宁波", "quzhou": "衢州", "sx": "绍兴", "taizhou": "台州", "wz": "温州", "yw": "义乌"}
    results_dic = {"city_list":[], "area_ave":[], "price_all_ave":[], "price_ave_ave":[]}
    results_layer = {}
    results_direction = {'东': 0, '西': 0, '南': 0, '北': 0, '东南': 0, '西北': 0, '东北': 0, '西南': 0}
    for city_name in city_name_dic:
        print(city_name_dic[city_name])
        try:
            results = list(Data_Analysis(city_name).run())
            results_dic["city_list"].append(city_name_dic[city_name])
            results_dic["area_ave"].append(results[0])
            results_dic["price_all_ave"].append(results[1])
            results_dic["price_ave_ave"].append(results[2])
            for i in results[3]:
                if (i not in results_layer):
                    results_layer[i] = results[3][i]
                else:
                    results_layer[i] += results[3][i]
            for i in results[4]:
                for j in list(i.split(" ")):
                    if (j in results_direction):
                        results_direction[j] += results[4][i]
                    else:
                        pass
        except FileNotFoundError:
            print("No " + city_name + " Data")
    print(results_layer)
    plot_pie(results_layer, "layer")
    print(results_direction)
    plot_pie(results_direction, "direction")

    df = pd.DataFrame(results_dic)
    df.to_csv('results.csv', encoding="utf-8-sig")
