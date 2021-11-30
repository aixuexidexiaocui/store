class cup:
    __h = 0
    __l = 0
    m = ''
    c = ''

    def seth(self , h):
        if h <= 0 or h > 10000:
            print("请给我找一个这么高的杯子")
        else:
            self.__h = h

    def geth(self):
        return self.__h

    def setl(self , l):
        if l <= 0 or l > 10:
            print("请给我找一个这么能装的杯子")
        else:
            self.__l = l

    def getl(self):
        return self.__l

    def cup(self):
        print("这是一个" , self.m , "色的，高" , self.__h , "由" , self.m , "制作，可以装" , self.__l , "L的水杯")


c = cup()
c.seth(5)
c.setl(5)
c.m = '透明'
c.c = '玻璃'

c.cup()
