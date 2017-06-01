from datetime import datetime
import time
from time import gmtime, strftime


class PhDateTime:


    '''
        Get current time. 
        Format: https://docs.python.org/2/library/time.html#time.strftime
        Usage: 
            PhDateTime.now('%Y-%m-%d %H:%M:%S')
            PhDateTime.now()
    '''
    def now(format_str = None):
        if format_str is None:
            return datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0000')
        else:
            return datetime.now().strftime(format_str)



    '''
        Get current system epoch
        Usage: PhDateTime.epoch()
    '''
    @staticmethod
    def epoch():
        return int(time.time())

    '''
        Convert epoch to format string
        Usage: PhDateTime.epoch_to_local_time(epoch, "%d/%m/%Y %H:%m:%S")
    '''
    @staticmethod
    def epoch_to_local_time(epoch, format_str=None):

        if  format_str is None:
            return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch))
        else:
            return time.strftime(format_str, time.localtime(epoch))

    # def epochToGmttime(self, epoch):
    #     return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(epoch))
    #
    # def timezone(self):
    #     return strftime("%z", gmtime())
    #
    # def timezoneOffset(self):
    #     return time.tzname

    '''
        Usage: PhDateTime.day()
    '''
    @staticmethod
    def day():
        return datetime.now().strftime("%d")

    '''
        Usage: PhDateTime.month()
    '''
    @staticmethod
    def month():
        return datetime.now().strftime("%m")

    '''
        Usage: PhDateTime.year()
    '''
    @staticmethod
    def year():
        return datetime.now().strftime("%Y")

    '''
        Usage: PhDateTime.hour()
    '''
    @staticmethod
    def hour():
        return datetime.now().strftime("%H")

    '''
        Usage: PhDateTime.minute()
    '''
    @staticmethod
    def minute():
        return datetime.now().strftime("%M")

    '''
        Usage: PhDateTime.second()
    '''
    @staticmethod
    def second():
        return datetime.now().strftime("%S")




