from six.moves import input

def calculate_tip(bill_amount, tip_rate):
    tip = bill_amount * (tip_rate / 100.0)
    tip = round(tip, 2)
    total = bill_amount + tip

    return (tip, total)


def main():

    bill_amount = ""
    tip_rate = ""
    while not (bill_amount.isdigit() and tip_rate.isdigit()):
        bill_amount = input("What is the bill amount? ")
        tip_rate = input("What is the tip rate? ")

        if not bill_amount.isdigit():
            print("Please enter a valid number for the bill amount.")

    bill_amount = float(bill_amount)
    tip_rate = float(tip_rate)

    tip, total = calculate_tip(bill_amount, tip_rate)

    print("Tip:   ${:.2f}".format(tip))
    print("Total: ${:.2f}".format(total))

if __name__ == '__main__':
    main()
