file_name = input("Enter a file name: ")
file = open(file_name)

counts = dict()

for line in file:
	words = line.split()

	for word in words:
		counts[word] = counts.get(word, 0) + 1

print("#######################")
print("Counts", counts)
print("#######################")

big_count = None
big_word = None

for word, count in counts.items():
	if big_word is None or count > big_count:
		big_word = word
		big_count = count

print("#######################")
print(big_word, big_count)
print("#######################")
