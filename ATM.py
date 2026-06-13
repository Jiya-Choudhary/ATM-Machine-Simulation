print("ATM Machine")
pw = 4444
pin = int(input("Enter your pin: "))
balance = 500000
list = ["balance", "deposit", "withdraw","exit"]
while True:
    if pin == pw : 
        print(list)
        choice = input("Enter choice:")
        if choice == "balance":
            print("Your Balance is :", balance)
        elif choice == "deposit":
            amount = int(input("Enter amount to deposit:"))
            balance = balance + amount
            print("Your total balance is:",balance)
        elif choice == "withdraw":
            amount = int(input("Enter amount to withdraw:"))
            if amount<=balance:
               balance = balance - amount
               print("Your total balance is:",balance)
            else:
               print("Insufficient balance!")
        elif choice == "exit":
            print("Closed")
            break
        else:
            print("Not in choice!")
    else:
       print("Wrong Pin , Try Again")
       Option = ["Quit" , "Retry"]
       print(Option)
       S = input("Enter Option:")
       if S == "Retry":
          pin = int(input("Enter your pin: "))
       else:
           print("Quited")
           break




