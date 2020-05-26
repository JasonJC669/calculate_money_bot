class Calculate:
    def __init__(self):
        pass

    def calculate(self, credit):
        """
        input: credit 一個二維陣列，全部人的借貸關係
        """
        self.people = 4  # int(input("總共多少人"))
        row = self.people
        column = self.people
        """
        credit = [list(range(row)) for _ in range(column)]
        for i in range(row):
            for j in range(column):
                if i != j:
                    credit[i][j] = input(f"{i+1}號 要給 {j+1}號 多少錢？")
                else:
                    credit[i][j] = 0
        """
        # print(credit)
        sum = [0]*self.people
        for j in range(self.people):
            sum[j] = 0
            for i in range(row):
                sum[j] = sum[j] + int(credit[i][j])
                sum[j] = sum[j] - int(credit[j][i])

        self.chosen = 1  # int(input("選一個人（輸入號碼）："))
        self.chosen = self.chosen - 1

        return sum
        """
        for i in range(self.people):
            if i != chosen:
                if sum[i] > 0:
                    print(f"{chosen+1}號 要給 {i+1}號 {sum[i]}元")
                else:
                    print(f"{chosen+1}號 要拿 {i+1}號 {-sum[i]}元")
        """
