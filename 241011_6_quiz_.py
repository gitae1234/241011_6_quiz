class login:
    def __init__(self, name, age, tp):

        self.name = name
        self.age = age
        self.tp = tp

    def info(self):
        print("이름: self.name")
        print("나이: self.age")
        print("연락처: self.tp")

login1 = login('이름', '나이', '연락처')
login.info()



