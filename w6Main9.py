def sum3_5(begin, end):
    sum=0
    for i in range(begin, end):
        if (i % 3 == 0 or i % 5 == 0):
            sum = i+sum
    print sum
    return sum

sum3_5(0, 1001)        

raw_input()