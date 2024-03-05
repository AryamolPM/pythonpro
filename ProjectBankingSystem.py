class Bank:
    def Account_login(self):
        account=input("Do you have an account? ")
        if account=="No":
            print("Create a new account!")
            number = int(input("Enter your account number: "))
            name = input("Enter your name: ")
            password=input(("Please enter a strong password (Characters not more than 8): "))
            print("Account created successfully!.\nYou are advised to accept the terms and conditions ")

        else:
            print("Ok! Please login with your account number and password")
            number=int(input("Enter your account number: "))
            password=input("Enter your password:")
            print("captcha=qaz12")
            captcha="qaz12"
            user=input("Enter the captcha:")
            if captcha==user:
                print("Done!Save this password for future use.")
            else:
                print("Something wrong! Try again")
    def amount_depositing(self):
        print("CASH DEPOSITING")
        name=input("Enter your name: ")
        phone_number=input("Enter your phone number:")
        amount=int(input("Enter the amount: "))
        print("OTP will be send to your phone: OTP:4848")
        otp=int(input("Enter otp: "))
        if otp==4848:
            print("Transaction Successful")
        else:
            print("Transaction Failed! Try Again")
    def amount_withdrawal(self):
        print("CASH WITHDRAWAL")
        name = input("Enter your name: ")
        phone_number = input("Enter your phone number:")
        amount = int(input("Enter the amount: "))
        print("OTP will be send to your phone: OTP:4848")
        otp = int(input("Enter otp: "))
        if otp == 4848:
            print("Transaction Successful")
        else:
            print("Transaction Failed! Try Again")
b1=Bank()
b1.Account_login()
print("_____________")
user=input("Are you here to deposit or withdraw the cash?")
if user=="Deposit":
    b1.amount_depositing()
else:
    b1.amount_withdrawal()