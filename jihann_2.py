import sqlite3
dbfile = sqlite3.connect("jihann.db")
sql = dbfile.cursor()

menu = {"コーラ": 150, "お茶": 120, "酒": 300, "サイダー": 150, "オレンジ": 200}

def purchased_items():
    import subprocess
    subprocess.call('clear')
    print (menu)
    global a
    a = input("購入品を選んでください。")

def sold_out():
    print ("売り切れです")

def money():
    end2 = 1
    while end2 == 1:
        try:
            global b
            b = int(input("お金を入力をして下さい。"))
            end2 = 3
        except ValueError:
            print ("お金以外が入力されています。")
    global c
    c = menu[a]
    global d
    d = b - c

def sold():
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

def not_enough_money():
    print ("投入金額が不足しています。")
    global e
    global b
    e = c - b
    print (str(e) + "円足りません。")
    end7 = 99
    while end7 == 99:
        try:
            global f
            f = int(input("お金を再度入力をして下さい。"))
            end7 = 88
        except ValueError:
            print ("お金以外が入力されています。")
    b = f + b
    global h
    h = b - c
    global i
    i = c - b


def sold2():
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

def not_enough_money2():
    print ("投入金額が不足しています。")
    print (str(i) + "円足りません。")

def no_product():
    import subprocess
    subprocess.call('clear')
    print ("該当商品がありません。")

def to_continue():
    endflag = "owari"
    while endflag == "owari":
        global x
        x = input("購入を続けますか？Yes or No")
        if x == "Yes":
            endflag = 55

        elif x == "No":
            import subprocess
            subprocess.call('clear')
            endflag = 55

        else:
            import subprocess
            subprocess.call('clear')
            print ("YesかNo以外が入力されています。")





mo = 33
while mo == 33:
    purchased_items()
    if a in menu:
        sql.execute("select quontity from jihann where menu = ? ", (a,))
        fetchresult = sql.fetchone()
        if fetchresult[0] == "0":
            sold_out()
        else:
            money()
            if d >= 0:
                sold()
            else:
                sad = "mata"
                while sad == "mata":
                    not_enough_money()
                    if h >= 0:
                        sold2()
                        sad = "ryo"
                    else:
                        not_enough_money2()

    else:
        no_product()
    to_continue()
    if x == "No":
        mo = 000