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
    number1 = int(input("\nEnter 1st number --> "))
    number2 = int(input("Enter 2nd value --> "))
    print("\nChoose the operation you would like to perform")
    print("\t[+] Add\n\t[-] Subtract\n\t[x] Multiply\n\t[/] Divide")
    option = input("\n--> ")
    if option == '+':
      print(add(number1,number2))
    elif option == '-':
      print(sub(number1,number2))
    elif option == 'x':
      print(mul(number1,number2))
    elif option == '/':
      print(div(number1,number2))
    else:
      None
    
    print("\nWould you like to continue using Basic Calculator?")
    print("\t[Y] Yes\n\t[N] No")
    run = input("\n--> ").lower()

# main program
print("\nWelcome to Basic Calculator!")
menu()