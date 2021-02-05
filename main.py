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
  run = 'y'
  while run in ["y","yes"]:
    number1 = int(input("\nEnter 1st value\n--> "))
    number2 = int(input("Enter 2nd value\n--> "))
    print("\nChoose the action you would like to perform")
    print("\t[1] Add\n\t[2] Subtract\n\t[3] Multiply\n\t[4] Divide")
    option = int(input("\n--> "))
    if option == 1:
      print(add(number1,number2))
    elif option == 2:
      print(sub(number1,number2))
    elif option == 3:
      print(mul(number1,number2))
    elif option == 4:
      print(div(number1,number2))
    else:
      None
    
    print("\nWould you like to continue using Basic Calculator?")
    print("\t[Y] Yes\n\t[N] No")
    run = input("\n--> ").lower()

# main program
print("\nWelcome to Basic Calculator!")
menu()