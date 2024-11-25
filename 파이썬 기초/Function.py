def open_account():
    print("새로운 계좌 생성")

open_account()

def deposit(balance, money): #입금
    print("입금완료. 잔액은 {0} 원", format(balance+money))
    return balance+money

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금완료. 잔액은 {0} 원", format(balance-money))
        return balance- money
    else:
        print("출금 xxxxxxx. 잔액은 {0}원", format(balance))
        return balance

def withdraw_night(balance, money): #저녁 출금
    commision = 100
    return commision, balance - money - commision

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
commision, balance =withdraw_night(balance, 500)
print("수수료 {0}원이고, 잔액은 {1}원임".format(commision, balance))