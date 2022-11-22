class Function:

    def __init__(self):
        self.x = int(input("Enter a number you want to find the Sequential Number Table of(Numbers only): \n"))
        # self.l1 = []

    def multiplants(self):
        if self.x > 0:
            self.num = 1
            for number in range(10):
                print(f"{self.x} * {self.num} = {self.x * self.num}")
                self.num += 1
            print("\n")
        else:
            print("Invalid Number")

    def result(self):

        for _ in range(self.x - 1):

            self.x -= 1
            Function.multiplants(self)

