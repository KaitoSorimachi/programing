class Kigou:
    def __init__(self):
        endflag = "owari"
        while endflag == "owari":
            try:
                self.a=int(input("数値を入力して下さい。"))
                endflag = "hajimari"
            except ValueError:
                print ("数値以外が入力されています。")

    def ikutu(self):
        print (str(self.a) + ":", end="")
        for i in range(self.a):
            print ("■", end="")

kigou=Kigou()
kigou.ikutu()



