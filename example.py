amount = int(input("Enter amount"))
# if elif else statement

if amount>10000 and amount<=50000:
    print("Access granted")

elif amount>5000 and amount<=10000:
    print("Your balance is running out")

elif amount>500 and amount<=5000:
    print("You need to top up your account")

elif amount>=0 and amount<=500:
    print("Insufficient balance")

else:
    print("Accepted")