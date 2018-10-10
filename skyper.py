import time
from skpy import Skype
from skpy import SkypeAuthException

class Skyper:
    def __init__(self, Bot_Username, Bot_pwd, users_list):
        self.bot_username = Bot_Username
        self.bot_pwd = Bot_pwd
        self.user_list = users_list
        self.title = ""
        self.message_time = ""
        self.message = ""
        self.sk = None
        self.set_up()
        
    def set_title(self, title):
        self.title = title
        
    def set_time(self, msgTime):
        self.message_time = msgTime

    def set_message(self, msg):
        self.message = msg

    def set_up(self):
        #self.sk = Skype(self.bot_username, self.bot_pwd)
        self.sk = Skype(connect=False)
        self.sk.conn.setTokenFile("tokens-app")
        self.test_token()
        self.sk.user # you
        self.sk.contacts # your contacts
        self.sk.chats # your conversations
        
    def test_token(self):
        try:
            self.sk.conn.readToken()
        except SkypeAuthException:
            print "( getSkypeToken )"
            open('tokens-app', 'w').close()
            self.sk.conn.setUserPwd(self.bot_username, self.bot_pwd)
            self.sk.conn.getSkypeToken()
        
    def send_message(self):
        for user in self.user_list:
            print("( " + self.message_time + " )" + ": Warn " + user + "\n")
            ch = self.sk.contacts[user].chat
            ch.sendMsg("{}\n{}:\n{}".format(self.title,self.message_time,self.message))

    def run_message(self):
        self.test_token()
        self.send_message()
