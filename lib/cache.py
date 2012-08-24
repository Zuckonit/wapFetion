#-*- coding:utf-8 -*-
import desetting
try:import cPickle as pickle
except:import pickle as pickle

suffix = (
    'txt.pick',
    'db.sqlite3',
)

_fmt = desetting.get_cache_default_opt_val('ENGINE')
#_pth = desetting.get_cache_default_opt_val('NAME')


#======================================
def cache_txt_pick(dic,outfile):
    with open(outfile,'wb') as f:
        pickle.dump(f,dic)

def decache_txt_pick(infile):
    with open(infile,'rb') as f:
        return pickle.load(f)


def cache_db_sqlite3():
    pass

def decache_txt_sqlite3():
    pass

#===========================

def smart_cache(dic):
    if _fmt == suffix[0]:
        cache_txt_pick()

    elif _fmt == suffix[3]:
        cache_db_sqlite3()

def smart_decache():
    pass
