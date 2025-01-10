# Here I have imported some built-in functions from the rich library that help me create the terminal design.
from rich.console import Console # The Console() function that helps me print colored text and styled texted
from rich.prompt import Prompt # The Prompt() function is same as input function
from rich.panel import Panel # The Panel() funciton helps me to create border for teminal design.

console = Console() # I create console value Which I left behind to Console() function, beacouse that was more easyer.

# Here I created a class called User that has several methods written in it, 
# and these methods create a user account and retrieve their personal account.
class User:


    # This is init (instance) method where i write what users need to register and create their accounte
    # name,last_name,passsord,age,balance,phone_number all this is object
    def __init__(self, name="", last_name="", email="", password="", age=None, balance=0, phone_number=""):
        self.name = name 
        self.last_name = last_name
        self.email = email
        self.password = password
        self.age = age
        self.balance = balance
        self.phone_number = phone_number

    # This function displays the information entered by the user, i.e. personal information.
    def show_personal_info(self):
        print("This is your personal information")
        print(f"Name: {self.name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Age: {self.age}")
        print(f"Balance: {self.balance}")
        print(f"Phone Number: {self.phone_number}")

    # This feature protects against fake age  entered by the user, 
    # meaning the user will not be able to enter anything other than an age.

    def get_age(self):
        while True:
            age = input("Enter Your Age: ")
            if age.isdigit() and int(age) >= 18 and int(age) <= 70: #if age is greater than 18 and less than 70 return age
                return int(age)
            # else print alert message for users.
            else:
                console.print("You must be 18 or more years old.", style="bold red") #console.print() is same as print() function but
                                                                                     # difference is that console.print() function help us
                                                                                     # to print colored and designed text.


    # This feature protects against fake emails entered by the user, 
    # meaning the user will not be able to enter anything other than an email.

    def valid_email(self):
        while True:
            email = Prompt.ask("Email: ")

            if email[-10:] == "@gmail.com":  #if email last ten element is equal "@gmail.com" return email 
                return email
            # esle print alert message for users
            else:
                console.print("Enter Valid Email", style="bold red") #style property have only Console() funciton and its help us to print()
                                                                     # colored text


    # This feature tell users that she/he must enter start amount to create accounte
    def get_balance(self):

        # if amount is less than 10 code must print alert message for users else return int(amount) beacouse input's data type is str.
        while True:
            amount = input("Enter start amount to create your account. Amount must be greater than $10: ")
            if amount.isdigit():
                amount = int(amount)
                if amount >= 10:
                    return amount
                else:
                    console.print("Amount must be greater than 10.",style="bold red")
            else:
                console.print("Please enter a valid number.", style="bold red")

    def empty(self,info):
        value = input(info)

        while not value:
            value = input("This field is required: ")

        return value


    # This feature tell users that she/he must eneter her name to create accounte.

    def valid_name(self):

        # while true code must ask users to enter her name is name input is empty code must print alert message else return name.
        while True:
            name = Prompt.ask("Name: ")

            if not name:
                console.print("Enter Valid Name", style="bold red")
            else:
                return name
        


    # This funciton tells users to enter create password for create their accounte.
    def valid_password(self):
        # while true code ask users that she/he must enter password to create accout but if password input is empty code print
        # alert message for user else return password
        while True:
            password = Prompt.ask("Password")

            if not password:
                console.print("Enter Valid Password", style="bold red")
            else:
                return password

    # This function tells users to eneter create password for create their accounte.
    def valid_last_name(self):

        # while true code ask user to enter their last name and if last name input is empty code will print alert message else code 
        # return last name
        while True:
            last_name = Prompt.ask("Last Name: ")

            if not last_name:
                console.print("Enter valid Last Name: ", style="bold red")
            else:
                return last_name

    # This function tells users to enter create password for create their accounte.
    def valid_phone_number(self):

        # while true code ask users phone number
        while True:
            phone_number = Prompt.ask("Phone Number")

            if len(phone_number) == 9: # if phone number length is less than 9 code print alert message else return phone number
                return phone_number
            else:
                console.print("Enter Valid Phone Number", style="bold red")

    # This function create accounte by users information.
    def create_account(self):
        # if name object is empty name object will equal to valid_name() whats mean we call valid_name_funciton 
        # to sign up our name fucntion thats why in every function i write return
        if not self.name:
            self.name = self.valid_name()
        # if last name object is empty last name object will equal to valid_last_name() function whats mean we call valid_last_name
        # function to sign up our last name
        if not self.last_name:
            self.last_name = self.valid_last_name()
        # if email object is empty email object will equal to valid_email() function whats mean we code call function valid_email()
        # to sign up our email.
        if not self.email:
            self.email = self.valid_email()
        # if email object is empty password object will equal to password() function whats mean we code call function valid_password()
        # to sign up our password.
        if not self.password:
            self.password = self.valid_password()
        # if email object is empty age object will equal to get_age() function whats mean we code call function get_age()
        # to sign up our age.
        if not self.age:
            self.age = self.get_age()
        # if email object is empty phone number object will equal to valid_phone_number() function whats mean we code call function valid_phone_number()
        # to sign up our valid_phone_number.
        if not self.phone_number:
            self.phone_number = self.valid_phone_number()
        # if email object is empty balance object will equal to get_balance() function whats mean we code call function get_balance()
        # to sign up our balance.
        if not self.balance:
            self.balance = self.get_balance()

        # if none of them is empty code will print message that tell users they create accounte saccessfuly and code will return all object, 
        # else code print alert message .
        if all([self.name, self.last_name, self.email, self.age, self.password, self.phone_number, self.balance]):
            console.print("Account successfully created.", style="bold green")
        else:
            console.print("There was an error creating the account.", style="bold red")
        return self
        

# This is Bankaccunte class that has several methods written in it,
# which methods help users to deposite or withdraw money form their balance.
class Bankaccount:


    # This is init (instance) method where is only balance parametr and created only balance object beacouse.
    # deposite and withdraw methods need only balance object and i write this code to get balance object from User class.
    def __init__(self,balance,):
        self.balance = balance


    # This function helps users to withdraw money from their balance.
    def withdraw(self):
        # i use try excpet method to create my own error. while true code ask users that how much money they wnat to withdarw from
        # their balance and if withdraw_amount is greater than balance or withdraw_amoutn is equal 0 or withdraw_amount is less than 0 
        # code will print alert message, else amount will minus to balance and code print message to how much moneny users have to their balance after withdraw.
        while True:
            try:
                withdraw_money = float(input(f"How much money do you want to withdraw from your balance? $ "))
                
                if withdraw_money <= 0:
                    console.print("Enter a valid amount greater than 0.", style="bold red")
                elif withdraw_money > self.balance:
                    console.print("Insufficient funds! You can't withdraw more than your current balance.", style="bold red")
                else:
                    self.balance -= withdraw_money
                    print(f"After withdrawal, your balance is ${self.balance}")
                    break  
            except ValueError:
                console.print("Please enter a valid number.", style="bold red")

    # This function helps users to deposite money to their balance.
    def deposit(self):
        # in this function i also use try/excpet method to create my own error. while true code ask users that how much money
        # they want to deposite to their balance.
        while True:
            try:
                deposit_money = float(input(f"How much money do you want to deposit to your balance? $ "))
                
                # if deposite_money is less than 0 or deposite_money is equal to 0 code will print alert message else code plus
                # deposite_money to balance and code will print message that how much money they have after deposite money.
                if deposit_money <= 0:
                    console.print("Enter a valid number greater than 0.", style="bold red")
                else:
                    self.balance += deposit_money
                    print(f"After deposit, your balance is ${self.balance}")
                    break 
            except ValueError:
                console.print("Please enter a valid number.", style="bold red")


# This is Start class also know the main class wich is child of User (paranet) class that has several methods written in it,
# which methods helps users to register or login after register and delet your account,
class Start(User):

    # This is init (instance) method where i created list of users and list of bank where is all accounte balance.
    def __init__(self):
        self.users = [] # This list and also bank list is like a data base for this entire code.
        self.bank = []
        
    # This is registre funciton that is same as create_accounte funciton bu difference is that in this function create object where is
    # nothing beacouse i want to create object not by myself but also by users entered information.
    def register(self):
        user = User("", "", "", "", None, 0, "")
        user = user.create_account() # this function work by user value beacouse user value i left behind created object by User class.
        bank = Bankaccount(user.balance) # this is value bank left behinde Bankaccounte class and i create object where is only balance
                                         # beacouse Bankaccounte need only balance parameter.
        self.users.append(user) # in this line of code where self.users is list i append accounte which is created by user eneterd information
        self.bank.append(bank) # and this line of code where self.bank is also list i append balance of all acounte



    # This is login funciton wich helps users to login to their accounte after create accounte. this function have only two parametre
    # beacouse i want to sign up user by she/he's email and password.
    def login(self, email, password):
        # i loop list of accounte and i get only email and password from list and equal to parameter.
        for user in self.users:
            if user.email == email and user.password == password: # if email parameter is equal to realy email and password parameter is equal
                                                                  # realy password code will return user else code will print alert message and return None.
                return user
        console.print("Invalid email or password.", style="bold red")
        return None


    # This funciton helps users to delete accounte.
    def delete(self):
        # in this function i also use try/except method to create my own error. while true code ask users question and if answer is "no"
        # code will print message "delet accounte cancel" else answer is "yes" code will delet latest accounte that was created
        #  by users enter information.
        try:
            delete = input("do you want delete caaount? (yes/no): ")

            if delete == "yes":
                self.users.pop()
                console.print("account was deleteed", style="bold green")
            else:
                console.print("delete account cancel.", style="bold green")
        except ValueError:
            console.print("You dont left any accout to delete", style="bold red")


    # This main accounte where is entire code.
    def main(self):

        # i created value running and left behined bool True.
        running = True

        # while running also while true code aks users question that users have or not accounte.
        while running:
            print("********************************************")
            print("Welcome To The Dragon Bank.")
            account = input("Do you have account? (yes/no): ")
            print("********************************************")

            # answer is "yes" and users list length is equal 0 code will alert message.
            if account == "yes" and len(self.users) == 0:
                console.print("You don't have an account. Please create one.", style="bold red")
            # if answer is "yes" and users length is gerater than 1 or equal to 1 code will ask users their email and password.
            elif account == "yes" and len(self.users) >= 1:
                email = self.empty("Enter your email: ")
                password = self.empty("Enter your password: ")

                # in this line of code i created user value left behined login function which have two parameter email input
                # and password input. that why login funcion have two parameter
                user = self.login(email, password)

                # if user (login function) is not empty code will print that user login saccssefuly to their accounte.
                if user:
                    console.print("You Login successfully", style="bold green")
                    bank = self.bank[0] # This is bank list and i left behined first index
                    # while true code will print all valid option dragon bank can do for users
                    while True:
                        # i use Panel function from rich libary to design main menu
                        menu = """
                                        This is Valid Option Dragon Bank Can Help You.
[bold yellow]1)[/bold yellow] Create New Account.
[bold yellow]2)[/bold yellow] Withdraw Money From balance.
[bold yellow]3)[/bold yellow] Deposit Money to balance.
[bold yellow]4)[/bold yellow] Show balance.
[bold yellow]5)[/bold yellow] Delete Account.
[bold yellow]6)[/bold yellow] Search Account Information.
[bold yellow]7)[/bold yellow] See users of our bank.
[bold yellow]8)[/bold yellow] Change account.
[bold yellow]9)[/bold yellow] Exit.
"""                     # this is title design of border
                        console.print(Panel(menu, title="[bold green]Main Menu[/bold green]", border_style="magenta")) 
                        help_option = input("Type Number: 1/6. ")
                        print("*********************************************")

                        # i use if else condition to call every funciton from entire code by users desire.
                        if help_option == "1":
                            # if user enter number "1" code will call register function
                            self.register()
                        elif help_option == "2":
                            # if user enter number "2" code will call withdraw function
                            bank.withdraw()
                        elif help_option == "3":
                            # if user enter number "3" code will call deposit function
                            bank.deposit()
                        elif help_option == "4":
                            # if user  enter number "4" code will print every users balance.
                            for i in self.bank:
                                print(f"Your balance is ${i.balance}")
                        elif help_option == "5":
                            # if user enter number "5" code will call delete function.
                            self.delete()
                            break # this mean to stop function
                        elif help_option == "6":
                            # if user enter number "6" code will call function show_personal_info.
                            user.show_personal_info()
                        elif help_option == "7":
                            # is user enter number "7 code will print every users name and last name."
                            print("Users of the bank:")
                            for i in self.users:
                                print(f"Name: {i.name}, Last Name: {i.last_name}")
                        elif help_option == "8":
                            # if user enter number "8" code will help to user change hes accounte.
                            change = input("Do You Want change account? (yes/no): ")


                            # if change equal "yes" and users list length is higher than 1 code will ask users hes other email and
                            # password
                            if change == "yes" and len(self.users) > 1:
                                email = self.empty("Enter your email: ")
                                password = self.empty("Enter your password: ")
                                user = self.login(email, password) # this is same as login function
                                if user: # if is not empty code will print message that user saccessfuly change hes accounte.
                                    console.print(f"You Login to accout", style="bold green")
                            # if change equal to "yes" and users list length is less than 1 or equal to 1 code will print alert message.
                            elif change == "yes" and len(self.users) <= 1:
                                console.print("You can't change accounte if you have only one", style="bold red")
                            # if change equal to "no" code will print message that change accounte cancle.
                            elif change == "no":
                                console.print("Change account cancle", style="bold green")
                            # otherways code will print alert message if you dont enter "yes" or "no".
                            else:
                                console.print("Enter only yes or no.", style="bold red")
                        # if user enter number "9" you exit from our bank accounte and code will end
                        elif help_option == "9":
                            transaction = input("Before you go, we have the coolest offer for you in the form of a loan? Do you want it? (yes/no): ")

                            if transaction == "yes":
                                print("Your response has been received. We will contact you later.")
                                running = False
                                break
                            elif transaction == "no":
                                print("Thanks for using our bank!")
                                running = False
                                break
                            else:
                                console.print("Enter only yes or no.", style="bold red")
                        else:
                            console.print("Enter a valid option.", style="bold red")
                # otherways if email or password is inccorect code will print alert message.
                else:
                    console.print("Login failed.", style="bold red")
            # if accounte equal "no" and users list length is greater than 1 or equal to one code will print alert message beacouse
            # if you have one accounte or more than one you cant enter no beacouse your allready have accounte.
            elif account == "no" and len(self.users) >= 1:
                console.print("You allready have account", style="bold red")
            # if accounte equal to "no" code will call register function.
            elif account == "no":
                self.register()
            # otherways if you dont enter yes or no print will alert message
            else:
                console.print("Please enter 'yes' or 'no'.", style="bold red")


# in this line of code if dunder name equal to dunder main code will start and call main function from Start class
if __name__ == "__main__":
    Start().main()
