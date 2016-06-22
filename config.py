#coding=utf8

TOKEN = 'caiqiqistudentinfo'
APP_ID = 'wx0cf9de76deef346c'
SECRET_KEY = '049acf4e2602cf0a21439c5e407775d7'
TULING_KEY = 'b3827b85168c97dc6391c406d7b35ef5'
ADMIN_OAUTH = 'admin_oauth'
WELCOME_WORD = u'''\
欢迎关注我的微信号！
回复下列内容获取对应信息：
目录： 获取文章目录的网址
帮助： 获取本信息
其他： 图灵机器人会陪你聊天'''
INDEX_URL = 'www.baidu.com'
REPLY_DICT = {
    u'目录': '点这里-> ' + INDEX_URL,
    u'帮助': WELCOME_WORD,
}
MENU = {}
ARTICLES_DIR = 'articles'
ARTICLES_NAME = 'articles.json'
BASE_URL = 'https://api.weixin.qq.com/cgi-bin'
