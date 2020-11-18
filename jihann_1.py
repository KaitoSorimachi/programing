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
            try:
                self.which = int(input("メニュー画面\n1.自販機飲み物購入\n2.自販機編集\n3.終了\n操作したい機能番号を入力してください。"))
                if self.which == 1:
                    from jihann_2 import Ver_2

                elif self.which == 2:
                    from jihann_3 import Ver_3

                elif self.which == 3:
                    dbfile.commit()
                    dbfile.close()
                    import sys
                    sys.exit()

                else:
                    print ("機能番号以外が入力されています。")

            except ValueError:
                import subprocess
                subprocess.call('clear')
                print ("機能番号以外が入力されています。")


ver_1 = Ver_1()
ver_1.choice()

