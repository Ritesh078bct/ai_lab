class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    def deposit_balance(self,account_number,balance):
        if account_number == self.__account_number:
            self.__balance=self.__balance+balance
            print(f"you deposited Rs.{balance},total amount:{self.__balance}")

    def withdraw_balance(self,account_number,balance):
        if account_number == self.__account_number:
            self.__balance=self.__balance-balance
            print(f"you withdraw Rs.{balance},total amount:{self.__balance}")

    def __str__(self):
        return f"Your account number:{self.__account_number}\nBalance:{self.__balance}"

if __name__ == "__main__":
    my_account=BankAccount(321,10000)
    print(my_account)
    # my_account.deposit_balance(321,100)
