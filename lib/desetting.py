#-*- coding:utf-8 -*-
import setting

class Error(Exception):
    def __init__(self,msg):
        Exception.__init__(self,msg)
        self.msg = msg

    def __repr__(self):
        return self.msg

    __str__ = __repr__


class NoSuchOption(Error):
    def __init__(self,opt=''):
        Error.__init__(self,"No such option :%r"%(opt,))
        self.opt = opt

class NoSuchKey(Exception):
    def __init__(self,dic,key):
        self.dic = dic
        self.key = key

    def __repr__(self):
        return "No such key %r in %r"%(self.key,self.dic,)

    __str__ = __repr__

def get_opt_val(opt):
    val = setting.__locals__.get(opt,None)
    if not val:
        raise NoSuchOption(opt)
    else:
        return val

def __get_dict_opt_val(dic,opt):
    val = dic.get(opt,None)
    if not val:
        raise NoSuchKey(dic,opt)
    else:
        return val

def get_cache_default_opt_val(opt):
    tmp = get_opt_val('CACHE')
    dft = __get_dict_opt_val(tmp,'default')
    val = __get_dict_opt_val(dft,opt)
    return val

def get_account():
    account  = get_opt_val('ACCOUNT')
    username = __get_dict_opt_val(account,'username')
    password = __get_dict_opt_val(account,'password')
    return (username,password)




#=================== main function used for test =======================#
if __name__ == '__main__':
    print '''this is a test code,if exception is raised,check your setting.py'''.upper()
    print get_account()
    print get_cache_default_opt_val('NAME')
    print get_cache_default_opt_val('ENGINE')
    #print get_cache_default_opt_val('HOST')
    #print get_cache_default_opt_val('USER')
    #print get_cache_default_opt_val('PASSWORD')
