tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
			 
def printTable(table):
	colwidths = [0] * len(tableData)
	lines = [ [] for i in range(len(tableData[0]))]
	for i, col in enumerate(tableData):
        maxlen = 0
        for val in col:
            maxlen = max(maxlen, len(val))
		colwidths[i]=maxlen
	for i, col in enumerate(tableData):
        for j, val in enumerate(col):
            chars = list(val)
            blank_chars = [" "] * (colwidths[i] - len(chars) + 1)
            blank_chars.extend(chars)
            lines[j].append("".join(blank_chars))
    for line in lines:
        print("".join(line))
table_print(tableData)