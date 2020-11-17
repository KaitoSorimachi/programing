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

    def in_menu(self):
        while True:
            import subprocess
            subprocess.call('clear')
            print (menu)
            self.a = input("購入品を選んでください。")
            if self.a in menu:
                sql.execute("select quontity from jihann where menu = ? ", (self.a,))
                self.fetchresult = sql.fetchone()
                if self.fetchresult[0] == "0":
                    print ("売り切れです")

                else:
                    end2 = 1
                    while end2 == 1:
                        try:
                            self.b = int(input("お金を入力をして下さい。"))
                            end2 = 3
                        except ValueError:
                            print ("お金以外が入力されています。")
                    self.c = menu[self.a]
                    self.d = self.b - self.c
                    break

            else:
                import subprocess
                subprocess.call('clear')
                print ("該当商品がありません。")

    def sold(self):
        if self.d >= 0:
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

        else:
            print ("投入金額が不足しています。")
            self.e = self.c - self.b
            print (str(self.e) + "円足りません。")
            sad = "mata"
            while sad == "mata":
                end7 = 99
                while end7 == 99:
                    try:
                        self.f = int(input("お金を再度入力をして下さい。"))
                        end7 = 88
                    except ValueError:
                        print ("お金以外が入力されています。")
                self.b = self.f + self.b
                self.h = self.b - self.c
                self.i = self.c - self.b
                if self.h >= 0:
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
                    sad = "ryo"

                else:
                    print("投入金額が不足しています。")
                    print (str(self.i) + "円足りません。")

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
                imp = "forever"
                while imp == "forever":
                    from jihann_1 import Ver_1

            else:
                import subprocess
                subprocess.call('clear')
                print ("YesかNo以外が入力されています。")

ver_2 = Ver_2()
while True:
    ver_2.in_menu()
    ver_2.sold()
    ver_2.to_continue()