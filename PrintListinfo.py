number=[]
n=0
sum=0
print("=================Information Providing System for Number List================\n")
print("As you enter a number, It wil give you the sum, median, and average of a list of numbers.\n")

while True :
    print("Enter numbers. (To finish press 'Enter' key)")
    n=input()
    if len(n)==0:
        break
    number.append(float(n))
    
number.sort()
number_center=int(len(number)/2)
if len(number)%2==1:
    median=number[number_center]
else:
    median=(number[number_center-1]+number[number_center])/2
for i in number:
    sum=sum+i
average=sum/len(number)
    
print("You entered\n",number)
print("sum : %.2f" %sum)
print("median : %.2f" %median)
print("average : %.2f" %average)
