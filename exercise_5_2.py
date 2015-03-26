largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        numi = int(num)
    except:
        print "Invalid input"  
        
    if largest is None:
        largest = numi
    elif numi > largest:
        largest = numi

        
    if smallest is None:
        smallest = numi
    elif numi < smallest:
        smallest = numi



print "Maximum is", largest
print "Minimum is", smallest
