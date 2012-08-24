#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib
import re

default_charset = 'utf-8'

"""
this method can get the charset of an url content,
if cannot find the charset by info dict,return None
else return the charset found by info dict
"""
def get_charset(url):
    content_type = urllib.urlopen(url).info.dict['content-type']
    if not content_type:
        content_type = urllib.urlopen(url).info.dict['CONTENT_TYPE']

    charset = re.search(r'charset=(.*)',content_type).group(1).lower()

    if not charset:
        return None
    else:
        return charset
