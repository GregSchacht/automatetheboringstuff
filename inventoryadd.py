
def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k, v in inventory.items():
		print (str(v) +' ' + k)
		item_total += v
	print("Total number of items: " + str(item_total))
	
def addToInventory(inventory, addeditems):
	for k in addeditems:
		inventory.setdefault(str(k), 0)
		inventory[k]=inventory[k]+1
	return inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff=addToInventory(stuff, loot)
displayInventory(stuff)