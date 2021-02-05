def add(num1,num2):
  result = num1 + num2
  return result

def sub(num1,num2):
  result = num1 - num2
  return result

def mul(num1,num2):
  result = num1 * num2
  return result

def div(num1,num2):
  result = num1 / num2
  return result

def rmd(num1,num2):
  divide = num1 // num2
  remainder = num1 % num2
  return ("Integer division:\t%s\nRemainder:\t%s" % (divide,remainder))

def pwr(num1,num2):
  result = num1 ** num2
  return result
#==============================
def menu():
  run = 'y'
  while run in ["y","yes"]:
    num1 = int(input("\nEnter 1st number --> "))
    num2 = int(input("Enter 2nd number --> "))
    print("\nChoose the operation you would like to perform")
    print("\t[+] Add\n\t[-] Subtract\n\t[x] Multiply\n\t[/] Divide\n\t[**] Power\n\t[//%] Integer Divison & Remainder")
    option = input("\n--> ")
    if option == '+':
      print(add(num1,num2))
    elif option == '-':
      print(sub(num1,num2))
    elif option == 'x':
      print(mul(num1,num2))
    elif option == '/':
      print(div(num1,num2))
    elif option == '//%':
      print(rmd(num1,num2))
    elif option == '^':
      print(pwr(num1,num2))
    else:
      None
    
    print("\nWould you like to continue using Basic Calculator?")
    print("\t[Y] Yes\n\t[N] No")
    run = input("\n--> ").lower()

# main program
print("\nWelcome to Basic Calculator!")
menu()