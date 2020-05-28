class Calculate:

    def __init__(self, people):
        self.people = people  # int(input("總共多少人"))
        self.credit = [[0 for _ in range(self.people)]
                       for _ in range(self.people)]
        self.changeusername = {}
        self.chosen = 0
        self.changeid = {}

    def change(self, username):
        if username in self.changeusername:
            pass
        else:
            self.changeusername[username] = len(
                self.changeusername) + 1
            self.changeusername[username] -= 1
        return self.changeusername[username]

    def lend(self, Alost, toB, money):
        A = self.change(Alost)
        B = self.change('@'+toB)
        self.credit[A][B] = self.credit[A][B] + int(money)

    def calculate(self):
        """
        input: credit 一個二維陣列，全部人的借貸關係
        """
        sum = [0]*self.people
        for j in range(self.people):
            sum[j] = 0
            for i in range(self.people):
                sum[j] = sum[j] + int(self.credit[i][j])
                sum[j] = sum[j] - int(self.credit[j][i])
        return sum

    def setchosen(self, name):
        self.chosen = self.change(name)

    def getchosen(self):
        return self.chosen

    def getusername(self, userid):
        self.changeid = dict((v, k) for k, v in self.changeusername.items())
        return self.changeid[userid]

    def clear(self):
        self.credit = [[0 for _ in range(self.people)]
                       for _ in range(self.people)]
