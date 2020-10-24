import sqlite3
dbfile = sqlite3.connect("jihann.db")
sql = dbfile.cursor()
"""
sql.execute("create table jihann(menu,quontity)")
sql.execute("INSERT INTO jihann VALUES('コーラ','10')")
sql.execute("INSERT INTO jihann VALUES('お茶','10')")
sql.execute("INSERT INTO jihann VALUES('酒','10')")
sql.execute("INSERT INTO jihann VALUES('サイダー','10')")
sql.execute("INSERT INTO jihann VALUES('オレンジ','10')")
"""
#sql.execute("select * from jihann ")
a = "コーラ"
sql.execute("select quontity from jihann where menu = ? ", (a,))
#print(sql.fetchone())
fetchresult = sql.fetchone()
if fetchresult[0] == "5":
    print ("OK")
else:
    print ("NG")
sql.execute("update jihann set quontity = '5' where menu = 'コーラ'")
sql.execute("select * from jihann ")
print(sql.fetchone())

"""
sql.execute("create table mydrink(buy,quontity)")
sql.execute("INSERT INTO mydrink VALUES('コーラ','0')")
sql.execute("INSERT INTO mydrink VALUES('お茶','0')")
sql.execute("INSERT INTO mydrink VALUES('酒','0')")
sql.execute("INSERT INTO mydrink VALUES('サイダー','0')")
sql.execute("INSERT INTO mydrink VALUES('オレンジ','0')")
"""
#sql.execute("delete from mydrink where buy = 'ぶどう' ")
sql.execute("select * from mydrink ")
a = sql.fetchall()
print(a)
dbfile.commit()
dbfile.close()