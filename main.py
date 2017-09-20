import helpers

run = True

menus = helpers.get_json_data('menus.json')

def available(index):
	return menus[index]['qty'] > 0

def available_after_ordered(index, temp_order):
	menu_item = menus[index]
	order_item = helpers.get_data(menu_item, temp_order)

	if order_item:
		if order_item['qty'] - menu_item['qty'] == 0:
			return False

	return True

def reduce_stock(temp_order):
	for order in temp_order:
		if order['name'] in [a for x in menus for a in x.values()]:
			item = helpers.get_data(order, menus)
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
			if helpers.check_valid(choice_index, menus):
				# check if still have stock
				if available(choice_index):
					# check if still have remaining stock after ordered (current order)
					if available_after_ordered(choice_index, temp_order):
						invalidChoice = False
					else:
						print("You have already ordered all remaining stock(s)")
						print("\n")
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

			if helpers.check_exist_temp(chosen_item, temp_order):
				item = helpers.get_data(chosen_item, temp_order)
				total_amount = item['qty'] + amount

				if helpers.available_stock(chosen_item, total_amount):
					invalidAmount = False
					item['qty'] = total_amount
				else:
					print("Your total number of order for {} exceeded the stock".format(item['name']))
					print("\n")
			else:
				if helpers.available_stock(chosen_item, amount):
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

		stop_order = helpers.prompt("Do you want to add another item? (y/n): ")
		print("\n") # blank space ------------------------------------

		if stop_order:
			ordering = False

	total_price = helpers.count_total_price(temp_order)

	print("The total price is: {}".format(total_price))

	# ================= payment =================
	for i in range(1, 21):
		price_amount = i * 5000
		print(str(i) + ". " + str(price_amount))

	invalid_price = True

	while invalid_price:
		payment_option = int(input("Input the payment option: "))

		if payment_option > 0 and payment_option <= 20:
			payment = payment_option * 5000

			if payment >= total_price:
				change = payment - total_price
				invalid_price = False
			else:
				print("Payment is not enough!")
				print("\n") # blank space ------------------------------------
		else:
			print("Payment option not available")

	print("Change: {}".format(change))

	# reduce stock
	reduce_stock(temp_order)
	helpers.save_menus('menus.json', menus)

	print("\n") # blank space ------------------------------------

	quit = helpers.prompt("Do you want to buy again? (y/n): ")

	print("\n") # blank space ------------------------------------

	if quit:
		run = False