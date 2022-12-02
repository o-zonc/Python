# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-11-18
# 과제번호: 11주차 1번

class Customer():
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    
    def withdraw(self, amount):
        amount *= -1
        if self.balance >= amount:
            return self.balance
        else:
            self.balance -= amount
            return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

if __name__ == '__main__':  
    Bill = Customer('Bill', 0)
    Steve = Customer('Steve', 50000)
    Tim = Customer('Tim', 100000)

    cnt = 0
    li = ('Tim', 'Bill', 'Steve')

    while True:
        cnt += 1
        c = cnt % 3
        try:
            amount = int(input(f'{li[c]}에게 입출금할 금액: '))
        except:
            print('프로그램을 종료합니다')
            break
        else:
            if amount > 0:
                if (cnt % 3 == 1):
                    Bill.deposit(amount)
                if (cnt % 3 == 2):
                    Steve.deposit(amount)
                if (cnt % 3 == 0):
                    Tim.deposit(amount)
            else:
                if (cnt % 3 == 1):
                    Bill.withdraw(amount)
                if (cnt % 3 == 2):
                    Steve.withdraw(amount)
                if (cnt % 3 == 0):
                    Tim.deposit(amount)
            
            print(f'Bill 잔액 {Bill.balance} 원')
            print(f'Steve 잔액 {Steve.balance} 원')
            print(f'Tim 잔액 {Tim.balance} 원')
            print()