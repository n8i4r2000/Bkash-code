class Bkash:
    def __init__(self, user_reg=None, send_money=None, recharge=None, check_amount=None, name=None, phone=None, check_balance=2000 ):
        self.user_reg = user_reg
        self.name = name
        self.phone = phone
        self.check_amount = check_amount
        self.send_money = send_money
        self.recharge = recharge

    def register(self):
        user_reg = input("Register or Login Your Bkash: ")
        name = input("Enter Your Name: ")
        phone = int(input("Enter Your Bkash Account Number: "))
        pin = int(input("Enter Your Bkash Pin: "))

        self.user_reg = {
            "user_reg": user_reg,
            "name": name,
            "phone": phone,
            "pin": pin
        }

        print(f"Your Bkash Registration is Successful. Welcome to the Bkash Dashboard! {self.user_reg['name']}")




    def check_balance(self):
        phone = input("Enter your phone number: ")
        user = self.find_user_by_phone(phone)

        if user:
            print(f"Your current balance is: {user.balance}")
        else:
            print("User not found!")

    def send_money(self):
        sender_phone = input("Enter your phone number: ")
        sender = self.find_user_by_phone(sender_phone)

        if not sender:
            print("Sender not found!")
            return

        receiver_phone = input("Enter receiver's phone number: ")
        receiver = self.find_user_by_phone(receiver_phone)

        if not receiver:
            print("Receiver not found!")
            return

        amount = float(input("Enter the amount to send: "))

home = Bkash()
home.check_balance
home.send_money

home.register()




print()
