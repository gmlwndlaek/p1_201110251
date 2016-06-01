def drawSquarWithCoords(coords):
    x1=coords[0][0]
    y1=coords[0][1]
    x2=coords[1][0]
    y2=coords[1][1]


def getCoordsFromFile(aFile):
    coords=[]
    for line in fin:
        line1=line.split(',')
        aRect=[(line1[0], line1[1]), (line1[2], line1[3].strip())]
        coords.append(aRect)
    return coords


def lab13():
    fin=open('coords.txt','r')
    mycoords = getCoordsFromFile(fin)
    fin.close()


def main():
    lab13()

if __name__=="__main__": 
    main() 