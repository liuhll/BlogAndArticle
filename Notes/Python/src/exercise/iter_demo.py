# -*- coding:UTF-8 -*-
import requests

# 可迭代对象和迭代器迭代器对象可以解决“用时访问”的问题，节省系统资源

def get_weather(city):
    url_api = "http://wthrcdn.etouch.cn/weather_mini?city=%s"%city
    resp = requests.get(url_api)
    data = resp.json()["data"]["forecast"][0]
    return "%s:%s,%s"%(city,data['low'],data['high'])


# print get_weather(u"北京")

from collections import Iterable,Iterator

class WeatherIterator(Iterator):
    '''
    获取城市的天气的迭代器对象，传入一个城市列表，获取这个城市列表的天气信息
    需要实现 Iterator 借口的next方法 abstractmethod
    '''
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def get_weather(self,city):
        url_api = "http://wthrcdn.etouch.cn/weather_mini?city=%s"%city
        resp = requests.get(url_api)
        data = resp.json()["data"]["forecast"][0]
        return "%s:%s,%s"%(city,data['low'],data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration

        city = self.cities[self.index]
        self.index +=1
        return self.get_weather(city)


class WeatherIterable(Iterable):
    '''
    天气的可迭代对象
    '''
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        #返回 天气的迭代器对象
        return WeatherIterator(self.cities)    


cities = [u"昆明",u"上海",u"北京",u"深圳",u"广州"]

for x in WeatherIterable(cities):
    print x        

