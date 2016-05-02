def charCount(word):
    w= word
    d=dict()
    for c in w:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print d
    
def lab9():
    charCount('sangmyung')

def main():
    lab9()
    
if __name__=="__main__":
    main()

