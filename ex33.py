numbers = []

def loop_numbers(count, aug):
    i = 0
    while i < count:
        print "At the top i is %d" % i
        numbers.append(i)

        i += aug
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

loop_numbers(8, 2)

print "The numbers: "

for num in numbers:
    print num
