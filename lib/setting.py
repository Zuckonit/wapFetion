#-*- coding:utf-8 -*-


#{{{future expand for configure choice
#SETTINGS = (
#    'CONF.areuFetion'
#    'CONF.settings.py'
#)
#}}}

#{{{future expand for txt.txt code
#CHARSET = 'utf-8'
#}}}


import os
expath = lambda path:os.path.expanduser(path)
CACHE = {
    'default': {
        'ENGINE':'txt.pick',             # Add txt.pick | db.sqlite3
        'NAME': (
                 expath('~/.config/areuFetion/cache/contact.pick'),
                 expath('~/.config/areuFetion/cache/userinfo.pick')
                ),

        #{{{future expand
        #'USER': '',             # Not used with db.sqlite3 or txt.[xml|txt|pick].
        #'PASSWORD': '',         # Not used with db.sqlite3 or txt.[xml|txt|pick].
        #'HOST': '',             # Not used with db.sqlite3 or txt.[xml|txt|pick].
        #'PORT': '',             # Not used with db.sqlite3 or txt.[xml|txt|pick].
        #}}}
    }
}


#{{{future expand for txt.txt
#interval character
INTERVAL = '|~slash~|'        #this will be used when ENGINE is txt.txt
                               #which work as a interval character like item1INSTERVALitem2
#}}}



#{{{future expand
#fetion account settings
#CIPHER = 0                         #if cipher=0,means no cipher for ACCOUT,cipher=1 on the countrary.
                                    #cipher with module cipher.py -c [val]
                                    #default cipher source is the ACCOUT (not null)
#}}}


ACCOUNT = {
    'username':'15280991357',                  #your fetion username
    'password':'yang3136299.cn'                   #your fetion password
}


#{{{future expand for sync
#SYNC = {
#   default:{
#       'sort':'dropbox'
#       'account':{
#           'username':'',
#           'password':''
#       }
#   }
#}
#}}}


__locals__ = locals()        #don't do any change of this line
