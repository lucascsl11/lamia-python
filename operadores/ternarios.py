promo = False
money = 2000

status = 'purchased' if promo or money > 1000 else 'not purchased'

print(status)