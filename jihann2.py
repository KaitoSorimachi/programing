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
import sqlite3
dbfile = sqlite3.connect("jihann.db")
sql = dbfile.cursor()

menu = {"コーラ": 150, "お茶": 120, "酒": 300, "サイダー": 150, "オレンジ": 200}
mo = 33
while mo == 33:

    print (menu)
    a = input("購入品を選んでください。")

    if a in menu:
        sql.execute("select quontity from jihann where menu = ? ",(a,))
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
            d = b-c
            if d >= 0:
                import subprocess
                subprocess.call('clear')
                print (str(a)+"をお買い上げしました。")
                print ("お釣りは"+str(d)+"円です。")
                upquon = int(fetchresult[0]) - 1
                sql.execute("update jihann set quontity = ? where menu = ?", (upquon, a,))
                sql.execute("select quontity from mydrink where buy = ?", (a,))
                fetchresult2 = sql.fetchone()
                upquon2 = int(fetchresult2[0]) + 1
                sql.execute("update mydrink set quontity = ? where buy = ?", (upquon2, a,))
                print ("{}の購入数これで{}個目です".format(a, upquon2))
            else:
                print ("投入金額が不足しています。")
                e = c-b
                print (str(e)+"円足りません。")
                sad = "mata"
                while sad == "mata":
                    end7 = 99
                    while end7 == 99:
                        try:
                            f = int(input("お金を再度入力をして下さい。"))
                            end7 = 88
                        except ValueError:
                            print ("お金以外が入力されています。")
                    b = f+b
                    h = b-c
                    i = c-b
                    if h >= 0:
                        import subprocess
                        subprocess.call('clear')
                        print (str(a) + "をお買い上げしました。")
                        print ("お釣りは" + str(h) + "円です。")
                        upquon = int(fetchresult[0]) - 1
                        sql.execute("update jihann set quontity = ? where menu = ?", (upquon,a,))
                        sql.execute("select quontity from mydrink where buy = ?",(a,))
                        fetchresult2 = sql.fetchone()
                        upquon2 = int(fetchresult2[0]) + 1
                        sql.execute("update mydrink set quontity = ? where buy = ?", (upquon2,a,))
                        print ("{}の購入数これで{}個目です".format(a,upquon2))
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
            import subprocess
            subprocess.call('clear')
            endflag = 55
        elif x == "No":
            import subprocess
            subprocess.call('clear')
            dbfile.commit()
            dbfile.close()
            import sys
            sys.exit()
        else:
            import subprocess
            subprocess.call('clear')
            print ("YesかNo以外が入力されています。")









