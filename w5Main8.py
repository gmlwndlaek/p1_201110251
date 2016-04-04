height=raw_input("What is your height?")
weight=raw_input("What is your weight?")

height=float(height)
weight=float(weight)

heightM=height/100

bmi=weight/(heightM*heightM)

print bmi

def computebmi(height, weight):
    if bmi<18.5:
        print "Under weight"
    elif bmi>=18.5 and bmi<23.0:
        print "normal weight"
    elif bmi>=23.0 and bmi<25.0:
        print "overweight"
    else:
        print "obese"
        
computebmi(height, weight)
        
raw_input()
