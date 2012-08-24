#-*- coding:utf-8 -*-
import re
import urllib
#import get_charset
import socket

TIMEOUT = 20
socket.setdefaulttimeout(TIMEOUT)

url_weather   = 'http://feixin.10086.cn/weather'
parse_weather = re.compile(r'<meta name="description" content="(.*?)"',re.DOTALL)

_default_charset = 'utf-8'

def getWeather(url = url_weather,parse = parse_weather):
    #char_set = get_charset.get_charset(url)
    try:
        data = urllib.urlopen(url).read()
        #if not char_set:
            #data = data.decode(_default_charset)
        #elif char_set != _default_charset:
            #data = data.decode(char_set).encode(_default_charset)
        #else:pass
        weather = parse.findall(data)[0].decode(_default_charset)
        return (True,weather)
        #return (True,parse.findall(data)[0])
    except Exception as e:
        return (False,e)
