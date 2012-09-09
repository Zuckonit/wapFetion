#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
#/*
#@ @ @  @ @ @                             @ @
# @ @   @ @                                 @
# @ @   @ @       @ @ @         @ @ @ @     @   @ @ @       @ @ @       @ @   @ @
# @   @   @     @       @     @       @     @     @       @       @       @ @
# @       @     @       @     @             @ @ @         @ @ @ @ @       @
# @       @     @       @     @             @     @       @               @
#@ @ @   @ @ @    @ @ @        @ @ @ @    @ @   @ @ @      @ @ @ @     @ @ @ @

#+-------------------------------------
#     FileName: fetion.py
#         Desc: areuFetion
#       Author: Mocker
#        Email: Zuckerwooo@gmail.com
#     HomePage: http://hi.baidu.com/new/lsin30
#      Version: 0.0.1
#   LastChange: 2012-08-04 11:31:37
#      History:

#-------------------------------------
#*/
'''
import urllib2
import urllib
import cookielib
import re

import desetting
import urls

#{{{fetion account
_accout  = desetting.get_account()
username = _accout[0]
password = _accout[1]
#{{test code
print username
print password
#}}
#}}}

#=================== Exceptions && Feedback ===================#
#{{{Exceptions
class Error(Exception):
    """base class of Fetion Exceptio"""
    def __init__(self,msg=''):
        Exception.__init__(self,msg)
        self.msg = msg

    def __repr__(self,msg):
        return self.msg

    __str__ = __repr__

class FetionLoginFailed(Error):
    def __init__(self,msg="Login failed!"):
        Error.__init__(self,msg)
        self.msg = msg

class FetionLogoutFailed(Error):
    def __init__(self,msg="Logout failed!"):
        Error.__init__(self,msg)
        self.msg = msg

class FetionNotYourFriend(Error):
    def __init__(self,msg="Not your friend"):
        Error.__init__(self,msg)
        self.msg    = msg

class FetionNotFindUserId(Error):
    def __init__(self,msg="Cannot find such user"):
        Error.__init__(self,msg)
        self.msg = msg

class FetionAlreadyFriend(Error):
    def __init__(self,msg="He or she is already your friend"):
        Error.__init__(self,msg)
        self.msg = msg

class FetionSendMsgFailed(Error):
    def __init__(self,mobile=''):
        if mobile:
            Error.__init__(self,"send message to @%r failed!"%(mobile,))
        else:
            Error.__init__(self,"send message failed!")

        self.mobile = mobile

class FetionSetBirthdayRemindFailed(Error):
    def __init__(self,msg = "set birthday remind failed!"):
        Error.__init__(self,msg)
        self.msg = msg
#}}}


#{{{Feedback information
feedback_login_ing       = '''您正在登录中国移动WAP飞信,请稍候'''
feedback_login_fail      = '''自动返回输入登录页面'''
feedback_not_find_userId = '''没有符合条件的好友'''
feedback_not_your_friend = '''没有找到你要查找的好友'''
feedback_already_friend  = '''该用户已经是您的好友'''
feedback_sure_friend     = '''发送成功!待对方同意后,TA就是您的好友啦'''
feedback_birth_remind_success  = '''生日短信提醒设置成功'''
feedback_verify_code     = '''图形验证码错误'''
#}}}

#============================= parse ============================#

#img src="/im/systemimage/verifycode1347069516764.jpeg"
#<img src="/im/systemimage/verifycode1347071510224.jpeg"
#parse_verify_code = re.compile(r'img src="/im/systemimage/verifycode(.*?).jpeg')
#name="captchaCode" value="$(captchaCode1347071510224)"
parse_verify_code = re.compile(r'<img src=.*?verifycode(.*?).jpeg')
parse_csrf_token  = re.compile(r'name="csrfToken" value="(.*?)"')
parse_user_id     = re.compile(r'touserid=(\d*)')
parse_group_id    = re.compile(r'idContactList=(.*?)&')
parse_group_name  = re.compile(r'\+\|(.*?)\(')
parse_all_pages   = re.compile(r'共.*?page=(.*?)&')
parse_all_id      = re.compile(r'touserid=(.*?)&.*type=all')
parse_all_name    = re.compile(r'touserid.*?type=all">(.*?)</a>')


#{{{user info
parse_info_name   = re.compile(r'姓名:(.*?)<br/>',re.DOTALL)
parse_info_backup = re.compile(r'备注姓名:(.*?)\[')
parse_info_fetion = re.compile(r'飞信号:(.*?)<br/>')
parse_info_mobile = re.compile(r'手机号码:(.*?)<br/>')
parse_info_age    = re.compile(r'年龄:(.*?)<br/>')
parse_info_birth  = re.compile(r'生日:(.*?)<',re.DOTALL)
parse_info_sex    = re.compile(r'性别:(.*?)<br/>')
parse_info_city   = re.compile(r'城市:(.*?)\[')
parse_info_conste = re.compile(r'星座:(.*?)\[')
parse_info_blood  = re.compile(r'血型:(.*?)\[')
parse_info_sign   = re.compile(r'心情短语:(.*?)<br/>')
#}}}




#======================= Class Fetion =========================#

class Fetion(object):
    def __init__(self,usr=username,pwd=password,login_status=4):
        self.usr = usr
        self.pwd = pwd
        self.login_status = login_status

        cj = cookielib.CookieJar()
        hd = urllib2.HTTPCookieProcessor(cj)
        self.opener = urllib2.build_opener(hd)
        urllib2.install_opener(self.opener)

    def open(self,url,data=''):
        """
        open url
        @return content of page @url
        """

        req  = urllib2.Request(url,urllib.urlencode(data))
        html = self.opener.open(req).read()
        #print html
        #if feedback_login_fail in html:
            #raise FetionLoginFailed
        #else:
        return html


    def login(self):
        htm = ''
        data = {
            'm': self.usr,
            'pass': self.pwd,
        }
        while '图形验证码错误' in htm or not htm:
            page = self.open('http://f.10086.cn/im5/login/loginHtml5.action')
            captcha = parse_verify_code.findall(page)[0]
            img = self.open('http://f.10086.cn/im5/systemimage/verifycode%s.jpeg' % captcha)
            open('verifycode.jpeg', 'wb').write(img)
            captchacode = raw_input('captchaCode:')
            data['captchaCode'] = captchacode
            htm = self.open('http://f.10086.cn/im5/login/loginHtml5.action', data)
        #self.alive()
        return '登录' in htm


    def logout(self):
        """
        logout
        """
        try:
            self.open(urls.URL['url_logout'])
        except:
            raise FetionLogoutFailed


    def send_msg_by_id(self,user_id,msg):
        """
        send message to user @user_id with content msg
        """

        url_token = urls.URL['url_input_msg'] + user_id
        url_msg   = urls.URL['url_send_msg']  + user_id
        html      = self.open(url_token)

        if feedback_not_your_friend in html:
            raise FetionNotYourFriend

        csrfToken= parse_csrf_token.findall(html)[0]
        try:
            self.open(url_msg,{
                                'backUrl':'',
                                'touchTitle':'',
                                'touchTextLength':'',
                                'msg':msg,
                                'csrfToken':csrfToken
                             })
        except:
            raise FetionSendMsgFailed(user_id)

    def send_msg_by_mobile(self,mobile,msg):
        """
        send message to user @mobile with content msg
        """

        user_id = self._get_id(mobile)
        try:
            self.send_msg_by_id(user_id,msg)
        except:
            raise FetionSendMsgFailed(mobile)


    def send2self(self,msg):
        """
        send message to yourself with content msg
        """
        try:
            self.open(urls.URL['url_send2self'],{'msg':msg})
        except:
            raise FetionSendMsgFailed

    def send2group(self,group_id,msg):
        """
        send messge to every members of group @group_id with content msg
        """

        members = self._get_group_members_by_group_id(group_id)
        for i in members.keys():
            try:
                self.send_msg_by_id(members[i],msg)
            except FetionSendMsgFailed as e:
                print e

    def send2all(self,msg):
        """
        send message to all your friends with content msg
        """

        id_name_list = self._get_all_members()
        for name,id in enumerate(id_name_list):
            try:
                self.send_msg_by_id(id,msg)
            except FetionSendMsgFailed as e:
                print e

    def _get_id(self,mobile):
        """
        get id of user @mobile
        @return userid
        """

        html = self.open(urls.URL['url_get_id'],{'searchText':mobile})
        if feedback_not_find_userId in html:
            raise FetionNotFindUserId
        else:
            return parse_user_id.findall(html)[0]


    def _get_group_name_id(self):
        """
        get name and id of each group
        @return {groupname:groupid}
        """

        html = self.open(urls.URL['url_get_group_id'])
        group_id_list   = parse_group_id.findall(html)
        group_name_list = parse_group_name.findall(html)
        group_name_list = [i.decode('utf-8') for i in group_name_list]

        outcome = dict(zip(group_name_list,group_id_list))
        return outcome if outcome else None

    #groupId str
    def _get_group_members_by_group_id(self,group_id):
        """
        get group members and each of their id of group @group_id
        @return {username:userid}
        """

        url       = urls.URL['url_get_group_members'] + group_id +'&type=group'
        pages     = int(self.get_pages_of_friends(url))
        url_group = ''

        name_list = []
        id_list   = []
        for i in range(1,pages+1):
            url_group = urls.URL['url_get_group_members'] + str(group_id) + '&page=%d'%i
            html = self.open(url_group)
            id_list.extend(parse_all_id.findall(html))
            name_list.extend(parse_all_name.findall(html))

        name_list = [i.decode('utf-8') for i in name_list]
        return dict(zip(name_list,id_list))


    def get_pages_of_friends(self,url=urls.URL['url_all']):
        """
        get pages of your friend list , which type is str
        @return pages
        """

        html = self.open(url)
        return parse_all_pages.findall(html)[0]

    def _get_all_members(self):
        """
        get all members and each of their id of your friend list
        @return {username:userid}
        """

        pages     = int(self.get_pages_of_friends())
        url       = ''
        name_list = []
        id_list   = []

        for i in xrange(1,pages+1):
            url  = urls.URL['url_all'] + '&page=%d'%i
            html = self.open(url)
            name_list.extend(parse_all_name.findall(html))
            id_list.extend(parse_all_id.findall(html))

        name_list = [i.decode('utf-8') for i in name_list]
        return dict(zip(name_list,id_list))

    def add_friend_by_mobile(self,mobile,name=''):
        """
        add friend @mobile ,
        you can change his nickname name in your friend list at the same time
        """

        #{'nickname':'','buddylist':groupid,'localName':backup,'number':mobile,'type':0}
        try:
            html = self.open(urls.URL['url_add_friend'],{'number':mobile})
            if feedback_already_friend in html:
                raise FetionAlreadyFriend
            else:
                if name:
                    self.change_nick_name(mobile,name)
                return True
        except:
            return False

    def del_friend_by_mobile(self,mobile):
        """
        remove friend @mobile
        """

        user_id = self._get_id(mobile)
        url    = urls.URL['url_del_friend'] + user_id
        self.open(url)

    def change_nick_name(self,mobile,name):
        """
        change the nickname of user @mobile in your friend list
        """

        user_id = self._get_id(mobile)
        self.open(urls.URL['url_change_nickname'],{'touserid':user_id,'localName':name})


    def get_user_info(self,mobile):
        """
        get information of user @mobile
        """

        try:
            user_id = self._get_id(mobile)
            url    = urls.URL['url_get_user_info'] + user_id
            html   = self.open(url)
            name   = parse_info_name.findall(html)[0].decode('utf-8')
            backup = parse_info_backup.findall(html)[0].decode('utf-8')
            fetion = parse_info_fetion.findall(html)[0]
            mobile = parse_info_mobile.findall(html)[0]
            age    = parse_info_age.findall(html)[0].decode('utf-8')
            birth  = parse_info_birth.findall(html)[0].decode('utf-8')
            sex    = parse_info_sex.findall(html)[0].decode('utf-8')
            city   = parse_info_city.findall(html)[0].decode('utf-8')
            conste = parse_info_conste.findall(html)[0].decode('utf-8')
            blood  = parse_info_blood.findall(html)[0].decode('utf-8')
            sign   = parse_info_sign.findall(html)[0].decode('utf-8')

            return {
                u'姓名':name,
                u'备注':backup,
                u'飞信号':fetion,
                u'手机号':mobile,
                u'年龄':age,
                u'生日':birth,
                u'性别':sex,
                u'城市':city,
                u'星座':conste,
                u'血型':blood,
                u'心情短语':sign
            }

        except Exception as e:
            print e

    def show_me_your_birthday(self,mobile):
        """
        tell user @mobile to public his/her birthday by sending him/her message
        """

        user_id = self._get_id(mobile)
        self.open(urls.URL['url_iwanna_know_your_birthday'],{'idUsers':user_id})

    def remind_me_your_birthday(self,mobile):
        """
        you'll get a reminding message when birthday of user @mobile is coming around
        """

        user_id = self._get_id(mobile)
        url    = urls.URL['url_remind_me_your_birthday'] +user_id + '&opt=1'
        html   = self.open(url)
        if feedback_birth_remind_success in html:
            print feedback_birth_remind_success
        else:
            raise FetionSetBirthdayRemindFailed
