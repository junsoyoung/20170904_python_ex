# coffee.py

coffee = 10

while True:
    money = int( input('Please, input your money'))
    if( money == 300):
        print( 'I will give you coffee.')
        coffee -= 1
    elif money > 300:
        print( 'I will give you change %d and coffee' % (money-300))
        coffee -= 1
    else:
        print( 'I will return your money and not give you the coffee.')
        print( 'The remained coffee is %d.' % coffee)

    if not coffee:
        print( 'Sold out')
        break
