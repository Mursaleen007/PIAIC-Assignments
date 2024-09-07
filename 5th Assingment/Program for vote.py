#CHECK A PERSON IS ELIGIBLE FOR VOTE
A = int(input("YOUR AGE : "))
if(A>=18):
    print("NEXT")
    b = (input("YOU HAVE NASHNALITY OF PAKISTAN :"))
    if(b == 'yes'):
            print("YOU ARE ELIGIBLE FOR VOTE")
    else:
     print("YOU ARE NOT ELIGIBLE FOR VOTE")
else:
    print("YOU ARE NOT ELIGIBLE FOR VOTE")