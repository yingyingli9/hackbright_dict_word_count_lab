import sys

text_file = open(sys.argv[1])

word_count = {}

for line in text_file:
    line = line.rstrip()
    line = line.lower()
    for c in line:
        if c in "?.!/;:,'\"_":
            line = line.replace(c, "")
    words = line.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1


for word, count in word_count.items():
    print word, count
