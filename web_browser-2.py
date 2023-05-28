import urllib.request, urllib.parse, urllib.error
# from urllib import request, parse, error

# file_handle = urllib.request.urlopen("http://www.dr-chunk.com/page1.html")
file_handle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()
for line in file_handle:
	words = line.decode().split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
print(counts)
