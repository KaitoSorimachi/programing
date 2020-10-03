class Kane:
    def __init__(self):
        self.t = 0
        self.n = 0
        self.a = 0
        self.sam = 0
        self.m = 0

    def kanekasi(self):
        suuji1 = 77
        while suuji1 == 77:
            try:
                self.t = int(input("借金＞"))
                suuji1 = 66
            except ValueError:
                print ("数値以外が入力されています。")

        suuji2 = 77
        while suuji2 == 77:
            try:
                self.n = int(input("年利率（％）＞"))
                suuji2 = 66
            except ValueError:
                print ("数値以外が入力されています。")

        suuji3 = 77
        while suuji3 == 77:
            try:
                self.a = int(input("返済額＞"))
                suuji3 = 66
            except ValueError:
                print ("数値以外が入力されています。")

        self.sam = 0
        self.m = 0
        self.n = self.n / 12 / 100 * self.t

    def hennsai(self):
        money = 55
        while money == 55:
            self.m += 1
            if self.t > self.a:
                self.t = self.t + self.n - self.a
                self.sam += self.a
                con = "{}月: 返済額 {} 円 残り {} 円".format(self.m, self.a, int(self.t))
                print (con)

            else:
                money = 44
                self.sam += self.t
                end = "{}月: 返済額 {} 円 これで完済。 返済総額: {} 円".format(self.m, int(self.t), int(self.sam))
                print (end)

kane = Kane()
kane.kanekasi()
kane.hennsai()

