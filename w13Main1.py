import time
editor='mhj'
timeEdited=time.strftime(' %Y-%m-%d''%H:%M:%S')
fin=open('output.txt', 'r')
fout=open('outputUpper.txt','w')
for line in fin:
    words=line.split()
    for word in words:
        if word=='line':
            word = word.upper()
            print "[{0} edited {1}] {2}".format(editor,timeEdited,word)
        else:
            print word

fin.close()
fout.close()