pin=1234
amount=5000
user_pin=int(input("Enter the Pin Number:"))
if user_pin==pin:
    print("1.Deposite\n2.Withdraw\n3.BalanceEnquiry")
    ch=int(input("Enter your Choice"))
    if ch==1:
        damount=int(input("Enter the deposite amount:"))
        amount=amount+damount
        print("Your available balance",amount)
    elif ch==2:
        wamount=int(input("Enter the withdraw amount:"))
        amount=amount-wamount
        print("Your available balance",amount)
    elif ch==3:
        print("Your available balance",amount)
    else:
        print("Wrong input")
else:
    print("Invalide Pin Number")


