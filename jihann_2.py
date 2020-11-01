import sqlite3
dbfile = sqlite3.connect("jihann.db")
sql = dbfile.cursor()

menu = {"コーラ": 150, "お茶": 120, "酒": 300, "サイダー": 150, "オレンジ": 200}

class Ver_2():
    def __init__(self):
        self.a = ""
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.f = 0
        self.h = 0
        self.i = 0
        self.x = ""
        self.fetchresult = ""
        self.fetchresult2 = ""
        self.upquon = 0
        self.upquon2 = 0

    def purchased_items(self):
        import subprocess
        subprocess.call('clear')
        print (menu)
        self.a = input("購入品を選んでください。")

    def sold_out(self):
        sql.execute("select quontity from jihann where menu = ? ", (self.a,))
        self.fetchresult = sql.fetchone()
        print ("売り切れです")

    def money(self):
        end2 = 1
        while end2 == 1:
            try:
                self.b = int(input("お金を入力をして下さい。"))
                end2 = 3
            except ValueError:
                print ("お金以外が入力されています。")
        self.c = menu[self.a]
        self.d = self.b - self.c

    def sold(self):
        import subprocess
        subprocess.call('clear')
        print (str(self.a) + "をお買い上げしました。")
        print ("お釣りは" + str(self.d) + "円です。")
        self.upquon = int(self.fetchresult[0]) - 1
        sql.execute("update jihann set quontity = ? where menu = ?", (self.upquon, self.a,))
        sql.execute("select quontity from mydrink where buy = ?", (self.a,))
        self.fetchresult2 = sql.fetchone()
        self.upquon2 = int(self.fetchresult2[0]) + 1
        sql.execute("update mydrink set quontity = ? where buy = ?", (self.upquon2, self.a,))
        print ("{}の購入数これで{}個目です".format(self.a, self.upquon2))

    def not_enough_money(self):
        print ("投入金額が不足しています。")
        self.e = self.c - self.b
        print (str(self.e) + "円足りません。")
        end7 = 99
        while end7 == 99:
            try:
                global f
                self.f = int(input("お金を再度入力をして下さい。"))
                end7 = 88
            except ValueError:
                print ("お金以外が入力されています。")
        self.b = self.f + self.b
        self.h = self.b - self.c
        self.i = self.c - self.b

    def sold2(self):
        import subprocess
        subprocess.call('clear')
        print (str(self.a) + "をお買い上げしました。")
        print ("お釣りは" + str(self.h) + "円です。")
        self.upquon = int(self.fetchresult[0]) - 1
        sql.execute("update jihann set quontity = ? where menu = ?", (self.upquon, self.a,))
        sql.execute("select quontity from mydrink where buy = ?", (self.a,))
        self.fetchresult2 = sql.fetchone()
        self.upquon2 = int(self.fetchresult2[0]) + 1
        sql.execute("update mydrink set quontity = ? where buy = ?", (self.upquon2, self.a,))
        print ("{}の購入数これで{}個目です".format(self.a, self.upquon2))

    def not_enough_money2(self):
        print ("投入金額が不足しています。")
        print (str(self.i) + "円足りません。")

    def no_product(self):
        import subprocess
        subprocess.call('clear')
        print ("該当商品がありません。")

    def to_continue(self):
        endflag = "owari"
        while endflag == "owari":
            self.x = input("購入を続けますか？Yes or No")
            if self.x == "Yes":
                endflag = 55

            elif self.x == "No":
                dbfile.commit()
                dbfile.close()
                import subprocess
                subprocess.call('clear')
                endflag = 55

            else:
                import subprocess
                subprocess.call('clear')
                print ("YesかNo以外が入力されています。")

ver_2 = Ver_2()
mo = 33
while mo == 33:
    ver_2.purchased_items()
    if self.a in menu:
        ver_2.money()
        if self.fetchresult[0] == "0":
            ver_2.sold_out()
        else:
            ver_2.money()
            if self.d >= 0:
                ver_2.sold()
            else:
                sad = "mata"
                while sad == "mata":
                    ver_2.not_enough_money()
                    if self.h >= 0:
                        ver_2.sold2()
                        sad = "ryo"
                    else:
                        ver_2.not_enough_money2()

    else:
        ver_2.no_product()

    ver_2.to_continue()
    if self.x == "No":
        mo = 000
        imp = "forever"
        while imp == "forever":
            import jihann_1