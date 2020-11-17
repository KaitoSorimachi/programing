import sqlite3
dbfile = sqlite3.connect("jihann.db")
sql = dbfile.cursor()

menu = {"コーラ": 150, "お茶": 120, "酒": 300, "サイダー": 150, "オレンジ": 200}

class Ver_3():
    def __init__(self):
        self.which2 = ""
        self.quan1 = ""
        self.quan2 = 0
        self.fetchresult3 = ""
        self.a = ""
        self.inquon = 0
        self.disposal = ""
        self.YesorNo = ""

    def choice_2(self):
        import subprocess
        subprocess.call('clear')
        which2_while = "which2_rr"
        while which2_while == "which2_rr":
            try:
                self.which2 = int(input("自販機編集メニュー\n1.飲み物個数追加\n2,飲み物種類追加\n3.飲み物種類削除\n操作したい機能番号を入力してください。"))
                if self.which2 == 1 or self.which2 == 2 or self.which2 == 3:
                    which2_while = "which2_oo"
                else:
                    print ("機能番号以外が入力されています。")
            except ValueError:
                print ("機能番号以外が入力されています。")

    def which2_1(self):
        if self.which2 == 1:
            import subprocess
            subprocess.call('clear')
            TE = "te"
            while TE == "te":
                sql.execute("select * from jihann ")
                print(sql.fetchall())
                self.quan1 = input("何を仕入れますか？")
                if self.quan1 in menu:
                    TE2 = "te2"
                    while TE2 == "te2":
                        try:
                            self.quan2 = int(input("いくつ仕入れますか？"))
                            TE2 = "teok2"
                            TE = "teok"
                        except ValueError:
                            print ("数値以外が入力されています。")

                else:
                    import subprocess
                    subprocess.call('clear')
                    print ("メニューにございません。")

            sql.execute("select quontity from jihann where menu = ? ", (self.quan1,))
            self.fetchresult3 = sql.fetchone()
            self.quan2 = self.fetchresult3[0] + self.quan2
            sql.execute("update jihann set quontity = ? where menu = ? ", (self.quan2, self.quan1,))
            sql.execute("select * from jihann ")
            print(sql.fetchall())

    def which2_2(self):
        if self.which2 == 2:
            import subprocess
            subprocess.call('clear')
            self.a = input("何を追加しますか？")
            menu[self.a] = 200
            inqu = 116
            while inqu == 116:
                try:
                    self.inquon = int(input("いくつ仕入れますか？"))
                    inqu = 114
                except ValueError:
                    print ("数値以外が入力されています。")
            sql.execute("INSERT INTO jihann VALUES(?,?)", (self.a, self.inquon))
            sql.execute("INSERT INTO mydrink VALUES(?,'0')", (self.a,))
            sql.execute("select * from jihann ")
            print(sql.fetchall())

    def which2_3(self):
        if self.which2 == 3:
            import subprocess
            subprocess.call('clear')
            Del = "del"
            while Del == "del":
                print (menu)
                self.disposal = input("何を削除しますか？")
                if self.disposal in menu:
                    sql.execute("delete from jihann where menu = ?", (self.disposal,))
                    sql.execute("delete from mydrink where buy = ?", (self.disposal,))
                    del menu[self.disposal]
                    sql.execute("select * from jihann ")
                    print(sql.fetchall())
                    Del = "delok"

                else:
                    import subprocess
                    subprocess.call('clear')
                    print ("メニューにございません。")

    def yesorno(self):
        YesorNo_con = "YN"
        while YesorNo_con == "YN":
            self.YesorNo = input("自販機編集を続けますか？Yes or No")
            if self.YesorNo == "No":
                dbfile.commit()
                dbfile.close()
                import subprocess
                subprocess.call('clear')
                YesorNo_con = "YN_end"
                imp = "forever"
                while imp == "forever":
                    from jihann_1 import Ver_1

            elif self.YesorNo == "Yes":
                import subprocess
                subprocess.call('clear')
                YesorNo_con = "YN_end"

            else:
                import subprocess
                subprocess.call('clear')
                print ("YesかNo以外が入力されています。")

ver_3 = Ver_3()
ver_3.choice_2()
ver_3.which2_1()
ver_3.which2_2()
ver_3.which2_3()
ver_3.yesorno()