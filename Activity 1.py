x = int(input("Enter the fee: "))
y = int(input("Enter the tip amount: "))

def tot_bill(bill_amount,tip_per):
    total = bill_amount *(1 + 0.01*tip_per)
    total = round(total,2)
    print (f"Please pay ${total}")

tot_bill (x,y)