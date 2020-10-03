class Keisann:
    def __init__(self):
        endflag = "owari"
        while endflag == "owari":
            try:
                self.a=int(input("数値を入力して下さい。1"))
                endflag = "hajimari"
            except ValueError:
                print ("数値以外が入力されています。")

        end2 = 1
        while end2 == 1:
            try:
                self.b=int(input("数値を入力して下さい。2"))
                end2 = 3
            except ValueError:
                print ("数値以外が入力されています。")

    def purasu(self):
        line = "{} + {} = {}".format(self.a,self.b,self.a+self.b)
        print (line)

    def mainasu(self):
        line = "{} - {} = {}".format(self.a,self.b,self.a-self.b)
        print (line)

    def kakeru(self):
        line = "{} × {} = {}".format(self.a,self.b,self.a*self.b)
        print (line)

    def amari(self):
        line = "{} ÷ {} = {}余り{}".format(self.a,self.b,self.a//self.b,self.a%self.b)
        print (line)

    def warizann(self):
        line="{} ÷ {} = {}".format(self.a,self.b,self.a/self.b)
        print (line)

keisann=Keisann()
keisann.purasu()
keisann.mainasu()
keisann.kakeru()
keisann.amari()
keisann.warizann()








