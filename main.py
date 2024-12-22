#Banking program with multiple options

#Create Values for program
bank_balance = 1000
#Create Dict for bank options
choices = {1 : "SHOW BALANCE",
           2 : "WITHDRAWAL",
           3 : "DEPOSIT",
           4 : "EXIT"}

#Print start menu with options
def start_menu():
      print("------Bank of Emmanuel------")
      print("What would you like to do today? ")
      for key, value in choices.items():
            print(f" {key} : {value}")

#Mitigate ValueError with Try/Except
def banking_choice():
      while True:
            try:

                  choice = int(input(("Please select 1, 2, 3, or 4: ")))

                  if choice in choices.keys():
                        print(f"You've chosen: {choices[choice]}")
                        return choice
                  else:
                        print(f"{choice} is not a valid option. ")
            except ValueError:
                  print("Please select a number (1-4). ")

#Define all banking options
def SHOW_BALANCE():
      print(f"Your balance is currently ${bank_balance} ")
      another_option()

def WITHDRAWAL():
      global bank_balance
      print(f"Your balance is currently ${bank_balance} ")
      with_amount = float(input("How much would you like to withdraw?: "))
      bank_balance -= with_amount
      print(f"After withdrawal, your balance is ${bank_balance} ")
      another_option()

def DEPOSIT():
      global bank_balance
      print(f"Your balance is currently ${bank_balance} ")
      dep_amount = float(input("How much would you like to deposit?: "))
      bank_balance += dep_amount
      print(f"After your deposit, your balance is ${bank_balance} ")
      another_option()

def EXIT():
      print("Thanks for banking with us today!")

#Creating a function that easily loops the banking program
def another_option():
      option = input("Would you like to choose another option? (YES/NO): ")
      if option.lower() == "yes":
            start_menu()
            choice = banking_choice()
            handle_choice(choice)
      elif option.lower() == "no":
            print("Thank you for banking with us today! ")
      else:
            print("That is not a valid option")
            another_option()

#Creating function to handle banking choice
def handle_choice(choice):
      if choice == 1:
            SHOW_BALANCE()
      elif choice == 2:
            WITHDRAWAL()
      elif choice == 3:
            DEPOSIT()
      elif choice == 4:
            EXIT()
            return

#Defining main program
def main():
      start_menu()
      choice = banking_choice()
      handle_choice(choice)

if __name__ == "__main__":
      main()
