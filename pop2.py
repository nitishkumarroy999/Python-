fruit = [['Orange','Fruit'],['Banana','Fruit'], ['Mango', 'Fruit']]
consume = ['Juice', 'Eat']
possible = []

# Iterating item in list fruit
for item in fruit :
	# Iterating use in list consume
	for use in consume :
		item.append(use)
		possible.append(item[:])
		item.pop(-1)
print(possible)
