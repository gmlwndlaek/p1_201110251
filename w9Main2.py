def adress():
    
    s='Hongjimoon streets of 20 February, Jongno-gu, Seoul'
    d1=dict()
    d2=dict()
    
    for word in s:
        asc = ord(word)
        if(48<=asc and asc<=57):
            if word not in d1:
                d1[word]=1
            else:
                d1[word]=d1[word]+1
        else:
            if word not in d2:
                d2[word]=1
            else:
                d2[word]=d2[word]+1
                
    print d1
    print d2
    
    d1.update(d2)
    
    %matplotlib inline
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(d1)), d1.values(),align='center')
    plt.xticks(range(len(d1)), list(d1.keys()))
    plt.show()                


adress()

raw_input()