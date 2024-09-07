#CHECK YOUR AGE WHETHER YOU ARE A CHILD,TEENAGER,ADULT,SENIOR CITIZEN
a = int(input("YOUR AGE :"))
if(a <= 12):
    print("YOU ARE A CHILD")
elif(a >= 13 and a <= 19):
    print("YOU ARE A TEENAGER")
elif(a >= 20 and a <= 59):
    print("YOU ARE ADULT")
else:
    print("YOU ARE SENIOR CITIZEN")
