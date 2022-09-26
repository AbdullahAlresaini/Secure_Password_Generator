import random


pass_len = int(input("Enter length of password:"))
password = ''
while(pass_len < 8):

    print("Password length must be 8 digit or more: ")
    pass_len = int(input("Enter length of password:"))
    if pass_len >= 8:
        break

array_of_carachter = ['a','b','c','d','e','f','g','h',
                      'i','j','k','l','m','n','o','p',
                      'q','r','s','t','u','v','w','x',
                      'y','z','A','B','D','E','F','G',
                      'H','I','J','K','L','M','N','O',
                      'P','Q','R','S','T','U','V','W',
                      'X','Y','Z','0','1','2','3','4',
                      '5','6','7','8','9','!','@','#',
                      '$','%','^','&','*','(',')','-',
                      '_','+','=','~','`','[',']','{',
                      '}','?','/','.',',','<','>',':',
                      ';','"',"'"]





for i in range(0,pass_len):

    password = password + random.choice(array_of_carachter)

print(password)

