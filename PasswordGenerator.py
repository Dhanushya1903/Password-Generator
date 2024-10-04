import random
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Numbers = ['0','1','2','3','4','5','6','7','8','9']
Symbols = ['!','@','#','$','%','^','&','*','(',')','+']
print("Password Generator!!")
NoOfLetters = int(input("Enter the number of letters in the password : "))
NoOfDigits = int(input("Enter the number of digits iin the password : "))
NoOfSymbols = int(input("Enter the number of symbols in the password : "))
password_list = []
for i in range(1,NoOfLetters+1):
    char = random.choice(Letters)
    password_list.append(char)

for i in range(1,NoOfDigits+1):
    char = random.choice(Numbers)
    password_list.append(char)

for i in range(1,NoOfSymbols+1):
    char = random.choice(Symbols)
    password_list.append(char)

random.shuffle(password_list)

password = ""

for i in password_list :
    password = password + i
print("Your Password :",password)

