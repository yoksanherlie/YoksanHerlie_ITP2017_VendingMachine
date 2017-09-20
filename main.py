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

def prompt():
	answer = input("Do you want to buy again? (y/n): ").lower()

	if answer == 'n':
		return True

	return False

def checkValid(index):
	return index >= 0 and index < len(menus)

def available(index):
	return menus[index]['qty'] > 0

def availableStock(item, amount):
	return item['qty'] >= amount

while run:
	print("======= Vending Machine v1 =======\n")

	# print information
	print("No. | Name | Price | Stock")
	print("--------------------------")

	for index, item in enumerate(menus):
		print("{no}. | {name} | {price} | {stock}".format(no=index + 1, name=item['name'], price=item['price'], stock=item['qty']))

	print("\n") # blank space ------------------------------------

	# ================= choose item =================
	invalid = True

	while invalid:
		choice = int(input("Input the number to choose the item: "))

		choice_index = choice - 1

		# check valid choice
		if checkValid(choice_index):
			# check if still have stock
			if available(choice_index):
				invalid = False
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

		if availableStock(chosen_item, amount):
			invalidAmount = False
			total_price = int(chosen_item['price']) * amount
		else:
			print("You can't buy more than amount of the stock")
			print("\n")

	print("\n") # blank space ------------------------------------

	print("The total price is: {}".format(total_price))

	# ================= payment =================
	not_enough = True
	change = 0

	while not_enough:
		payment = int(input("Input the payment: "))

		if payment >= total_price:
			change = payment - total_price
			not_enough = False
		else:
			print("Payment is not enough!")
			print("\n") # blank space ------------------------------------

	print("Change: {}".format(change))

	# reduce stock
	chosen_item['qty'] -= amount

	print("\n") # blank space ------------------------------------

	quit = prompt()

	print("\n") # blank space ------------------------------------

	if quit:
		run = False
