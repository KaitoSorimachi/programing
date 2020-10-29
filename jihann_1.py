import sqlite3
dbfile = sqlite3.connect("jihann.db")
sql = dbfile.cursor()

import subprocess
subprocess.call('clear')

def choice():
    which_while = "which_rr"
    while which_while == "which_rr":
        which = input("メニュー画面\n1.自販機飲み物購入\n2.自販機編集\n3.終了\n操作したい機能番号を入力してください。")
        if which == "1" or which == "１":
            imp = "forever"
            while imp == "forever":
                import jihann_2

        elif which == "2" or which == "２":
            imp = "forever"
            while imp == "forever":
                import jihann_3

        elif which == "3" or which == "３":
            dbfile.commit()
            dbfile.close()
            import sys
            sys.exit()

        else:
            import subprocess
            subprocess.call('clear')
            print ("機能番号以外が入力されています。")

choice()

