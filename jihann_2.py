import sqlite3
dbfile = sqlite3.connect("jihann.db")
sql = dbfile.cursor()

menu = {"コーラ": 150, "お茶": 120, "酒": 300, "サイダー": 150, "オレンジ": 200}

from jihann_1 import Ver_1

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
        # 購入品を選ぶ
        while True:
            import subprocess
            subprocess.call('clear')
            print (menu)
            self.a = input("購入品を選んでください。")
            if self.a in menu:
                sql.execute("select quontity from jihann where menu = ? ", (self.a,))
                self.fetchresult = sql.fetchone()
                if self.fetchresult[0] == "0":
                    # 売り切れ
                    print ("売り切れです")

                else:
                    # お金を請求
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
                # 該当商品がない
                import subprocess
                subprocess.call('clear')
                print ("該当商品がありません。")

    def sold(self):
        # お買い上げ
        if self.d >= 0:
            import subprocess
            subprocess.call('clear')
            print (str(self.a) + "をお買い上げしました。")
            print ("お釣りは" + str(self.d) + "円です。")
            # 購入個数
            self.upquon = int(self.fetchresult[0]) - 1
            sql.execute("update jihann set quontity = ? where menu = ?", (self.upquon, self.a,))
            sql.execute("select quontity from mydrink where buy = ?", (self.a,))
            self.fetchresult2 = sql.fetchone()
            self.upquon2 = int(self.fetchresult2[0]) + 1
            sql.execute("update mydrink set quontity = ? where buy = ?", (self.upquon2, self.a,))
            print ("{}の購入数これで{}個目です".format(self.a, self.upquon2))

        else:
            # お金が足りない
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
                    # お買い上げ
                    import subprocess
                    subprocess.call('clear')
                    print (str(self.a) + "をお買い上げしました。")
                    print ("お釣りは" + str(self.h) + "円です。")
                    # 購入個数
                    self.upquon = int(self.fetchresult[0]) - 1
                    sql.execute("update jihann set quontity = ? where menu = ?", (self.upquon, self.a,))
                    sql.execute("select quontity from mydrink where buy = ?", (self.a,))
                    self.fetchresult2 = sql.fetchone()
                    self.upquon2 = int(self.fetchresult2[0]) + 1
                    sql.execute("update mydrink set quontity = ? where buy = ?", (self.upquon2, self.a,))
                    print ("{}の購入数これで{}個目です".format(self.a, self.upquon2))
                    sad = "ryo"

                else:
                    # お金が足りない
                    print("投入金額が不足しています。")
                    print (str(self.i) + "円足りません。")

    def to_continue(self):
        # 購入を続けるかどうか
        endflag = "owari"
        while endflag == "owari":
            self.x = input("購入を続けますか？Yes or No")
            if self.x == "Yes":
                # 続ける(繰り返し)
                endflag = 55

            elif self.x == "No":
                # 続けないjihann_1へ
                dbfile.commit()
                import subprocess
                subprocess.call('clear')
                endflag = 55
                ver_1 = Ver_1()
                ver_1.choice()

            else:
                import subprocess
                subprocess.call('clear')
                print ("YesかNo以外が入力されています。")
