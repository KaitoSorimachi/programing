import sqlite3
dbfile = sqlite3.connect("jihann.db")
sql = dbfile.cursor()

menu = {"コーラ": 150, "お茶": 120, "酒": 300, "サイダー": 150, "オレンジ": 200}

def choice_2():
    import subprocess
    subprocess.call('clear')
    global which2
    which2 = input("自販機編集メニュー\n1.飲み物個数追加\n2,飲み物種類追加\n3.飲み物種類削除\n操作したい機能番号を入力してください。")

def which2_1():
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

    sql.execute("update jihann set quontity = ? where menu = ? ", (quan2, quan1,))
    sql.execute("select * from jihann ")
    print(sql.fetchall())

def yesorno():
    YesorNo_con = "YN"
    while YesorNo_con == "YN":
        global YesorNo
        YesorNo = input("自販機編集を続けますか？Yes or No")
        if YesorNo == "No":
            import subprocess
            subprocess.call('clear')
            YesorNo_con = "YN_end"

        elif YesorNo == "Yes":
            import subprocess
            subprocess.call('clear')
            YesorNo_con = "YN_end"

        else:
            import subprocess
            subprocess.call('clear')
            print ("YesかNo以外が入力されています。")

def which2_2():
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

def which2_3():
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
            Del = "delok"

        else:
            import subprocess
            subprocess.call('clear')
            print ("メニューにございません。")

def Select_number():
    print ("機能番号以外が入力されています。")

which2_while = "which2_rr"
while which2_while == "which2_rr":
    choice_2()
    if which2 == "1" or which2 == "１":
        which2_1()
        yesorno()
        if YesorNo == "No":
            which2_while = "which2_oo"

    elif which2 == "2" or which2 == "２":
        which2_2()
        yesorno()
        if YesorNo == "No":
            which2_while = "which2_oo"

    elif which2 == "3" or which2 == "３":
        which2_3()
        yesorno()
        if YesorNo == "No":
            which2_while = "which2_oo"

    else:
        Select_number()