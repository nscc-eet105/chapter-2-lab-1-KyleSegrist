
#Kyle Segrist
#Lab2-1
#June 16 2025
user_first_name = input('Enter your first name:')
user_last_name = input('Enter your last name:')
marble_qty = int(input('enter the number of marbles you wish to purchase:'))
marble_price = float(1.20)
total = marble_qty * marble_price
message = 'Order prepared for '+ user_first_name + user_last_name

print(message)

print( marble_qty , 'marbles ordered @', marble_price)
    
 
print(f' Total cost is ${total:,.2f}')

