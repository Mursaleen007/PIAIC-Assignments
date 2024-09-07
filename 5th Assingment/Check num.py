#CHECK THE NUMBER IS EVEN OR ODD , POSITIVE OR NAGATIVE 

Num = int(input("Number : "))

if(Num%2 == 0 and Num>= 0):
    print("NUMBER IS : EVEN \nNUM IS : POSITIVE ")
elif(Num%2 == 0 and Num<= 0):
    print("NUMBER IS : EVEN \nNUM IS : NAGATIVE")
elif(Num%2 != 0 and Num>= 0):
    print("NUMBER IS : ODD \nNUMBER IS : POSITIVE")
else:
    print("NUMBER IS : ODD \nNUMBER IS : NAGATIVE")