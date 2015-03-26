x = 1 + 2 * 3 - 8 / 4
print x




def computepay(h,r):
    if h > 40:
        pay = (40 * r) + (h - 40) * r * 1.5
    else:
        pay = h * r 
    return pay

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)

p = computepay(h,r)

print p
