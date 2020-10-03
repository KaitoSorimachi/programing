"""
金額を入力するとその金額を出来るだけ少ない枚数の貨幣を使って支払えるように貨幣の枚数を数えるプログラムを書いて下さい。貨幣は、{１万円札、五千円札、千円札、五百円玉、百円玉、五十円玉、十円玉、五円玉、一円玉}とする（余り使わないので２千円札は除く）。
実行結果
金額(円)> 48767
金額: 48767 円
一万円札= 4 枚
五千円札= 1 枚
千円札　= 3 枚
五百円玉= 1 枚
百円玉　= 2 枚
五十円玉= 1 枚
十円玉　= 1 枚
五円玉　= 1 枚
一円玉　= 2 枚
"""
suuji = 11
while suuji == 11:
    try:
        money = int(input("金額(円)>"))
        suuji = "ii"
    except ValueError:
        print ("お金以外が入力されています。")

print ("金額:"+str(money))
a = money // 10000
money = money % 10000
b = money // 5000
money = money % 5000
c = money // 1000
money = money % 1000
d = money // 500
money = money % 500
e = money // 100
money = money % 100
f = money // 50
money = money % 50
g = money // 10
money = money % 10
h = money // 5
i = money % 5

print ("一万円札 = "+str(a)+"枚")
print ("五千円札 = "+str(b)+"枚")
print ("千円札 = "+str(c)+"枚")
print ("五百円玉 = "+str(d)+"枚")
print ("百円玉 = "+str(e)+"枚")
print ("五十円玉 = "+str(f)+"枚")
print ("十円玉 = "+str(g)+"枚")
print ("五円玉 = "+str(h)+"枚")
print ("一円玉 = "+str(i)+"枚")

