fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    linelst = list()
    linelst = line.rstrip().split()
    for i in linelst:
        if i not in lst:
            lst.append(i)
lst.sort()
print lst
