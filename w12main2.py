myfile=open('output.txt', 'w')
line1='first line\n'
myfile.write(line1)
line2='\tsecond line\n'
myfile.write(line2)
line3='third'
myfile.write(line3)
myfile.close()

myfile=open('output.txt', 'r')
for i in myfile:
    if i.find('line')>=0:
        print i.upper()
    else:
        print i
myfile.close()