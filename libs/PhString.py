class PhString:
    def sub(self, src, location, length):
        return src[location:(location + length)]

    def compare(self, str1, str2):
        x = (str1 == str2)
        return x
        
    def append(self, src, string):
        return (src + string)

    def split(self, src, string):
        return src.split(string)

    def contain(self, src, string):
        return (string in src)
        
    def toInt(self, src):
        return int(src)

    def toFloat(self, src):
        return float(src)
        
    def remove(self, src, string):
        return src.replace(string, "")

    def uppercase(self, src):
        return src.upper()
        
    def lowercase(self, src):
        return src.lower()
        
    def reserve(self, src):
        return src[::-1]

