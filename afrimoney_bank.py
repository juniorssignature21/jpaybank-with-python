import csv


class AfrikMoney:
    firstName = ''
    lastName = ''
    phone = ''
    yourage = ''
    acct_balance = 0
    password = ''
    confirm_password = ''
    acct_no = ''
    
    def register(self):
          AfrikMoney.firstName = input("Enter your first Name: ")
          AfrikMoney.lastName = input("Enter your Last Name: ")
          while True:
                    AfrikMoney.phone = str(input("Enter a number: "))
                    if len(AfrikMoney.phone) == 11 and AfrikMoney.phone.isdigit():
                              print("✅ please proceed!")
                              break
                    else:
                              print('❌ invalid phone number')
                              continue
          while True:
                    AfrikMoney.yourage = int(input("How old are you?: "))
                    if AfrikMoney.yourage >= 18:
                         print("✅ verified!")
                         break
                    else:
                         print("❌**********\nYou are not eligible\nYou must be 18 yrs and above!")
                         exit()        

          AfrikMoney.acct_balance = 0
          while True: 
                    AfrikMoney.password = input('create 6-digits login pin: ')
                    if len(AfrikMoney.password) == 6 and AfrikMoney.password.isdigit():
                         break
                    elif len(AfrikMoney.password) < 6 and AfrikMoney.password.isdigit():
                         print("password must not be less than 6-digits")
                         continue
                    else:
                         print("password must not be greater than 6-digits")
                         continue
          while True:     
               AfrikMoney.confirm_password = input('confirm 6-digits login pin: ')
               if AfrikMoney.confirm_password == AfrikMoney.password:
                    print('✅ Correct!\n')
                    break
               else:
                    print('❌ Passwords do not match!')
                    continue


          AfrikMoney.acct_no = AfrikMoney.phone[1:]
          
          print(f"hello {AfrikMoney.firstName} {AfrikMoney.lastName}\nYour phone number is: {AfrikMoney.phone}\nAnd you {AfrikMoney.yourage} years old!\nYour account number is: {AfrikMoney.acct_no}")

          

          new_data = {
          AfrikMoney.phone:AfrikMoney.confirm_password
          
          }

          file_path = 'detail.csv'
          with open(file_path, 'a', newline='') as f:
               fieldnames = [AfrikMoney.phone,AfrikMoney.confirm_password]
               writer = csv.DictWriter(f, fieldnames=fieldnames)

               if f.tell() == 0:
                    writer.writeheader()

                    writer.writerow(new_data)

          print("Details added successfully")


    def login(self):
          log = input("Enter your phone number: ")
          logs = input("Enter your 6-digits login password: ")


          with open ('detail.csv', 'r') as file_name:
                file = csv.DictReader(file_name)

                for row in file:
                      if row[log] == logs:
                            print("✅ **********\nSuccessfully logged in")
                            self.user_option(self)
                            break
                      else:
                            print("Wow")
                      



    def user_option(self):
        print("Welcome to Jpay online banking!\nChoose an Option below:")
        print('1: Check balance')
        print('2: Withdraw')
        print('3: Deposit')
        print('4: Transfer')
        print('5: Account details')
        user = input()
        if user == '1':
             self.get_balance(self)
             self.user_option(self)

        elif user == '2':
             self.withdrawal(self)
             self.user_option(self)
        elif user == '3':
             self.deposit(self)
             self.user_option(self)
        elif user == '4':
             self.transfer(self)
             self.user_option(self)
        elif user == '5':
             print(f"Your Full Name: {AfrikMoney.firstName} {AfrikMoney.lastName}\nAge: {AfrikMoney.yourage} yrs old\nPhone Number: {AfrikMoney.phone}\nAccount number: {AfrikMoney.acct_no}\nBalance: {AfrikMoney.acct_balance}")

    def get_balance(self):
         check = input('Would you like to check your account balance?(y/n) ').lower()
         while True:
            if check == 'y':
               print(f'{AfrikMoney.firstName} Your balance is ${AfrikMoney.acct_balance:.2f}\n\n')
               #  another = input('Would you like to continue? ')
               #  if another == 'y':
               AfrikMoney.user_option(self)
               break
            elif check == 'n':
                print('OK')
                exit()
            else:
                print('❌**********\nInvalid option')
                exit()

    def deposit(self):
        amount = int(input('Enter amount to deposit: '))
        AfrikMoney.acct_balance = AfrikMoney.acct_balance + amount
        print('✅ Successful!')
        self.get_balance(self)
        

    def withdrawal(self):
         withdraw_amount = int(input('Enter amount to withdraw: '))
         if withdraw_amount <= AfrikMoney.acct_balance:
              AfrikMoney.acct_balance = AfrikMoney.acct_balance - withdraw_amount
              print(f'✅**********\nTransaction Sucessful!')
              self.get_balance()

         else:
              print(f'❌ **********\nInsufficient funds!')

     
    def transfer(self):
         trans = int(input("Enter amount to transfer: "))
         print("**********\nTransaction processing\n**********")
         if self.acct_balance >= trans:
              AfrikMoney.acct_balance = AfrikMoney.acct_balance - trans
              print(f"Transaction Successful\n**********\nYou have successfully tranfered ${trans} to ")
              self.get_balance()

         else:
              print(f"❌**********\nTransaction Unsuccessful\n**********\nInsufficient funds\nYour balance is {AfrikMoney.acct_balance}") 
              


            
              
                         

    
          
