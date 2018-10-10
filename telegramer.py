import telegram

class Telegramer:
    def __init__(self, token):
        self.bot = telegram.Bot(token='XXX')
    
    def send_message(self, chat_id, title, msgTime, msg):
        self.bot.send_message(chat_id=chat_id, text="{}\n{}:\n{}".format(title, msgTime, msg))