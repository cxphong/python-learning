import random

class PhRandom:

    def integer(self, fr, to):
        num = random.randrange(fr, to + 1, 1)
        print ("num %d" % num)
        return num
