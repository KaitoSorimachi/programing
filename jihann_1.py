import subprocess
subprocess.call('clear')

import sqlite3
dbfile = sqlite3.connect("jihann.db")
sql = dbfile.cursor()

class Ver_1():
    def __init__(self):
        self.which = 0

    def choice(self):
        which_while = "which_rr"
        while which_while == "which_rr":
            self.which = input("メニュー画面\n1.自販機飲み物購入\n2.自販機編集\n3.終了\n操作したい機能番号を入力してください。")
            if self.which == "1" or self.which == "１":
                imp = "forever"
                while imp == "forever":
                    import jihann_2

            elif self.which == "2" or self.which == "２":
                imp = "forever"
                while imp == "forever":
                    import jihann_3

            elif self.which == "3" or self.which == "３":
                dbfile.commit()
                dbfile.close()
                import sys
                sys.exit()

            else:
                import subprocess
                subprocess.call('clear')
                print ("機能番号以外が入力されています。")

ver_1 = Ver_1()
ver_1.choice()

