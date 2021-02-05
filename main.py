def add(number1,number2):
  result = number1 + number2
  return result

def sub(number1,number2):
  result = number1 - number2
  return result

def mul(number1,number2):
  result = number1 * number2
  return result

def div(number1,number2):
  result = number1 / number2
  return result
#====================
def menu():
  run = 'True'
  while run == 'True':
    number1 = input("Enter 1st value\n--> ")
    number2 = input("Enter 2nd value\n--> ")
    print("Choose the action you would like to perform")
    print("[1] Add\n[2] Subtract\n[3] Multiply\n[4] Divide")
    option = int(input("\n--> "))
    if option == 1:
      print(add(number1,number2))
    elif option == 2:
      print(sub(number1,number2))
    elif option == 3:
      print(mul(number1,number2))
    elif option == 4:
      print(div(number1,number2))
    run = input("Enter True or False\n--> ")

# main program
menu()