#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

def generatePassword(num,sym,let):
  passwordList = []
  
  
  for i in range(1,num+1):
    r = random.randint(1,len(numbers)-1);
    passwordList+=numbers[r];
    
  for i in range(1,sym+1):
    r = random.randint(1,len(symbols)-1);
    passwordList+=symbols[r];

  for i in range(1,let+1):
    r = random.randint(1,len(letters)-1);
    passwordList+=letters[r];

    random.shuffle(passwordList)
  newP = ""
  for cher in passwordList:
      newP += cher

  
  return newP
  
    
print(generatePassword(nr_numbers,nr_symbols,nr_letters))