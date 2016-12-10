l = range(1,100)
number = 50

firstpoint = 0
midpoint = (len(l)-1)/2
lastpoint = len(l) - 1
found = False

while firstpoint <= lastpoint and found == False:
    if l[midpoint] == number:
        found = True
    elif l[midpoint] > number:
        lastpoint = midpoint
        midpoint = (firstpoint + midpoint)/2
    elif l[midpoint] < number:
        firstpoint = midpoint
        midpoint = midpoint = (firstpoint + midpoint)/2
        
if found:
    print "Found index " + str(midpoint)
else:
    print "not found"