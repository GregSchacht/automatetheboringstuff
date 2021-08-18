#Create the "meat"
def addcommas(commalist):
	strholder=''
	for i in commalist:
		if i != "and" and i != commalist[-1]:
			strholder=strholder + str(i) +','
		if i != commalist[-1]:
			strholder=strholder + ' '
	strholder=strholder+"and "+str(commalist[-1])
	print(strholder)

finallist=['scrimmy', 1, 'bingus', "trungle"]
print("We're gonna split up " + str(finallist))

addcommas(finallist)
