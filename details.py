from afrimoney_bank import *

class Jpay_details:
     details = {}
     print("1. Sign up")
     print("2. Sign in")
     details = input()
     if details == "1":
          AfrikMoney.register(self=AfrikMoney)
          AfrikMoney.user_option(self=AfrikMoney)
     elif details == "2":
          AfrikMoney.login(self=AfrikMoney)
          AfrikMoney.user_option(self=AfrikMoney)

              
         

         