class Test:
    def __init__(self):
        self.a=english_tennsuu
        self.b=math_tennsuu
        self.t=goukei
        self.av=heikinn

    def input(self):
        self.a = int(input("英語の成績を入力して下さい"))
        self.b = int(input("数学の成績を入力して下さい"))

    def english(self):
        print("英語の得点:" + str(self.a))

    def math(self):
        print("数学の得点:" + str(self.b))

    def sum(self):
        self.t = (self.a + self.b)
        print("合　　　計:" + str(self.t))

    def ave(self):
        self.av = self.t / 2
        print("平　　　均:" + str(self.av))
