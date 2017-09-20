run = True

menus = [
	{
		'name': 'Coca-cola',
		'price': '15000',
		'qty': 20
	},
	{
		'name': 'Sprite',
		'price': '10000',
		'qty': 20
	},
	{
		'name': 'Nescafe',
		'price': '5000',
		'qty': 20
	},
	{
		'name': 'Kitkat',
		'price': '5000',
		'qty': 20
	},
	{
		'name': 'Fitbar',
		'price': '5000',
		'qty': 20
	},
	{
		'name': 'Mentos',
		'price': '5000',
		'qty': 20
	}
]

def prompt(message):
	answer = input(message).lower()

	if answer == 'n':
		return True

	return False

def checkValid(index, options):
	return index >= 0 and index < len(options)

def available(index):
	return menus[index]['qty'] > 0

def available_stock(item, amount):
	return item['qty'] >= amount

def check_exist_temp(item, temp_order):
	return item['name'] in [a for x in temp_order for a in x.values()]

def get_data(item, item_list):
	for i in item_list:
		if i['name'] == item['name']:
			return i

def count_total_price(temp_order):
	total = 0
	for order in temp_order:
		total += int(order['price']) * order['qty']

	return total

def reduce_stock(temp_order):
	for order in temp_order:
		if order['name'] in [a for x in menus for a in x.values()]:
			item = get_data(order, menus)
			item['qty'] -= order['qty']

while run:
	print("======= Vending Machine v1 =======\n")

	# print information
	print("No. | Name | Price | Stock")
	print("--------------------------")

	for index, item in enumerate(menus):
		if item['qty'] <= 0:
			msg_stock = "Item out of stock"
		else:
			msg_stock = item['qty']
		print("{no}. | {name} | {price} | {stock}".format(no=index + 1, name=item['name'], price=item['price'], stock=msg_stock))

	print("\n") # blank space ------------------------------------

	# ================= start ordering =================
	ordering = True

	temp_order = []
	
	while ordering:
		# ============= choose item ==============
		invalidChoice = True

		while invalidChoice:
			choice = int(input("Input the number to choose the item: "))

			choice_index = choice - 1

			# check valid choice
			if checkValid(choice_index, menus):
				# check if still have stock
				if available(choice_index):
					invalidChoice = False
				else:
					print("Item out of stock")
					print("\n")
			else:
				print("Not in the list of choices!")
				print("\n")

		chosen_item = menus[choice_index]

		# ================= input amount =================
		invalidAmount = True

		while invalidAmount:
			amount = int(input("Input the amount for " + chosen_item['name'] + ": "))

			if check_exist_temp(chosen_item, temp_order):
				item = get_order(chosen_item, temp_order)
				total_amount = item['qty'] + amount

				if available_stock(chosen_item, total_amount):
					invalidAmount = False
					item['qty'] = total_amount
				else:
					print("Your total number of order for {} exceeded the stock".format(item['name']))
					print("\n")
			else:
				if available_stock(chosen_item, amount):
					invalidAmount = False
					new_item = {
						'name': chosen_item['name'],
						'price': chosen_item['price'],
						'qty': amount
					}
					temp_order.append(new_item)
				else:
					print("You can't buy more than amount of the stock")
					print("\n")

		stop_order = prompt("Do you want to add another item? (y/n): ")

		if stop_order:
			ordering = False

	print("\n") # blank space ------------------------------------

	total_price = count_total_price(temp_order)

	print("The total price is: {}".format(total_price))

	# # ================= payment =================
	for i in range(1, 21):
		price_amount = i * 5000
		print(str(i) + ". " + str(price_amount))

	invalid_price = True

	while invalid_price:
		payment_option = int(input("Input the payment option: "))
		
		payment = payment_option * 5000

		if payment >= total_price:
			change = payment - total_price
			invalid_price = False
		else:
			print("Payment is not enough!")
			print("\n") # blank space ------------------------------------

	print("Change: {}".format(change))

	# reduce stock
	reduce_stock(temp_order)

	print("\n") # blank space ------------------------------------

	quit = prompt("Do you want to buy again? (y/n): ")

	print("\n") # blank space ------------------------------------

	if quit:
		run = False
