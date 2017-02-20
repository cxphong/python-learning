from datetime import datetime
import time
from time import gmtime, strftime

class PhDateTime:
    
    # format: https://docs.python.org/2/library/time.html#time.strftime
    # exanple: %Y-%m-%d %H:%M:%S
    def now(self, format):
        return datetime.now().strftime(format)

    def now1(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def now2(self):
        return datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    def epoch(self):
        return int(time.time())

    def epochToLocaltime(self, epoch):
        return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch))

    def epochToGmttime(self, epoch):
        return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(epoch))

    def timezone(self):
        return strftime("%z", gmtime())

    def timezoneOffset(self):
        return -time.timezone

    def day(self):
        return datetime.now().strftime("%d")

    def month(self):
        return datetime.now().strftime("%m")

    def year(self):
        return datetime.now().strftime("%Y")

    def hour(self):
        return datetime.now().strftime("%H")

    def minute(self):
        return datetime.now().strftime("%M")

    def second(self):
        return datetime.now().strftime("%S")




