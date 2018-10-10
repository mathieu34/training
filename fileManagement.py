import os

class fileManagement:
    FILENAME = ""

    def __init__(self, filename):
        self.FILENAME = filename
        
    def log(self, title, message_time, message):
        strFormatted = "{}\n{}:\n{}\n".format(title, message_time, message)
        with open(self.FILENAME, "a") as file:
            file.write(strFormatted)