import json

# helper funtions
def prompt(message):
	answer = input(message).lower()

	if answer == 'n':
		return True

	return False

def check_valid(index, options):
	return index >= 0 and index < len(options)

def available_stock(item, amount):
	return item['qty'] >= amount

def check_exist_temp(item, temp_order):
	return item['name'] in [a for x in temp_order for a in x.values()]

def get_data(item, item_list):
	for i in item_list:
		if i['name'] == item['name']:
			return i

	return False

def count_total_price(temp_order):
	total = 0
	for order in temp_order:
		total += int(order['price']) * order['qty']

	return total

def get_json_data(file):
	with open(file) as json_data:
		return json.load(json_data)

def save_menus(file, data):
    with open(file, 'w') as outfile:
        json.dump(data, outfile)