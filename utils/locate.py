e#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib
import urllib2
import re
#import get_charset

__all__ = ['locate']

_url_query       = 'http://wap.10086.cn/apps/location/query.do'
_parse_province  = re.compile(r'''所属省份：(.*?)<''')
_parse_city      = re.compile(r'''所属城市：(.*?)<''')

_default_charset = 'utf-8'

def locate(mobile,url=_url_query):
    if len(mobile) != 11:
        return {'error':'please enter 11 digit phone number'}

    postdata = {
        'iphone':mobile,
        'v':2
    }

    req  = urllib2.Request(url,urllib.urlencode(postdata))
    html =  urllib2.urlopen(req).read()
    #charset = get_charset.get_charset(url)
    ##if not charset:
        #html = html.decode(_default_charset)
    #elif charset != _default_charset:
        #html = html.decode(_default_charset).encode(_default_charset)
    #else:pass

    province = _parse_province.findall(html)[0].decode(_default_charset)
    city     = _parse_city.findall(html)[0].decode(_default_charset)

    return {'province':province,'city':city}

