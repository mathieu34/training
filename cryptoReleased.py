import time
import getpass
import sys, os
from threading          import Thread
from skyper             import Skyper
from helper             import *
from fileManagement     import *
from kucoin.client      import Client
from telegramer         import Telegramer

# Kucoin client need to be installed, API_KEY, SECRET_KEY, TELEGRAM_CHAT_ID need to be filled with correct information.
# The purpose of this bot is to signal the user when a new cryptocurrency is released in an exchange platform.
# If CHECK_NEW_SYMBOLS is TRUE, then it sends a message into a Skype account and a Telegram channel as soon as a symbol is released.
# If a symbol in the list is released, then it sends a message into a Skype account and a Telegram channel and triggers an alarm.

# object1 shall be bigger or equal than object2
# compare object1 and object2, then return the diff
def compare(object1, object2):
    diff = []
    for tmp1 in object1:
        tmpFound = False
        for tmp2 in object2:
            if tmp1['coinType'] == tmp2['coinType']:
                tmpFound = True
                break
        if tmpFound == False:
            if tmp1['coinType'] not in diff:
                diff.append(tmp1['coinType'])
    return diff

class botKucoin(Thread):
    # Exchange platform settings.
    API_KEY         = 'XXX'
    SECRET_KEY      = 'XXX'
    # Crypto to look for in the exchange platform.
    SYMBOLS                 = ['AIR', 'ART', 'BET', 'CFI', 'CLOAK', 'ELA', 'ELTCOIN', 'EVE', 'GBYTE', 'MONA', 'MYST', 'PTOY', 'STA', 'SYNX', 'WAN', 'XEM', 'XNN', 'ZIL', 'BCDT', 'ELA', 'REN', 'FLOT', 'SEN', 'INSTAR', 'CRNC', 'REM', 'WBT']
    CHECK_NEW_SYMBOLS       = True
    # Trigger a sound.
    ALARM                   = True
    LOG_FILENAME            = "E:/Dev/PythonBots/Logs/kucoin_logs.txt"
    # Telegram channel to send the message to.
    TELEGRAM_CHAT_ID        = XXX
    DEBUG                   = False
    
    # Init
    fileManagementObt       = None
    alarm_function_running  = False
    symbols_list            = []

    def __init__(self, SkyperInst, TelegramerInst):
        self.skyper = SkyperInst
        self.telegramer = TelegramerInst
        self.fileManagementObt = fileManagement(self.LOG_FILENAME)
        Thread.__init__(self)

    def threaded_alarm_function(self):
        while True:
            print ("\a")
            time.sleep(5)
            
    def run(self):
        # Retrieve password
        #self.SKYPE_PWD = getpass.getpass()
        
        # Kucoin connection
        client = Client(self.API_KEY, self.SECRET_KEY)
    
        # Skype connection
        #skyper = Skyper(self.SKYPE_USERNAME, self.SKYPE_PWD, self.SKYPE_USERS)
        send_msg_skype(self.skyper, "KUCOIN", time.ctime(int(time.time())), "Bot is running...")
        self.fileManagementObt.log("KUCOIN", time.ctime(int(time.time())), "Bot is running...")
       
        # Telegram connection
        #telegramer = Telegramer(token='521036992:AAG8pG_Gc7tmldnlpJgXGUwrPkGGKjhtCHw')
        self.telegramer.send_message(self.TELEGRAM_CHAT_ID, "KUCOIN", time.ctime(int(time.time())), "BOT is running...")
        
        # Get list of symbols
        try:
            if self.DEBUG:
                previousInfo = [{u'sell': 10824.0, u'sort': 100, u'buy': 10820.0, u'changeRate': 0.0417, u'vol': 208.75995661, u'symbol': u'BTC-USDT', u'high': 10849.999999, u'coinType': u'BTC', u'lastDealPrice': 10824.0, u'feeRate': 0.001, u'volValue': 2189548.32186627, u'trading': True, u'low': 9999.0, u'coinTypePair': u'USDT', u'datetime': 1519026140000L, u'change': 433.779732}, {u'sell': 0.087433, u'sort': 100, u'buy': 0.08713844, u'changeRate': -0.0054, u'vol': 3946.72613, u'symbol': u'ETH-BTC', u'high': 0.089597, u'coinType': u'LTC', u'lastDealPrice': 0.08712844, u'feeRate': 0.001, u'volValue': 347.13935351, u'trading': True, u'low': 0.086022, u'coinTypePair': u'BTC', u'datetime': 1519026138000L, u'change': -0.00047156}]
            else:
                previousInfo = client.get_trading_symbols()
                if previousInfo:
                    for symbol in previousInfo:
                        if symbol['coinType'] not in self.symbols_list:
                            self.symbols_list.append(symbol['coinType'])
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            strFormatted = "{}\n{}:\n{}\n".format(exc_type, fname, exc_tb.tb_lineno)
            self.fileManagementObt.log("KUCOIN", time.ctime(int(time.time())), strFormatted)
   
        # Request in a loop the list of symbols, and compare it with the initial list.
        while True:
            try:
                currentTime = time.ctime(int(time.time()))
                if self.DEBUG:
                    info = [{u'sell': 10824.0, u'sort': 100, u'buy': 10820.0, u'changeRate': 0.0417, u'vol': 208.75995661, u'symbol': u'BTC-USDT', u'high': 10849.999999, u'coinType': u'BTC', u'lastDealPrice': 10824.0, u'feeRate': 0.001, u'volValue': 2189548.32186627, u'trading': True, u'low': 9999.0, u'coinTypePair': u'USDT', u'datetime': 1519026140000L, u'change': 433.779732}, {u'sell': 0.087433, u'sort': 100, u'buy': 0.08713844, u'changeRate': -0.0054, u'vol': 3946.72613, u'symbol': u'ETH-BTC', u'high': 0.089597, u'coinType': u'LTC', u'lastDealPrice': 0.08712844, u'feeRate': 0.001, u'volValue': 347.13935351, u'trading': True, u'low': 0.086022, u'coinTypePair': u'BTC', u'datetime': 1519026138000L, u'change': -0.00047156}, {u'sell': 944.5969, u'sort': 100, u'buy': 942.9, u'changeRate': 0.0291, u'vol': 1116.388536, u'symbol': u'ETH-USDT', u'high': 947.777777, u'coinType': u'ETH', u'lastDealPrice': 942.9, u'feeRate': 0.001, u'volValue': 1031605.24945772, u'trading': True, u'low': 892.137139, u'coinTypePair': u'USDT', u'datetime': 1519026140000L, u'change': 26.661531}]
                else:
                    info = client.get_trading_symbols()
                if info:
                    print "( ", currentTime, " ): [ KUCOIN ] get_trading_symbols"
                    
                    # Looking for any new symbols.
                    if self.CHECK_NEW_SYMBOLS == True:
                        for symbol in info:
                            if symbol['coinType'] not in self.symbols_list:
                                # New symbol detected.
                                self.symbols_list.append(symbol['coinType'])
                                depositAddress = {}
                                print "( ", currentTime, " ): [ KUCOIN ] new symbol named ", symbol['coinType']
                                print "( ", currentTime, " ): [ KUCOIN ] get_deposit_address"
                                try:
                                    depositAddress = client.get_deposit_address(symbol['coinType'])
                                except:
                                    pass
                                # Send a message to the skype user and telegram channel.
                                if len(depositAddress) != 0:
                                    self.telegramer.send_message(self.TELEGRAM_CHAT_ID, "KUCOIN", currentTime, depositAddress)
                                    send_msg_skype(self.skyper, "KUCOIN", currentTime, depositAddress)
                                    print "( ", currentTime, " ): [ KUCOIN ] depositAddress ", depositAddress
                                else:
                                    self.telegramer.send_message(self.TELEGRAM_CHAT_ID, "KUCOIN", currentTime, symbol['coinType'])
                                    send_msg_skype(self.skyper, "KUCOIN", currentTime, symbol['coinType'])
                                    print "( ", currentTime, " ): [ KUCOIN ] depositAddress ", symbol['coinType']
                                self.fileManagementObt.log("KUCOIN", time.ctime(int(time.time())), depositAddress)
                                break
                    
                    # Looking for a symbol in the list.
                    for symbol in self.SYMBOLS:
                        depositAddress = {}
                        for kucoinSymbol in info:
                            if kucoinSymbol['coinType'] == symbol:
                                # Symbol in the list detected.
                                print "( ", currentTime, " ): [ KUCOIN ] found symbol ", symbol
                                print "( ", currentTime, " ): [ KUCOIN ] get_deposit_address"
                                if self.ALARM == True:
                                    if self.alarm_function_running == False:
                                        self.alarmThread = Thread(target = self.threaded_alarm_function)
                                        self.alarmThread.start()
                                        self.alarm_function_running = True
                                try:
                                    depositAddress = client.get_deposit_address(symbol)
                                except:
                                    pass
                                if len(depositAddress) != 0:
                                    self.telegramer.send_message(self.TELEGRAM_CHAT_ID, "KUCOIN", currentTime, depositAddress)
                                    send_msg_skype(self.skyper, "KUCOIN", currentTime, depositAddress)
                                    print "( ", currentTime, " ): [ KUCOIN ] depositAddress ", depositAddress
                                else:
                                    self.telegramer.send_message(self.TELEGRAM_CHAT_ID, "KUCOIN", currentTime, symbol)
                                    send_msg_skype(self.skyper, "KUCOIN", currentTime, symbol)
                                    print "( ", currentTime, " ): [ KUCOIN ] depositAddress ", symbol                         
                                self.SYMBOLS.remove(symbol)
                                self.fileManagementObt.log("KUCOIN", time.ctime(int(time.time())), depositAddress)
                                break
                    previousInfo = info
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                strFormatted = "{}\n{}:\n{}\n".format(exc_type, fname, exc_tb.tb_lineno)
                self.fileManagementObt.log("KUCOIN", time.ctime(int(time.time())), strFormatted)
            time.sleep(10)