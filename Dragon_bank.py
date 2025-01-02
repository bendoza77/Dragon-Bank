class User:

    def __init__(self):
        self.name = self.empty("Enter Your Name: ")
        self.last_name = self.empty("Enter Your Last Name: ")
        self.email = self.empty("Enter Your Email: ")
        self.password = self.empty("Enter Your Password: ")
        self.age = self.get_age()
        self.balance = self.get_balance()
        self.phone_number = self.empty("Enter Your Phone Number: ")
    

    @classmethod
    def show_personal_info(cls,name,last_name,password,age,phone_umber,balance,email):

        return cls(name,last_name,password,phone_umber,age,email,balance)


    def empty(self,info):

        value = input(info)

        while not value:
            value = input(f"{info}cant be empty: ")
        return value

    def get_age(self):

        while True:

            age = input("Enter Your Age: ")

            if age.isdigit():
                return int(age)
            else:
                print("You must enter number not string: ")
        
    def get_balance(self):

        while True:
            amount = int(input("Enter start amount to creat your account. amount must be greater than $10: "))

            if amount >= 10:
                return amount
            if not str(amount):
                print("This field is required")
            else:
                print("Amount must be greater than 10:  ")



    def creat_account(self):

        if not self.name:
            self.name = self.empty("This field is required: ")
        if not self.last_name:
            self.last_name = self.empty("This field is required: ")
        if not self.email:
            self.email = self.empty("This field is required: ")
        if not self.password:
            self.password = self.empty("This field is required: ")
        if not self.age:
            self.age = self.get_age("This field is required")
        if not self.phone_number:
            self.phone_number = self.empty("This field is required: ")
        if not self.balance:
            self.balance = self.get_balance()
        if self.name and self.last_name and self.email and self.age and self.password and self.phone_number and self.balance:
           print()
        
        return self
        
class Balance(User):

    def __init__(self):

        self.balance = float(input("Enter Your start balalnce: "))



class Bankaccount(Balance):

    def withdraw(self):
        while True:
            try:
                withdraw_money = float(input(f"How much money do you want to withdraw from your balance? $ "))
                
                if withdraw_money <= 0:
                    print("Enter a valid amount greater than 0.")
                elif withdraw_money > self.balance:
                    print("Insufficient funds! You can't withdraw more than your current balance.")
                else:
                    self.balance -= withdraw_money
                    print(f"After withdrawal, your balance is ${self.balance}")
                    break  
            except ValueError:
                print("Please enter a valid number.")

    def show_balance(self):
        return f"{self.name} balance is {self.balance}"

    def deposit(self):
        while True:
            try:
                deposit_money = float(input(f"How much money do you want to deposit to your balance? $ "))
                
                if deposit_money <= 0:
                    print("Enter a valid number greater than 0.")
                else:
                    self.balance += deposit_money
                    print(f"After deposit, your balance is ${self.balance}")
                    break 
            except ValueError:
                print("Please enter a valid number.")




class Creatnewaccount(User):
    def __init__(self):
        self.second_name = self.empty("Enter Your New Name: ")
        self.second_last_name = self.empty("Enter Your New Last Name: ")
        self.second_email = self.empty("Enter Your New Email: ")
        self.second_password = self.empty("Enter Your New Password: ")
        self.age = self.get_age()
        self.phone_number = self.empty("Enter Your New Phone Number: ")

    def create_new_account(self):
        print("New account details:")
        new_account = User()
        new_account.name = self.second_name
        new_account.last_name = self.second_last_name
        new_account.age = self.age
        new_account.phone_number = self.phone_number
        new_account.email = self.second_email
        new_account.password = self.second_password
        new_account.balance = self.get_balance()
        print(new_account.show_personal_info())


class Start(User):

    def __init__(self):
        self.users = []
        

    def register(self):
        user = User().creat_account()
        self.users.append(user)

    def new_account(self):
        new = Creatnewaccount().create_new_account()
        self.users.append(new)

    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        print("Invalid email or password.")
        return None

    def delete(self,user):

        try:
            delete = input("do you want delete caaount? (yes/no): ")

            if delete == "yes":
                self.users.remove(user)
                print("account was deleteed")
            else:
                print("delete account cancele.")
        except:
            raise ValueError("you dont  left account to delete.")

    def main(self):

        running = True

        while running:

            print("***********************************************")
            print("Welcome to the Dragon Bank.")
            account = input("Do you have account? yes/no: ")
            print("***********************************************")

            if account == "yes":
                email = self.empty("Enter your email: ")
                password = self.empty("Enter your password: ")

                user = self.login(email,password)

                if user:
                        print("**********************************************")
                        print("This is valid option i can help you.")
                        print("1) Creat New Account.")
                        print("2) Withdraw Money From balance.")
                        print("3) Deposite Money to balance.")
                        print("4) Delete Account.")
                        print("5) Search account information.")
                        print("6) Exit.")
                        print()
                        help = input("Type Number: 1/6. ")
                        print("*********************************************")
                        if help == "1":
                            print(Creatnewaccount().create_new_account())
                            cont = input("want continue? (yes/no): ")
                        if help == "2":
                            print(Bankaccount().withdraw())
                            cont = input("want continue? (yes/no): ")
                        if help == "3":
                            Bankaccount().deposit()
                            cont = input("want continue? (yes/no): ")
                        if help == "4":
                            self.delete(user)
                            cont = input("want continue? (yes/no): ")
                        if help == "5":
                            User.show_personal_info()
                            cont = input("want continue? (yes/no): ")
                        if help == "6":
                            email_res = []
                            password_res = []
                            for i in self.users:
                                email_res.append(i.email)
                                password_res.append(i.password)
                            print(email_res + password_res)
                            cont = input("want continue? (yes/no): ")
                        if help != "1" or help != "2" or help != "3" or help != "4" or help != "5" or help != "6":
                            print("Enter valid optinon")
                        if help == "7":
                            print("Thanks for uing our bank")
                            running = False


                        if cont == "no":
                            print("Thanks for using our bank")
                            running = False
                else:
                    print("login failed")

            elif account == "no":
                self.register()
            else:
                print("Enter only yes or no.")




if __name__ == "__main__":
    Start().main()
