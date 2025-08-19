n=int(input("Enter the no"))
temp=n
rev=0
while(n>0):
    i=n%10
    rev=rev*10+i
    n=n//10
if(temp==rev):
        print("palindrome")
else:
        print("not a palinfrome")

