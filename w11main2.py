list_veryGood = [10.3, 8.5, 24.4, 12.9, 7.4, 5.9, 12.9, 10.1, 13.1, 10.6, 27.1, 16.2, 11.4, 12.2, 13.5, 13.7]
list_good = [36.1, 31.7, 39.8, 33.1, 25.8, 24.6, 27.9, 38.9, 37.1, 34.6, 40.0, 37.8, 29.8, 26.5, 29.7, 37.6]
list_bad = [10.3, 12.4, 3.8, 7.2, 15.6, 17.1, 11.2, 7.0, 8.7, 13.4, 2.9, 6.8, 14.8, 14.9, 11.1, 4.1]
list_veryBad = [3.9, 4.7, 1.5, 2.0, 6.7, 7.1, 4.8, 2.0, 1.5, 1.9, 1.5, 0.8, 4.9, 4.4, 2.4, 1.2]

sum=0

for i in list_veryGood + list_good:
    sum=sum+i

total = len(list_veryGood+list_good)

aver = sum/total

print aver

sum=0

for i in list_veryBad + list_bad:
    sum=sum+i

total = len(list_veryBad+list_bad)

aver = sum/total

print aver

raw_input()