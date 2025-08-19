n=int(input("ENter the no"))
sum=0
while(n>0):
    i=n%10
    sum=sum+i
    n=n//10
print(sum)