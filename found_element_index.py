# Returns the index of the first occurrence of the element 

def find_index(ml, e):
	print(f"list: {ml}")
	print(f"elemet: {e}")
	for index in range(len(ml)):
		if e == ml[index]:
			return index
	return "There is no element in the list"
	

my_list = [i for i in range(10, 100)]
my_list = my_list+[j for j in range(20, 80)]

number = input("Enter a positive number: ")

print(f"index: {find_index(my_list, int(number))}")