name = input('What is your name? ')
color = input('Whats your favourite color? ')
print(name + ' likes ' + color)

#Exercise 2

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down paymemt: R{down_payment}")