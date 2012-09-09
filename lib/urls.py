#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urllib

#http://f.10086.cn/im/login/inputpass.action
base = 'http://f.10086.cn/im/'
wrap = lambda mid,trail,getdata='':base + mid + '/' + trail + urllib.urlencode(getdata)
URL = {
    #login
    'url_login' : wrap('login','inputpasssubmit1.action'),
    'url_verify': wrap('login','inputpass.action'),
    #'url_login' : wrap('login','login.action'),

    #index
    'url_logout': wrap('index','logoutsubmit.action'),
    'url_all':wrap('index','index.action?',{'type':'all'}),
    'url_get_group_id':wrap('index','index.action?',{'type':'group'}),
    'url_get_group_members':wrap('index','contactlistView.action?',{'idContactList':''}),
    'url_get_id':wrap('index','searchOtherInfoList'),

    #user
    'url_send2self':wrap('user','sendMsgToMyselfs.action'),
    'url_get_user_info':wrap('user','userinfoByuserid.action?',{'touserid':''}),
    'url_add_friend':wrap('user','insertfriend2.action'),
    'url_del_friend':wrap('user','deletefriendsubmit.action?',{'touserid':''}),
    'url_change_nickname':wrap('user','updateLocalnames.action'),

    #chat
    'url_send_msg':wrap('chat','sendMsg.action?',{'touserid':''}),
    'url_input_msg':wrap('chat','toinputMsg.action?',{'touserid':''}),

    #birthday
    'url_iwanna_know_your_birthday':wrap('birthday','sendReminds.action'),
    'url_remind_me_your_birthday':wrap('birthday','switchSubscription.action?',{'contactId':''}),
}
#print URL['url_get_group_members']
#print URL['url_del_friend']
