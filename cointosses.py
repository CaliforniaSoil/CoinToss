import random 
xround = 0
countx = 0
county = 0
count = 0
for x in range(5000):
    x = random.random()
    xround = round(x)
    if xround == 1.0:
        countx += 1
        count += 1
        print "Attempt # {} Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(count,countx,county)
    if xround == 0.0:
        county += 1
        count += 1
        print "Attempt # {} Throwing a coin... It's a tail! ... Got {} head(s) so far and {}tail(s) so far".format(count, countx, county)
