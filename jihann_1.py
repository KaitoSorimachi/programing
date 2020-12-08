import subprocess
subprocess.call('clear')

import sqlite3
dbfile = sqlite3.connect("jihann.db")
sql = dbfile.cursor()

from jihann_2 import Ver_2
from jihann_3 import Ver_3

class Ver_1():
    def __init__(self):
        self.which = 0

    def choice(self):
        which_while = "which_rr"
        while which_while == "which_rr":
            try:
                # メニュー画面
                self.which = int(input("メニュー画面\n1.自販機飲み物購入\n2.自販機編集\n3.終了\n操作したい機能番号を入力してください。"))
                if self.which == 1:
                    # 自販機飲み物購入jihann_2へ
                    ver_2 = Ver_2()
                    while True:
                        ver_2.in_menu()
                        ver_2.sold()
                        ver_2.to_continue()

                elif self.which == 2:
                    # 自販機編集jihann_3へ
                    ver_3 = Ver_3()
                    while True:
                        ver_3.choice_2()
                        re = ver_3.choice_2()
                        if re == 1:
                            ver_3.which2_1()
                        elif re == 2:
                            ver_3.which2_2()
                        else:
                            ver_3.which2_3()
                        ver_3.yesorno()

                elif self.which == 3:
                    # 終了
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

