alama=int(input("Weka alama yako:"))
# if elif else statement

if alama>80 and alama<=100:
    print("You scored an A")

elif alama>60 and alama<=80:
    print("You have a B....")

elif alama>40 and alama<=60:
    print("You have a C")

elif alama>30 and alama<=40:
    print("You have a D")

elif alama>=0 and alama<=30:
    print("You have an E")

else:
    print("Wrong input")
