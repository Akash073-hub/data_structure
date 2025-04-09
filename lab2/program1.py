a=[10,89,9,56,4,80,8]
maximum=a[0]
minimum=a[0]
for i in range(0,len(a)):
    if(maximum<a[i]):
        maximum=a[i]
    elif(minimum>a[i]):
        minimum=a[i]
print(maximum,minimum)
a.remove(maximum)
a.remove(minimum)
second_maximum=a[0]
second_minimum=a[0]
for j in range(0,len(a)):
    if(second_maximum<a[j]):
        second_maximum=a[j]
    elif(second_minimum>a[j]):
        second_minimum=a[j]
print(second_maximum,second_minimum)
