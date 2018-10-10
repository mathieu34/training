from skyper							import Skyper
from selenium 		 				import webdriver
import time
import logging

def ring_alarm():
	for x in range(1 ,2):
		print ("\a")
		time.sleep(0.9)

def alert():
	for x in range(1 ,20):
		print ("\a")
		time.sleep(0.3)

def send_msg_skype(skyper, title, msgTime, msg):
	skyper.set_title(title)
	skyper.set_time(msgTime)
	skyper.set_message(msg)
	skyper.run_message()

def set_settings():
	driver = webdriver.Chrome()
	driver.implicitly_wait(30)
	driver.maximize_window()
	logging.basicConfig(level=logging.INFO)
	logger = logging.getLogger("test")
	return driver, logger