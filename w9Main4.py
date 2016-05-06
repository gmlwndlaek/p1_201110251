popoulation=list()
population=[[74425, 76326],[109688, 115744],[144796, 146776],[174996, 181676],[177841, 177434],[204630, 205980],[223373, 232245],[161055, 166130],[171576, 176735],[279169, 293772],[239450, 251066],[148690, 156510],[182977, 196992],[237792, 242641],[283869, 296762],[209344, 210282],[118965, 114441],[186503, 186856],[195734, 203014],[254381, 249472],[212401, 229111],[271654, 295354],[319197, 335045],[229829, 231671]]

mSum=0
wSum=0
total=list()
total2=list()

for i in range(0,len(population)):
    mSum+=population[i][0] 
    wSum+=population[i][1]
    total.append(population[i][0]+population[i][1])

mAver=mSum/len(population)
wAver=wSum/len(population)

print mSum
print wSum
print mAver
print wAver
print total


%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt

plt.bar(range(len(total)), total,align='center')
plt.xticks(range(len(total)), list(total2))
plt.show()