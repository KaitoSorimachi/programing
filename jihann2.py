"""
自動販売機プログラムを作成して下さい。
最初にコンソールに購入できる飲み物を出力させて下さい。
その後
キーボードから入力を行わせ、
入力された文言に対して判定をかけて
該当商品が存在すれば投入金額を入力させ、
該当商品ががない場合は、
「該当商品がありません」とメッセージを出力させ、
購入を続けるか問いて下さい。
投入金額を入力後
足りない場合は
「投入金額が不足しています」
「○○○○○円足りません」
と出力させる。
足りた場合且つ、お釣りが出る場合、
「○○○○を購入しました。」
「お釣りは￥○○○です」
と出力させる
購入を続けるか、購入を終了するかを選ばせ
続ける場合は、画面をクリアして
自動販売機の商品を再度表示させ
終了する場合はそのままプログラムを終了させる
"""
# -*- coding: utf-8 -*-

import sqlite3
dbfile = sqlite3.connect("jihann.db")
sql = dbfile.cursor()

import subprocess
subprocess.call('clear')

menu = {"コーラ": 150, "お茶": 120, "酒": 300, "サイダー": 150, "オレンジ": 200}

which_while = "which_rr"
while which_while == "which_rr":
    which = input("メニュー画面\n1.自販機飲み物購入\n2.自販機編集\n3.終了\n操作したい機能番号を入力してください。")
    if which == "1" or which == "１":
        mo = 33
        while mo == 33:
            import subprocess
            subprocess.call('clear')
            print (menu)
            a = input("購入品を選んでください。")
            if a in menu:
                sql.execute("select quontity from jihann where menu = ? ", (a,))
                fetchresult = sql.fetchone()
                if fetchresult[0] == "0":
                    print ("売り切れです")

                else:
                    end2 = 1
                    while end2 == 1:
                        try:
                            b = int(input("お金を入力をして下さい。"))
                            end2 = 3
                        except ValueError:
                            print ("お金以外が入力されています。")
                    c = menu[a]
                    d = b - c
                    if d >= 0:
                        import subprocess
                        subprocess.call('clear')
                        print (str(a) + "をお買い上げしました。")
                        print ("お釣りは" + str(d) + "円です。")
                        upquon = int(fetchresult[0]) - 1
                        sql.execute("update jihann set quontity = ? where menu = ?", (upquon, a,))
                        sql.execute("select quontity from mydrink where buy = ?", (a,))
                        fetchresult2 = sql.fetchone()
                        upquon2 = int(fetchresult2[0]) + 1
                        sql.execute("update mydrink set quontity = ? where buy = ?", (upquon2, a,))
                        print ("{}の購入数これで{}個目です".format(a, upquon2))

                    else:
                        print ("投入金額が不足しています。")
                        e = c - b
                        print (str(e) + "円足りません。")
                        sad = "mata"
                        while sad == "mata":
                            end7 = 99
                            while end7 == 99:
                                try:
                                    f = int(input("お金を再度入力をして下さい。"))
                                    end7 = 88
                                except ValueError:
                                    print ("お金以外が入力されています。")
                            b = f + b
                            h = b - c
                            i = c - b
                            if h >= 0:
                                import subprocess
                                subprocess.call('clear')
                                print (str(a) + "をお買い上げしました。")
                                print ("お釣りは" + str(h) + "円です。")
                                upquon = int(fetchresult[0]) - 1
                                sql.execute("update jihann set quontity = ? where menu = ?", (upquon, a,))
                                sql.execute("select quontity from mydrink where buy = ?", (a,))
                                fetchresult2 = sql.fetchone()
                                upquon2 = int(fetchresult2[0]) + 1
                                sql.execute("update mydrink set quontity = ? where buy = ?", (upquon2, a,))
                                print ("{}の購入数これで{}個目です".format(a, upquon2))
                                sad = "ryo"

                            else:
                                print ("投入金額が不足しています。")
                                print (str(i) + "円足りません。")

            else:
                import subprocess
                subprocess.call('clear')
                print ("該当商品がありません。")

            endflag = "owari"
            while endflag == "owari":
                x = input("購入を続けますか？Yes or No")
                if x == "Yes":
                    endflag = 55

                elif x == "No":
                    import subprocess
                    subprocess.call('clear')
                    endflag = 55
                    mo = 000

                else:
                    import subprocess
                    subprocess.call('clear')
                    print ("YesかNo以外が入力されています。")

    elif which == "2" or which == "２":
        import subprocess
        subprocess.call('clear')
        which2_while = "which2_rr"
        while which2_while == "which2_rr":
            which2 = input("自販機編集メニュー\n1.飲み物個数追加\n2,飲み物種類追加\n3.飲み物種類削除\n操作したい機能番号を入力してください。")
            if which2 == "1" or which2 == "１":
                import subprocess
                subprocess.call('clear')
                TE = "te"
                while TE == "te":
                    sql.execute("select * from jihann ")
                    print(sql.fetchall())
                    quan1 = input("何を仕入れますか？")
                    if quan1 in menu:
                        TE2 = "te2"
                        while TE2 == "te2":
                            try:
                                quan2 = int(input("いくつ仕入れますか？"))
                                TE2 = "teok2"
                                TE = "teok"
                            except ValueError:
                                print ("数値以外が入力されています。")

                    else:
                        import subprocess
                        subprocess.call('clear')
                        print ("メニューにございません。")

                sql.execute("update jihann set quontity = ? where menu = ? ", (quan2, quan1, ))
                sql.execute("select * from jihann ")
                print(sql.fetchall())
                YesorNo_con = "YN"
                while YesorNo_con == "YN":
                    YesorNo = input("自販機編集を続けますか？Yes or No")
                    if YesorNo == "No":
                        import subprocess
                        subprocess.call('clear')
                        which2_while = "which2_oo"
                        YesorNo_con = "YN_end"

                    elif YesorNo == "Yes":
                        import subprocess
                        subprocess.call('clear')
                        YesorNo_con = "YN_end"

                    else:
                        import subprocess
                        subprocess.call('clear')
                        print ("YesかNo以外が入力されています。")

            elif which2 == "2" or which2 == "２":
                import subprocess
                subprocess.call('clear')
                a = input("何を追加しますか？")
                menu[a] = 200
                inqu = 116
                while inqu == 116:
                    try:
                        inquon = int(input("いくつ仕入れますか？"))
                        inqu = 114
                    except ValueError:
                        print ("数値以外が入力されています。")
                sql.execute("INSERT INTO jihann VALUES(?,?)", (a, inquon))
                sql.execute("INSERT INTO mydrink VALUES(?,'0')", (a,))
                sql.execute("select * from jihann ")
                print(sql.fetchall())
                YesorNo_con2 = "YN2"
                while YesorNo_con2 == "YN2":
                    YesorNo2 = input("自販機編集を続けますか？Yes or No")
                    if YesorNo2 == "No":
                        import subprocess
                        subprocess.call('clear')
                        which2_while = "which2_oo"
                        YesorNo_con2 = "YN_end2"

                    elif YesorNo2 == "Yes":
                        import subprocess
                        subprocess.call('clear')
                        YesorNo_con2 = "YN_end2"

                    else:
                        import subprocess
                        subprocess.call('clear')
                        print ("YesかNo以外が入力されています。")

            elif which2 == "3" or which2 == "３":
                import subprocess
                subprocess.call('clear')
                Del = "del"
                while Del == "del":
                    print (menu)
                    disposal = input("何を削除しますか？")
                    if disposal in menu:
                        sql.execute("delete from jihann where menu = ?", (disposal,))
                        sql.execute("delete from mydrink where buy = ?", (disposal,))
                        del menu[disposal]
                        sql.execute("select * from jihann ")
                        print(sql.fetchall())
                        YesorNo_con3 = "YN3"
                        while YesorNo_con3 == "YN3":
                            YesorNo3 = input("自販機編集を続けますか？Yes or No")
                            if YesorNo3 == "No":
                                import subprocess
                                subprocess.call('clear')
                                which2_while = "which2_oo"
                                YesorNo_con3 = "YN_end3"
                                Del = "delok"

                            elif YesorNo3 == "Yes":
                                import subprocess
                                subprocess.call('clear')
                                YesorNo_con3 = "YN_end3"
                                Del = "delok"

                            else:
                                import subprocess
                                subprocess.call('clear')
                                print ("YesかNo以外が入力されています。")

                    else:
                        import subprocess
                        subprocess.call('clear')
                        print ("メニューにございません。")

            else:
                print ("機能番号以外が入力されています。")

    elif which == "3" or which == "３":
        dbfile.commit()
        dbfile.close()
        import sys
        sys.exit()

    else:
        import subprocess
        subprocess.call('clear')
        print ("機能番号以外が入力されています。")







