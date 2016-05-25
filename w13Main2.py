data=[1,2,3,4,5,6,7,8,9,10]
fout=open('outputNumber.txt', 'w')
for i in data:
    toPrint="{0}\t".format(i)
    if (i%2==0):
        toPrint="{0}\t\n".format(i)
    fout.write(toPrint)
fout.close()
%load outputNumber.txt