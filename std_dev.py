n=int(input("Enter the number of element to be entered in list: "))
b=[]
for i in range(n):
    a=int(input('enter the element to enter in list'))  
   
    b.append(a)
print(b)
sum=0
for i in range(len(b)):
    sum+=b[i]
mean = sum/len(b)
print(mean)

sum_of+dev= 0
for i in range(len(b)):
    c=(b[i]- mean)**2
    sum_of_dev+=c
    Standard_Deviation = ((sum_of_dev)/len(b))**0.5
print("Standard Deviation of sample is ",Standard_Deviation)
