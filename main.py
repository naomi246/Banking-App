class RangeError(Exception):
  pass

class AnsError(Exception):
  pass

##FUNCTIONS AND PROCEDURES
      
#OPTION SELECTION     
def options_selections():
  try:
    print("Which of the following actions would you like to perform?")
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Put down $ on credit card")
    print("4) Cancel")
    action = int(input())
    if action > 4 or action < 1:
      raise RangeError
  except RangeError:
    print("Once you've chosen which action you'd like to perform, please enter the corresponding number.")
  except ValueError:
    print("Once you've chosen which action you'd like to perform, please enter the corresponding number.")  
  return action

#WRONG VALUE 
def wrong_value_withdraw(name_of_action, num):
  while True: 
    try:
      how_much = int(input("How much money would you like to "+name_of_action+"?: "))
      if how_much > num or how_much < 0:
        print("Please enter a number within the range of your total balance")
      else:
        return how_much
    except ValueError:
      print("Please enter a number!")

def wrong_value_all(name_of_action, num):
  while True: 
    try:
      how_much = int(input("How much money would you like to "+name_of_action+"?: "))
      if how_much < 0:
        print("Please enter a number greater than 0.")
      else: 
        return how_much
    except ValueError:
      print("Please enter a number")
  

#RESPONSE
def response(num):
  cont_ans_list = ["Continue", "continue", "CONTINUE"]
  quit_ans_list = ["Quit", "quit", "QUIT"]
  print("Your balance is now", "$"+str(num))
  cont_ans = input("Thank you using NAK banking services, would you like to coninue or quit: ")
  if cont_ans in cont_ans_list:
    return 1
  elif cont_ans in quit_ans_list:
    print("Thank you for using NAK banking services! Come again!")
    return -1

def log_in():
  while True:
    print("LOG IN:")
    user_try = input("Enter your username: ")
    pass_try = input("Enter your password: ")
    if user_try == username and pass_try == password:
      break
    elif user_try == username and pass_try != password:
      print("Your password does not match your username. Please try again!")
    elif user_try != username and pass_try == password:
      print("Your username does not match your password. Please try again!")
    else: 
        print("The log in info you've entered is incorrect, please try again!")

#THE MAIN CODE 
#MAKING AN ACCOUNT
print("Welcome to NAK bank!") 
while True:
  try:
      make_account = input("Would you like to create an account?(Yes or No): ")
      yes_ans = ["yes","Yes","YES","Y","y"]
      no_ans = ["no", "No", "NO","N","n"]
      if make_account in yes_ans:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print("Thank you for setting up an account with NAK bank!")
        log_in()
        break
      elif make_account in no_ans:
        print("Your information from this session will not be saved.")
        break
      else:
        raise AnsError
  except AnsError:
    print("Please answer yes or no!")
      
  

#LOGGING IN    


#WELCOME + CODE
while True: 
  try:
    print("Welcome to NAK Bank!")
    balance = int(input("What is the current balance of your account: "))
    if balance < 0:
      raise RangeError
    else: 
      break
  except RangeError: 
    print("Your current balance must be greater than or equal to zero!")
  except ValueError:
    print("Please enter the amount of money in your account!")

while True: 
  action = options_selections()
  #DEPOSIT
  if action == 1:
    deposit = wrong_value_all("deposit", balance)
    balance += deposit
    end = response(balance)
    if end == 1:
      continue
    elif end == -1:
      break 
  
  #WITHDRAWAL
  elif action == 2:
    withdraw = wrong_value_withdraw("withdraw", balance)
    balance -= withdraw
    end = response(balance)
    if end == 1:
      continue
    elif end == -1:
      break
    
  #CREDIT CARD
  elif action == 3:
    credit_card = wrong_value_all("put down on your credit card", balance)
    balance -= credit_card
    end = response(balance)
    if end == 1:
      continue
    elif end == -1:
      break
    
  #CANCEL
  elif action == 4:
    print("Thanks for using NAK banking services! Come again!")
    break

