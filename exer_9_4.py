# comments
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if not line.startswith("From ") : continue
    linelst = list()
    linelst = line.rstrip().split()
    counts[linelst[1]] = counts.get(linelst[1],0) + 1


bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword,bigcount
