# This will calculate the total amount for an electric bill

hours = int(input("Enter the KW hours used: "))
if hours <= 1000 :
    amountOwed = (hours * 7.633) / 100
elif hours > 1000 :
    amountOwed = ((7.633 * 1000) + (9.259 * (hours - 1000))) / 100

print("Amount owed is $%.2f" % amountOwed)