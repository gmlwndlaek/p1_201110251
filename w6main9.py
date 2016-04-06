"""
@author mhj
@since 160406
"""
def sum3_5(begin, end):
    sum=0
    for i in range(begin, end):
        if (i % 3 == 0 or i % 5 == 0):
            sum = i+sum
    print sum
    return sum        


def findLeapYear():
    sel=int(raw_input("year?"))
    if (sel%4 == 0) and (sel%100!=0 or sel%400==0):
        print "leap year"
    else:
        print "not leap year"

def lab6():
    sum3_5(0, 1001)
    findLeapYear()

def main():
    lab6()

if __name__=="__main__":
    main()

raw_input()