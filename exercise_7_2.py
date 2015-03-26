# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
rsum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print line
    cpos = line.find(':')
    num = float(line[cpos+1:].strip())
    rsum = rsum + num
    count = count + 1
#print "Done"
#print count
print "Average spam confidence:",rsum/count
