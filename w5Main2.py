def computerGrade(marks):
    if(90<=marks and marks<=100):
        grade='A'
    elif(80<=marks and marks<90):
        grade='B'
    elif(70<=marks and marks<80):
        grade='C'
    elif(60<=marks and marks<70):
        grade='D'
    else:
        grade='F'
    return grade
def lab1():
    marks=raw_input("enter marks")
    marks=float(marks)
    print marks
    mygrade=computeGrade(marks)
    print mygrade

def main():
    lab1()

main()