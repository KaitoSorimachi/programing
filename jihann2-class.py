class Jihann():
    def __init__(self):
        self.menu = {"コーラ": 150, "お茶": 120, "酒": 300, "サイダー": 150, "オレンジ": 200}
        self.a = ""
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.f = 0
        self.h = 0
        self.i = 0
        self.x = ""

    def senntaku(self):
        while True:
            self.menu = {"コーラ": 150, "お茶": 120, "酒": 300, "サイダー": 150, "オレンジ": 200}
            print (self.menu)
            self.a = input("購入品を選んでください。")

            if self.a in self.menu:
                end2 = 1
                while end2 == 1:
                    try:
                        self.b = int(input("お金を入力をして下さい。"))
                        end2 = 3
                    except ValueError:
                        print ("お金以外が入力されています。")
                break
            else:
                import subprocess
                subprocess.call('clear')
                print ("該当商品がありません。")

    def tariruka(self):
        self.c = self.menu[self.a]
        self.d = self.b - self.c
        if self.d >= 0:
            import subprocess
            subprocess.call('clear')
            print (str(self.a)+"をお買い上げしました。")
            print ("お釣りは"+str(self.d)+"円です。")
        else:
            print ("投入金額が不足しています。")
            self.e = self.c-self.b
            print (str(self.e)+"円足りません。")
            self.mouitido()

    def mouitido(self):
            sad = "mata"
            while sad == "mata":
                end7 = 99
                while end7 == 99:
                    try:
                        self.f = int(input("お金を再度入力をして下さい。"))
                        end7 = 88
                    except ValueError:
                        print ("お金以外が入力されています。")
                self.b = self.f + self.b
                self.h = self.b - self.c
                self.i = self.c - self.b
                if self.h >= 0:
                    import subprocess
                    subprocess.call('clear')
                    print (str(self.a) + "をお買い上げしました。")
                    print ("お釣りは" + str(self.h) + "円です。")
                    sad = "ryo"
                else:
                    print ("投入金額が不足しています。")
                    print (str(self.i) + "円足りません。")


    def tuzukeru(self):
        endflag = "owari"
        while endflag == "owari":
            self.x = input("購入を続けますか？Yes or No")
            if self.x == "Yes":
                import subprocess
                subprocess.call('clear')
                endflag = 55
            elif self.x == "No":
                import subprocess
                subprocess.call('clear')
                import sys
                sys.exit()
            else:
                import subprocess
                subprocess.call('clear')
                print ("YesかNo以外が入力されています。")

jihann = Jihann()
while True:
    jihann.senntaku()
    jihann.tariruka()
    jihann.tuzukeru()

