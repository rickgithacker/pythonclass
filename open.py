fhand = open('crap.txt','r')
count = 0
for line in fhand:
    count = count + 1
    line = line.rstrip()
    print line
print count
