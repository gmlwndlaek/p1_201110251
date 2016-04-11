x=list()
for i in range(0,1001):
    if(i%4==0 and i%5!=0):
        print i
        x.append(i)

def sumList(list):
    x=list
    sum=0

    for i in range(0,len(x)):
        sum=sum+x[i]

    return sum
print sumList(x)

raw_input()